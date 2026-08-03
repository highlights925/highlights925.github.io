---
title: "Root Cause Analysis for Industrial Process Anomalies through the Integration of Knowledge Graph and Large Language Model"
authors:
  - admin
  - Yahui Li
  - Chunjie Zhou
  - Yu-Chu Tian
date: "2024-07-28T00:00:00Z"
doi: "10.23919/CCC63176.2024.10662704"
publishDate: "2024-07-28T00:00:00Z"
publication_types: ["paper-conference"]
publication: In *2024 43rd Chinese Control Conference (CCC)*
publication_short: In *CCC*
abstract: "Root cause analysis for industrial process anomalies is critical for manufacturing activities. Industrial process alarms can provide crucial information to enable root cause analysis. However, the complex system structure causes a large number of alarms to emerge at the same time. To address this issue, we proposed an approach that utilizes knowledge graphs and large language models to provide comprehensible root cause analysis. Firstly, we extract knowledge such as historical anomalies from catalytic cracking operation manuals to construct an industrial process safety knowledge graph. Then, named entities in each alarm are extracted as keywords to retrieve factual knowledge from the knowledge graph. Finally, factual knowledge will be provided to the large language model as prior knowledge to infer the root cause of anomalies. Experimental results show that the proposed approach can accurately identify the root cause, thereby ensuring the safety of industrial processes."
summary: "Combining knowledge graphs and large language models for interpretable root cause analysis of industrial process anomalies."
tags:
  - Large Language Models
  - Knowledge Graph
  - Process Safety
  - Root Cause Analysis
featured: true
url_pdf: "conference-paper.pdf"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""
image:
  filename: featured.jpg
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Overview

The pipeline couples structured safety knowledge with large language models. Alarm entities act as retrieval keys; the LLM then reasons over graph facts rather than raw alarms alone, improving comprehensibility under alarm floods.

**Role:** First author · **Theme:** Knowledge Graphs & LLMs · **Citations (OpenAlex):** 7

## Highlights

- Build an industrial process safety knowledge graph from catalytic cracking manuals and historical anomalies.
- Use NER over alarm text to retrieve factual context from the knowledge graph.
- Feed retrieved facts to an LLM as prior knowledge for interpretable root-cause analysis.

## Key Results

Experiments show the approach can accurately identify root causes in industrial anomaly scenarios, supporting safer process operations.

## Links

- DOI: [10.23919/CCC63176.2024.10662704](https://doi.org/10.23919/CCC63176.2024.10662704)
- Google Scholar profile: [Qi Sun](https://scholar.google.com/citations?user=F_aQcNMAAAAJ)

