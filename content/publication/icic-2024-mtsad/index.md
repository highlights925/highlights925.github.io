---
title: "Spatial-Temporal Dependency Based Multivariate Time Series Anomaly Detection for Industrial Processes"
authors:
  - admin
  - Yahui Li
  - Zhenpeng Hu
  - Chunjie Zhou
  - Lu Liu
date: "2024-08-01T00:00:00Z"
doi: "10.1007/978-981-97-5618-6_18"
publishDate: "2024-08-01T00:00:00Z"
publication_types: ["chapter"]
publication: In *International Conference on Intelligent Computing (ICIC)*
publication_short: In *ICIC*
abstract: "A multi-task variational autoencoder combines graph attention networks for cross-variable structure and selective state-space models for temporal patterns. Across three datasets, including catalytic-cracking process data, it outperforms six baselines and produces anomaly scores and a causal variable graph to support interpretation."
summary: "First-author work on spatial-temporal multivariate time series anomaly detection for industrial processes."
tags:
  - Anomaly Detection
  - Time Series
  - Industrial Processes
featured: true
url_pdf: "https://doi.org/10.1007/978-981-97-5618-6_18"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://doi.org/10.1007/978-981-97-5618-6_18"
url_video: ""
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

Industrial sensors are noisy and interdependent: anomalies may appear as an unusual value, a broken relationship between variables, or a change in temporal behavior. This paper treats spatial and temporal dependency modeling as a joint anomaly-detection problem.

## Method

The proposed multi-task variational autoencoder learns a representation of multivariate time series. Graph attention networks capture relationships across process variables, while selective state-space models capture temporal dynamics. The multi-task objective is intended to learn robust representations in the presence of noise; anomaly scores and a causal graph provide interpretable signals for diagnosis.

## Evaluation

The model is compared with six baselines on three datasets, including catalytic-cracking process data. Reported F1 scores across the three datasets are 0.9389, 0.8151, and 0.9524. The anomaly scores and variable graph are presented as aids for operators to inspect and respond to detected events. Qi Sun is first author.

## Paper

- [Springer chapter](https://link.springer.com/chapter/10.1007/978-981-97-5618-6_18) · [DOI](https://doi.org/10.1007/978-981-97-5618-6_18)


{{< paper-chat >}}

{{< comments >}}
