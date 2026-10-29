---
title: "OregairuChar: A Benchmark Dataset for Character Appearance Frequency Analysis in My Teen Romantic Comedy SNAFU"
authors:
  - admin
  - Dongqing Zhou
  - Lin Zhang
date: "2025-11-07T00:00:00Z"
doi: "10.48550/arXiv.2511.05263"
publishDate: "2025-11-07T00:00:00Z"
publication_types: ["article"]
publication: "*arXiv preprint*"
publication_short: In *arXiv*
abstract: "The analysis of character appearance frequency is essential for understanding narrative structure, character prominence, and story progression in anime. In this work, we introduce OregairuChar, a benchmark dataset designed for appearance frequency analysis in the anime series My Teen Romantic Comedy SNAFU. The dataset comprises 1600 manually selected frames from the third season, annotated with 2860 bounding boxes across 11 main characters. OregairuChar captures diverse visual challenges, including occlusion, pose variation, and inter-character similarity, providing a realistic basis for appearance-based studies. To enable quantitative research, we benchmark several object detection models on the dataset and leverage their predictions for fine-grained, episode-level analysis of character presence over time. This approach reveals patterns of character prominence and their evolution within the narrative. By emphasizing appearance frequency, OregairuChar serves as a valuable resource for exploring computational narrative dynamics and character-centric storytelling in stylized media."
summary: "A first-author benchmark dataset for anime character appearance frequency analysis, with detection baselines and narrative analysis."
tags:
  - Computer Vision
  - Benchmark Dataset
  - Anime
featured: false
url_pdf: "https://arxiv.org/pdf/2511.05263"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://arxiv.org/abs/2511.05263"
url_video: ""
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

Character screen time is a measurable signal of narrative prominence, but anime footage presents detection challenges such as occlusion, changing poses, and visually similar characters. OregairuChar provides a manually annotated benchmark for studying appearance frequency in *My Teen Romantic Comedy SNAFU*.

## Dataset and method

The release contains 1,600 manually selected frames from season 3, with 2,860 bounding boxes covering 11 main characters. The authors benchmark multiple object detectors, then aggregate their predictions by episode to examine how character presence changes over the series. The annotations support both detector evaluation and downstream character-frequency analysis.

## Evidence and contribution

The paper positions the dataset as a starting point for computational narrative analysis in stylized media. The reported analysis is based on model predictions over episodes; it is not a claim that screen time alone captures a character’s narrative importance. Qi Sun is the first author.

## Paper and data

- [arXiv preprint and abstract](https://arxiv.org/abs/2511.05263) · [PDF](https://arxiv.org/pdf/2511.05263) · [DOI](https://doi.org/10.48550/arXiv.2511.05263)


{{< paper-chat >}}

{{< comments >}}
