---
title: "Interpretable Vehicular Safety Control Based on Hybrid Automata and Deep Reinforcement Learning"
authors:
  - Lu Liu
  - admin
  - Liren Yang
  - Chunjie Zhou
date: "2024-11-01T00:00:00Z"
doi: "10.1109/CAC63892.2024.10865523"
publishDate: "2024-11-01T00:00:00Z"
publication_types: ["paper-conference"]
publication: In *2024 China Automation Congress (CAC)*
publication_short: In *CAC*
abstract: "Advanced driver assistance system (ADAS) is an emerging technology in autonomous vehicles. It involves discrete function switches with continuous dynamics, thus sudden changes of different control strategies may lead vehicles to lose stability and safety. While existing analysis mainly focuses on individual functions, and ignores the continuity of control variables when switching between various functions. Meanwhile, interpretable control procedures with safety guarantees are often absent due to the complex vehicular systems. Therefore, verifying ADAS functions with safety guarantees and interpretability is essential, especially for adaptive cruise control which is a main function of ADAS. This paper proposes an approach for safety control based on hybrid automata and deep reinforcement learning. First, hybrid automata are built to describe ADAS functions, and then a deep reinforcement learning model is employed to optimize the strategies for adaptive cruise control. Finally, numerical experiments demonstrate that the proposed approach effectively manipulates vehicle maneuvers across four different scenarios, including acceleration, deceleration, emergency braking and vehicle cut-in. Furthermore, this approach shows strong interpretability, high efficiency, and low resource cost, with an inference requiring 1.08 ms and 456.89 MB of memory on the CPU."
summary: "Interpretable ADAS safety control combining hybrid automata and deep reinforcement learning."
tags:
  - ADAS
  - Reinforcement Learning
  - Hybrid Automata
featured: false
url_pdf: "https://doi.org/10.1109/CAC63892.2024.10865523"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://doi.org/10.1109/CAC63892.2024.10865523"
url_video: ""
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

ADAS functions switch between discrete operating modes while vehicle motion evolves continuously. A controller that behaves well within one mode can still create abrupt or unsafe behavior during transitions. This paper studies interpretable safety control for adaptive cruise control (ACC) using a hybrid-system representation.

## Method

Hybrid automata describe the ADAS functions and their mode transitions. Deep reinforcement learning (DRL) optimizes ACC control strategies inside that representation, making the operating mode and maneuver part of the control explanation.

## Evaluation

Numerical experiments cover acceleration, deceleration, emergency braking, and vehicle cut-in. The paper reports CPU inference of 1.08 ms and 456.89 MB memory use. These figures describe the authors’ reported setup and should not be read as hardware-independent guarantees. Qi Sun is second author.

## Paper

- [IEEE Xplore record](https://ieeexplore.ieee.org/document/10865523) · [DOI](https://doi.org/10.1109/CAC63892.2024.10865523)


{{< paper-chat >}}

{{< comments >}}
