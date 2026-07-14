---
title: "Qi Sun"
date: 2022-10-24
type: landing

design:
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      username: admin
      text: ""
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  - block: markdown
    content:
      title: 'Research Highlights'
      subtitle: ''
      text: |-
        - **Knowledge-augmented RCA**: Combining safety knowledge graphs with LLMs for industrial root-cause analysis ([CCC 2024](/publication/ccc-2024/)).
        - **Multivariate time series**: Spatial-temporal dependency modeling for anomaly detection in process industries ([ICIC 2024](/publication/icic-2024-mtsad/)).
        - **Manufacturing NLP**: Anchor-span named entity recognition for knowledge extraction ([EAAI 2025](/publication/eai-2025-ner/)).
        - **CPS safety**: Formal and data-driven verification for ADAS and process cyber-physical systems ([RESS](/publication/ress-2026-adas/), [IEEE SMC](/publication/smc-2024-adas/)).
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    content:
      title: Recent Publications
      text: "[View all publications →](/publication/)"
      filters:
        folders:
          - publication
        exclude_featured: true
      count: 8
    design:
      view: citation
---
