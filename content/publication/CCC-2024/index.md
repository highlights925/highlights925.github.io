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
url_source: "https://doi.org/10.23919/CCC63176.2024.10662704"
url_video: ""
image:
  filename: featured.jpg
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

Industrial alarm floods can obscure the initiating event: many alarms arrive together, while their relationships depend on the process structure and operating history. This paper asks whether a language model can explain a likely root cause when it is given relevant, traceable process knowledge rather than alarm text alone.

## Method

The workflow builds a process-safety knowledge graph from catalytic-cracking operation manuals and historical anomaly information. Named entities extracted from alarm messages become retrieval keys; the retrieved graph facts are then supplied to a large language model as contextual evidence for root-cause inference. The graph supplies domain facts, while the language model turns those facts and alarm observations into an explanation.

## Evidence and contribution

The conference paper reports experiments in which the method identifies root causes accurately. The published abstract does not give a numeric accuracy or a comparison table, so this page does not attach a score to that claim. Qi Sun is the first author.

## Paper

- [IEEE Xplore record and abstract](https://ieeexplore.ieee.org/abstract/document/10662704) · [DOI](https://doi.org/10.23919/CCC63176.2024.10662704)
- The conference PDF is available with this page.


{{< paper-chat >}}

{{< comments >}}
