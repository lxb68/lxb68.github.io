---
title: "Wave-Energy Power Optimization with Improved Simulated Annealing"
order: 6
track: "modeling"
featured: false
period: "2022"
role: "CUMCM Team Lead | National Second Prize"
status: "complete"
visual: "simulation"
icon: "∿"
visual_label: "Dynamics · SA"
cover: "/images/project/dynamic-system-simulation/cover.svg"
tech:
  - "Dynamic Modeling"
  - "Finite Difference Method"
  - "Improved Simulated Annealing"
  - "MATLAB"
summary: "Modeled the coupled heave and pitch dynamics of a wave-energy converter, simulated its time-domain response, and optimized PTO damping parameters with improved simulated annealing."
---

## Project Overview

This project was developed for the 2022 China Undergraduate Mathematical Contest in Modeling. It studied a wave-energy converter consisting of a float, an internal oscillator, a central shaft, and a power take-off system with springs and dampers. The work connected force and torque analysis, dynamic equations, numerical simulation, and parameter optimization to determine how damping settings affect average output power.

As team lead, I organized the workflow into four stages: mechanical analysis, dynamic modeling, finite-difference simulation, and parameter search. The project received a **National Second Prize**.

## Method

The model first described vertical heave and then extended the state space to coupled heave and pitch. It accounted for gravity, wave excitation, hydrostatic restoring forces, radiation damping, springs, and both linear and rotational PTO damping. The continuous equations were discretized with a **0.001 s** time step to simulate displacement, velocity, angular displacement, angular velocity, and instantaneous power.

Because the average-power objective had no convenient analytical form, the project used an improved simulated-annealing search based on the Metropolis criterion. Candidate generation was adjusted to explore a wider damping-parameter range and reduce the risk of becoming trapped in a small local neighborhood.

## Key Results

| Scenario | Best average output power |
| --- | ---: |
| Heave only, constant linear damping | **240.3179 W** |
| Heave only, nonlinear linear damping | **240.6511 W** |
| Coupled heave and pitch with joint damping optimization | **325.1951 W** |

## Personal Contributions

- Led problem decomposition, modeling decisions, team coordination, and report organization.
- Contributed to the force and torque analysis and converted the physical system into a discrete dynamic model.
- Implemented time-domain simulation and parameter search in MATLAB.
- Designed the improved candidate-generation strategy and compared damping configurations across motion scenarios.
