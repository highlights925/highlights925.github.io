---
title: Safety Knowledge Graph & LLM Root-Cause Analysis
summary: Constructing industrial safety knowledge graphs and combining them with LLMs for interpretable root-cause analysis under alarm floods.
tags:
  - Knowledge Graph
  - Large Language Models
  - Process Safety
date: "2024-07-28T00:00:00Z"
authors:
  - admin
external_link: ""
url_code: ""
url_pdf: ""
image:
  filename: featured.png
  focal_point: Smart
projects: []
---

## Motivation

Industrial plants often emit large volumes of alarms during abnormal conditions. Operators need **comprehensible root causes**, not only anomaly scores.

## Approach

1. Extract safety knowledge from manuals and historical anomalies into a **process safety knowledge graph**.
2. Apply **NER** on alarm text to retrieve relevant graph facts.
3. Provide retrieved facts to an **LLM** as prior knowledge for RCA.

## Outcomes

- First-author paper at **CCC 2024** on KG + LLM root-cause analysis.
- Related manufacturing NER work in **EAAI 2025**.
- Closely aligned with the MEng thesis on FCC reaction–regeneration safety knowledge graphs.
