---
title: "Capacity Estimation of Lithium-ion Battery with Multi-task Autoencoder and Empirical Mode Decomposition"
authors:
  - admin
  - Fangshu Cui
  - Mingrui Shi
author_notes:
#  - "Equal contribution"
#  - "Equal contribution"
date: "2024-06-22T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-06-22T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Measurement"
publication_short: ""

abstract: Capacity estimation of lithium-ion batteries is a commonly used method in health diagnosis and management. Its mainstream method involves using data-driven time series forecasting models to learn the patterns of changes in capacity. However, capacity regeneration poses a challenge for training time series forecasting models. Therefore, we propose a hybrid method that applies empirical mode decomposition and a multi-task autoencoder. In detail, empirical mode decomposition is applied to decompose the time series of capacity into intrinsic mode functions and a residual. Then, a multi-task autoencoder based on diagonal state space models is applied to estimate intrinsic mode functions while support vector regression is utilized for the residual. Experimental results show that the method outperforms seven baselines on three datasets, with an average root mean square error of 0.0103, 0.0111, and 0.0004. Furthermore, it is capable of performing an inference on the CPU in 3.57 ms with 0.69 MB of memory usage.

# Summary. An optional shortened abstract.
summary: We propose a hybrid method combining empirical mode decomposition and a multi-task autoencoder for lithium-ion battery capacity estimation, addressing capacity regeneration challenges. Experiments on three datasets show superior accuracy and efficiency, achieving low error rates and fast CPU inference with minimal memory usage.

tags:
- Source Themes
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: http://arxiv.org/pdf/1512.04133v1
url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

{{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/).
