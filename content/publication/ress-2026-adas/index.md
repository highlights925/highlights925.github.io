---
title: "Enhanced Verification of Safety and Security for Advanced Driver Assistance Systems"
authors:
  - Lu Liu
  - admin
  - Liren Yang
  - Yu-Chu Tian
  - Chunjie Zhou
date: "2026-02-01T00:00:00Z"
doi: "10.1016/j.ress.2025.111691"
publishDate: "2026-02-01T00:00:00Z"
publication_types: ["article-journal"]
publication: In *Reliability Engineering & System Safety*
publication_short: In *RESS*
abstract: "This paper combines reachability-based formal verification with DRL-guided falsification for ADAS under cyberattacks. A hybrid automaton models vehicle and controller behavior, while attacks are bounded disturbances. When conservative verification is inconclusive, reachability results guide a DRL search for concrete unsafe attack paths, demonstrated with Flow* and CARLA/Scenic."
summary: "A verification framework for ADAS safety and security, published in RESS 2026."
tags:
  - ADAS
  - Safety Verification
  - Cyber-Physical Systems
featured: true
url_pdf: "https://doi.org/10.1016/j.ress.2025.111691"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://doi.org/10.1016/j.ress.2025.111691"
url_video: ""
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
projects: []
slides: ""
---

## Study focus

Reachability-based formal verification can become inconclusive when cyberattacks are represented conservatively as bounded disturbances. Falsification can find concrete unsafe examples, but an unguided search may be expensive and does not itself prove safety. This paper makes verification and falsification guide one another.

## Method

A hybrid automaton models vehicle dynamics and ADAS control modes; attack effects are over-approximated as bounded inputs during reachability analysis. When the reachable-set result is inconclusive, a deep-reinforcement-learning (DRL) falsifier searches for attack paths that violate the safety specification. Verification geometry and outcomes shape the DRL reward and help focus the search.

## Evaluation and contribution

The framework is demonstrated with Flow* reachability and high-fidelity CARLA/Scenic simulations. It targets concrete counterexample discovery in cases where over-approximation blocks a decisive verification result. Qi Sun is second author; the article lists his contribution as data curation.

## Paper

- [Reliability Engineering & System Safety article](https://www.sciencedirect.com/science/article/pii/S0951832025008919) · [DOI](https://doi.org/10.1016/j.ress.2025.111691)


{{< paper-chat >}}

{{< comments >}}
