---
title: "Spatial-Temporal Dependency Based Automatic Failure Mode Classification for Industrial Processes"
authors:
  - Runlong Wang
  - admin
  - Yanjun Liu
  - Peihang Xu
  - Chunjie Zhou
date: "2024-11-01T00:00:00Z"
doi: "10.1109/CAC63892.2024.10864828"
publishDate: "2024-11-01T00:00:00Z"
publication_types: ["paper-conference"]
publication: In *2024 China Automation Congress (CAC)*
publication_short: In *CAC*
abstract: "With the rapid development of network technology, cyber-physical systems in the chemical industry are facing increasingly severe cybersecurity threats. Cyber attacks can lead to the failure of critical protection layers within these systems, including the basic process control system (BPCS), alarm systems, and the safety instrumented system (SIS), thereby endangering the safety and stability of industrial processes. In order to accurately identify the system state, this study proposes a spatial-temporal dependency based multivariate time series classification method for industrial processes. By preprocessing the process data from cyber-physical systems in the chemical industry and subsequently employing graph attention networks and diagonal state space models for feature extraction, we capture the spatial-temporal dependencies in the process data and obtain low-dimensional representations. This approach enables accurate monitoring of the states of industrial control systems and precise localization of failures. We validated the performance of the proposed method using the Tennessee Eastman Process (TEP) dataset and the Catalytic Cracking Process (CCP) dataset. Experimental results demonstrate that this method achieves high accuracy and reliability, providing strong support for enhancing the security of industrial control systems."
summary: "Spatial-temporal multivariate time series classification for industrial failure mode recognition."
tags:
  - Time Series
  - Cyber-Physical Systems
  - Failure Diagnosis
featured: false
url_pdf: "https://doi.org/10.1109/CAC63892.2024.10864828"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://doi.org/10.1109/CAC63892.2024.10864828"
url_video: ""
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

Chemical-process cyber-physical systems depend on several protection layers, including basic process control, alarms, and safety instrumented systems. The paper classifies system and failure states from process measurements, with the stated motivation of detecting failures that can threaten those layers.

## Method

The proposed classifier represents dependencies between process variables using graph attention networks, then models temporal patterns with diagonal state-space models. The resulting spatial-temporal representation is used to classify multivariate process states and support failure localization.

## Evaluation

Experiments use both the Tennessee Eastman Process (TEP) benchmark and a catalytic-cracking process (CCP) dataset. The paper reports high classification accuracy and reliability, but the public abstract does not provide numerical results; this page therefore avoids inventing a percentage. Qi Sun is second author.

## Paper

- [IEEE Xplore record](https://ieeexplore.ieee.org/document/10864828) · [DOI](https://doi.org/10.1109/CAC63892.2024.10864828)


{{< paper-chat >}}

{{< comments >}}
