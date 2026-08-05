"""Storage singletons: Neo4j driver + Redis client (lazy init)."""

from typing import Optional

import redis
from neo4j import GraphDatabase

from .config import (
    NEO4J_DATABASE, NEO4J_PASSWORD, NEO4J_URI, NEO4J_USER,
    REDIS_URL, COMMENT_CACHE_TTL,
)

_redis: Optional[redis.Redis] = None
_neo4j = None


def get_redis() -> redis.Redis:
    global _redis
    if _redis is None:
        _redis = redis.from_url(REDIS_URL, decode_responses=True)
    return _redis


def get_neo4j():
    global _neo4j
    if _neo4j is None:
        _neo4j = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    return _neo4j


def init_comment_schema() -> None:
    driver = get_neo4j()
    with driver.session(database=NEO4J_DATABASE) as s:
        s.run("CREATE CONSTRAINT IF NOT EXISTS FOR (p:Page) REQUIRE p.id IS UNIQUE")
        s.run("CREATE CONSTRAINT IF NOT EXISTS FOR (u:Commenter) REQUIRE u.email_hash IS UNIQUE")
        s.run("CREATE CONSTRAINT IF NOT EXISTS FOR (c:Comment) REQUIRE c.id IS UNIQUE")
