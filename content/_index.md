---
title: "Qi Sun"
date: 2022-10-24
type: landing

design:
  spacing: "4rem"

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
        color: "#04140f"
        image:
          filename: stacked-peaks.svg
          filters:
            brightness: 0.85
          size: cover
          position: center
          parallax: false
  - block: markdown
    content:
      title: Research Focus
      subtitle: Industrial AI for safety-critical systems
      text: |-
        I build methods that turn **process signals**, **alarms**, and **domain documents** into explainable decisions for plants and vehicles.

        {{< research-themes >}}

        {{< research-match >}}
    design:
      columns: '1'
  - block: collection
    content:
      title: Research Projects
      text: "[All research themes →](/projects/)"
      filters:
        folders:
          - project
      count: 3
    design:
      view: article-grid
      fill_image: true
      columns: 3
  - block: collection
    id: papers
    content:
      title: Featured Publications
      text: "[View all publications →](/publication/)"
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 2
      fill_image: true
  - block: collection
    content:
      title: Recent Publications
      text: ""
      filters:
        folders:
          - publication
        exclude_featured: true
      count: 6
    design:
      view: citation
  - block: collection
    id: news
    content:
      title: News
      page_type: post
      count: 5
      order: desc
    design:
      view: date-title-summary
---
