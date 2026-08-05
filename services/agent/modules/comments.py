"""Comments module: visitor comments stored in Neo4j graph, cached in Redis."""

import hashlib
import json
import time
from typing import Dict, List, Optional

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

from core import config
from core.deps import check_rate_limit, require_api_key
from core.storage import get_neo4j, get_redis, init_comment_schema

_CACHE_TTL = config.COMMENT_CACHE_TTL


def _cache_key(page_id: str) -> str:
    return f"comments:{hashlib.sha256(page_id.encode()).hexdigest()}"


def list_comments(page_id: str, limit: int = 50) -> List[Dict]:
    r = get_redis()
    key = _cache_key(page_id)
    cached = r.get(key)
    if cached:
        try:
            return json.loads(cached)
        except json.JSONDecodeError:
            pass

    driver = get_neo4j()
    with driver.session(database=config.NEO4J_DATABASE) as s:
        result = s.run(
            """
            MATCH (c:Comment)-[:ON]->(p:Page {id: $page_id})
            OPTIONAL MATCH (c)<-[:REPLY_TO]-(reply:Comment)
            OPTIONAL MATCH (author:Commenter)-[:AUTHORED]->(c)
            WITH c, author, count(reply) AS reply_count
            ORDER BY c.created_at DESC
            LIMIT $limit
            RETURN c.id AS id, c.text AS text, c.name AS name, c.created_at AS created_at,
                   author.email_hash AS email_hash, reply_count
            """,
            page_id=page_id, limit=limit,
        )
        comments = [
            {
                "id": r["id"],
                "text": r["text"],
                "name": r["name"],
                "created_at": r["created_at"],
                "email_hash": r["email_hash"],
                "reply_count": r["reply_count"],
            }
            for r in result
        ]
    r.setex(key, _CACHE_TTL, json.dumps(comments))
    return comments


def add_comment(
    page_id: str,
    page_title: str,
    name: str,
    text: str,
    email: str = "",
    parent_id: Optional[str] = None,
) -> Dict:
    comment_id = hashlib.sha256(f"{page_id}:{time.time()}:{text}".encode()).hexdigest()[:16]
    created_at = int(time.time())
    email_hash = hashlib.sha256(email.encode()).hexdigest()[:12] if email else "anonymous"

    driver = get_neo4j()
    with driver.session(database=config.NEO4J_DATABASE) as s:
        s.run(
            """
            MERGE (p:Page {id: $page_id})
            SET p.title = $page_title
            MERGE (u:Commenter {email_hash: $email_hash})
            CREATE (c:Comment {id: $comment_id, text: $text, name: $name, created_at: $created_at})
            CREATE (c)-[:ON]->(p)
            CREATE (u)-[:AUTHORED]->(c)
            WITH c
            OPTIONAL MATCH (parent:Comment {id: $parent_id})
            FOREACH (_ IN CASE WHEN parent IS NOT NULL THEN [1] ELSE [] END |
                CREATE (c)-[:REPLY_TO]->(parent)
            )
            """,
            page_id=page_id, page_title=page_title, email_hash=email_hash,
            comment_id=comment_id, text=text, name=name, created_at=created_at,
            parent_id=parent_id,
        )

    get_redis().delete(_cache_key(page_id))
    return {
        "id": comment_id, "text": text, "name": name,
        "created_at": created_at, "email_hash": email_hash,
    }


def get_stats() -> Dict:
    driver = get_neo4j()
    with driver.session(database=config.NEO4J_DATABASE) as s:
        pages = s.run("MATCH (p:Page) RETURN count(p) AS n").single()["n"]
        comments = s.run("MATCH (c:Comment) RETURN count(c) AS n").single()["n"]
        commenters = s.run("MATCH (u:Commenter) RETURN count(u) AS n").single()["n"]
    return {"pages": pages, "comments": comments, "commenters": commenters}


class CommentCreate(BaseModel):
    page_id: str = Field(..., max_length=200)
    page_title: str = Field("", max_length=300)
    name: str = Field(..., min_length=1, max_length=80)
    text: str = Field(..., min_length=1, max_length=2000)
    email: str = Field("", max_length=200)
    parent_id: Optional[str] = None


def register(app: FastAPI, deps, cfg: dict) -> None:
    # Best-effort schema init when the module loads
    try:
        init_comment_schema()
    except Exception as exc:
        print(f"[warn] Neo4j comment schema init failed: {exc}")

    @app.get("/api/comments")
    async def comments_list(page_id: str, _: None = Depends(deps.require_api_key)):
        try:
            return {"comments": list_comments(page_id)}
        except Exception as exc:
            raise HTTPException(status_code=503, detail=f"Comment storage unavailable: {exc}")

    @app.post("/api/comments")
    async def comments_create(
        req: CommentCreate,
        _: None = Depends(deps.require_api_key),
        __: None = Depends(deps.check_rate_limit),
    ):
        try:
            return add_comment(
                page_id=req.page_id,
                page_title=req.page_title,
                name=req.name,
                text=req.text,
                email=req.email,
                parent_id=req.parent_id,
            )
        except Exception as exc:
            raise HTTPException(status_code=503, detail=f"Comment storage unavailable: {exc}")

    @app.get("/api/comments/stats")
    async def comments_stats(_: None = Depends(deps.require_api_key)):
        try:
            return get_stats()
        except Exception as exc:
            raise HTTPException(status_code=503, detail=f"Comment storage unavailable: {exc}")
