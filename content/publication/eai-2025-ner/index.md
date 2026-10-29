---
title: "Named Entity Recognition Based on Anchor Span for Manufacturing Knowledge Extraction"
authors:
  - Yahui Li
  - admin
  - Chunjie Zhou
  - Lu Liu
  - Yu-Chu Tian
date: "2025-12-01T00:00:00Z"
doi: "10.1016/j.engappai.2025.112693"
publishDate: "2025-12-01T00:00:00Z"
publication_types: ["article-journal"]
publication: In *Engineering Applications of Artificial Intelligence*
publication_short: In *EAAI*
abstract: "Manufacturing text often contains nested entities packed into short, information-dense passages. The anchor-span NER (ASNER) model combines token and span classification: a boundary-matching network proposes candidate spans, then biaffine attention and convolutional context features classify them. The authors evaluate it on public NER datasets and a Chinese catalytic-cracking manual corpus."
summary: "An anchor-span NER method for extracting manufacturing knowledge from domain text, published in EAAI 2025."
tags:
  - Named Entity Recognition
  - Knowledge Extraction
  - Manufacturing
featured: true
url_pdf: "https://doi.org/10.1016/j.engappai.2025.112693"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://doi.org/10.1016/j.engappai.2025.112693"
url_video: ""
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

Manufacturing manuals often pack domain-specific facts into short sentences and contain nested entities: one phrase may itself include another meaningful entity. Flat sequence tagging can miss these nested spans or choose incorrect boundaries, which then damages downstream knowledge extraction.

## Method

The anchor-span NER (ASNER) model combines token and span classification. A boundary-match network uses entity head and tail features to propose candidate anchor spans; biaffine attention and convolutional layers encode token context, after which the filtered candidates are classified. The authors also construct a Chinese nested NER dataset from catalytic-cracking operation manuals.

## Evaluation and contribution

The published article evaluates ASNER on six public flat and nested NER datasets plus a real refining-manual corpus. The abstract and article record report effectiveness but do not expose a single headline score in the accessible summary. Qi Sun is second author; the article’s contribution statement lists his work as validation and data curation.

## Paper

- [Engineering Applications of Artificial Intelligence article](https://www.sciencedirect.com/science/article/pii/S0952197625027241) · [DOI](https://doi.org/10.1016/j.engappai.2025.112693)


{{< paper-chat >}}

{{< comments >}}
