---
title: "Safety Verification of Advanced Driver Assistance Systems Using Hybrid Automaton Reachability"
authors:
  - Lu Liu
  - admin
  - Liren Yang
  - Yahui Li
  - Chunjie Zhou
date: "2024-10-06T00:00:00Z"
doi: "10.1109/SMC54092.2024.10830931"
publishDate: "2024-10-06T00:00:00Z"
publication_types: ["paper-conference"]
publication: In *2024 IEEE International Conference on Systems, Man, and Cybernetics (SMC)*
publication_short: In *IEEE SMC*
abstract: "Advanced driver assistance system (ADAS) is effectively promoting the vehicular automation level and it is critical to ensure its functional safety. While existing analysis mainly focuses on individual applications of ADAS, safety violations in the overall system can be found by extensive road tests, which are not only costly in terms of time and money but also lack a formal safety guarantee. This is because tests may not cover all driving scenarios, especially the ones that involve discrete mode switching. In this paper, we focus on the longitudinal vehicle motion and provide a pipeline to perform safety verification for all the related ADAS applications. To that end, we specify safety constraints and boundaries for a vehicle's longitudinal cruising and collision avoidance and validate a longitudinal dynamic model against the high-fidelity simulation software CarSim. Then we define hybrid automata to describe the closed-loop system composed of the vehicle dynamics and the ADAS. Finally, by computing the reachable sets of the hybrid automata and comparing them with the specified safety boundaries, the ADAS is verified. Numerical experiments demonstrate the efficacy of the proposed approach."
summary: "Formal safety verification for ADAS via hybrid automaton reachability analysis."
tags:
  - ADAS
  - Formal Verification
  - Hybrid Automata
featured: false
url_pdf: "https://doi.org/10.1109/SMC54092.2024.10830931"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://doi.org/10.1109/SMC54092.2024.10830931"
url_video: ""
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

Road testing cannot cover every ADAS mode transition, and testing alone does not establish a formal safety guarantee. This paper develops a reachability-based verification pipeline for longitudinal vehicle behavior under cruising and collision-avoidance functions.

## Method

The authors specify safety constraints and boundaries, validate a longitudinal vehicle model against CarSim, and represent the closed-loop vehicle-plus-ADAS system as a hybrid automaton. They compute reachable sets from the model and compare those sets with the specified unsafe boundaries; safety follows when the reachable behavior stays outside those regions.

## Evidence and contribution

Numerical experiments demonstrate the verification pipeline for the modeled ADAS applications. Qi Sun is second author. The work is related to the later safety-security paper on this site, which adds bounded cyberattack modeling and guided falsification when reachability verification is inconclusive.

## Paper

- [IEEE SMC proceedings record](https://doi.org/10.1109/SMC54092.2024.10830931) · [DOI](https://doi.org/10.1109/SMC54092.2024.10830931)


{{< paper-chat >}}

{{< comments >}}
