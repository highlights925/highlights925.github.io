---
title: "Enhancing DeepLabv3+ With Multiscale Sparse-Aware Dilated Convolution and Boundary-Interactive ASPP for River Ice Segmentation"
authors:
  - Dingju Zhou
  - Kaijun Wu
  - Junmei Hu
  - admin
date: "2026-01-01T00:00:00Z"
doi: "10.1109/LGRS.2026.3667024"
publishDate: "2026-01-01T00:00:00Z"
publication_types: ["article-journal"]
publication: In *IEEE Geoscience and Remote Sensing Letters*
publication_short: In *IEEE GRSL*
abstract: "Accurate segmentation of river ice in remote sensing imagery remains challenging due to heterogeneous ice textures, fragmented floes, and ambiguous ice–water boundaries. While DeepLabv3+ effectively captures multi-scale context, its standard atrous convolution suffers from uniform sampling and gridding effects, which limit boundary discrimination in complex river ice scenes. To address these issues, we propose a lightweight enhancement to DeepLabv3+ that integrates regionally weighted dilated convolution, a coordinated dilation configuration strategy, and a boundary-aware refinement branch. The proposed design improves central feature aggregation while preserving global context, without introducing additional computational overhead. Experiments on the NWPU_YRCC2 dataset demonstrate a 1.95% mIoU improvement over the baseline DeepLabv3+, validating the effectiveness of the proposed framework for precise and efficient river ice segmentation."
summary: "A lightweight DeepLabv3+ enhancement for river ice segmentation in remote sensing imagery."
tags:
  - Remote Sensing
  - Semantic Segmentation
  - DeepLab
featured: false
url_pdf: "https://doi.org/10.1109/LGRS.2026.3667024"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://doi.org/10.1109/LGRS.2026.3667024"
url_video: ""
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

River-ice imagery contains fragmented floes, varied textures, and indistinct ice–water edges. Standard atrous convolution in DeepLabv3+ samples features uniformly, which can cause gridding artifacts and weak boundary detail. This paper adapts the segmentation network to those image structures.

## Method

The model combines multiscale sparse-aware dilated convolution with a coordinated dilation configuration and a boundary-interactive ASPP refinement branch. The design aims to aggregate central-region features and preserve broader context while improving the representation of ice boundaries.

## Evidence

On the NWPU_YRCC2 dataset, the paper reports a 1.95 percentage-point mIoU improvement over baseline DeepLabv3+, with no additional computational overhead. This is the reported dataset result; performance on other imagery remains a separate validation question. Qi Sun is fourth author.

## Paper

- [IEEE Geoscience and Remote Sensing Letters record](https://doi.org/10.1109/LGRS.2026.3667024) · [DOI](https://doi.org/10.1109/LGRS.2026.3667024)


{{< paper-chat >}}

{{< comments >}}
