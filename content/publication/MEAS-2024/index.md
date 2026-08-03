---
title: "Capacity Estimation of Lithium-ion Battery with Multi-task Autoencoder and Empirical Mode Decomposition"
authors:
  - admin
  - Fangshu Cui
  - Mingrui Shi
date: "2024-08-01T00:00:00Z"
doi: "10.1016/j.measurement.2024.115146"
publishDate: "2024-06-22T00:00:00Z"
publication_types: ["article-journal"]
publication: In *Measurement*
publication_short: In *Measurement*
abstract: "Capacity estimation of lithium-ion batteries is a commonly used method in health diagnosis and management. Its mainstream method involves using data-driven time series forecasting models to learn the patterns of changes in capacity. However, capacity regeneration poses a challenge for training time series forecasting models. Therefore, we propose a hybrid method that applies empirical mode decomposition and a multi-task autoencoder. In detail, empirical mode decomposition is applied to decompose the time series of capacity into intrinsic mode functions and a residual. Then, a multi-task autoencoder based on diagonal state space models is applied to estimate intrinsic mode functions while support vector regression is utilized for the residual. Experimental results show that the method outperforms seven baselines on three datasets, with an average root mean square error of 0.0103, 0.0111, and 0.0004. Furthermore, it is capable of performing an inference on the CPU in 3.57 ms with 0.69 MB of memory usage."
summary: "A hybrid EMD and multi-task autoencoder method for lithium-ion battery capacity estimation, with strong accuracy and efficient CPU inference."
tags:
  - Battery Health
  - Time Series
  - State Space Models
featured: false
url_pdf: "https://doi.org/10.1016/j.measurement.2024.115146"
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

EMD decomposes capacity series into IMFs and a residual. A multi-task diagonal-state-space autoencoder estimates IMFs; SVR models the residual.

**Role:** First author · **Theme:** Battery Health Estimation · **Citations (OpenAlex):** 10

## Highlights

- Handle capacity regeneration via empirical mode decomposition (EMD).
- Estimate IMFs with a multi-task autoencoder based on diagonal state space models.
- Achieve low RMSE and millisecond-level CPU inference with small memory footprint.

## Key Results

Outperforms seven baselines on three datasets (avg. RMSE 0.0103 / 0.0111 / 0.0004); inference in 3.57 ms with 0.69 MB on CPU.

## Links

- DOI: [10.1016/j.measurement.2024.115146](https://doi.org/10.1016/j.measurement.2024.115146)
- Google Scholar profile: [Qi Sun](https://scholar.google.com/citations?user=F_aQcNMAAAAJ)

