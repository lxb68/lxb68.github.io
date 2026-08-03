---
title: "Multi-Objective Collision-Free AGV Scheduling"
order: 2
track: "scheduling"
featured: true
period: "Dates to be provided"
role: "Project Member"
visual: "agv"
icon: "🤖"
visual_label: "GA* · A* · CAT"
cover: "/images/project/collision-free-agv/warehouse-layout.png"
tech:
  - "Multi-objective Optimization"
  - "Improved Genetic Algorithm"
  - "A* Path Planning"
  - "Conflict Avoidance Table"
summary: "Developed an integrated multi-AGV scheduler for order and pallet assignment, route optimization, picking-station balancing, and collision-free execution in an automated warehouse."
---

## Project Overview

This project addressed coordinated multi-AGV scheduling in an automated warehouse. The system jointly handles order assignment, pallet selection, picking-station matching, and outbound–return–recycling routes, while resolving node conflicts, opposite-direction conflicts, congestion, and storage-node deadlocks during concurrent operation.

The warehouse was modeled as a **32 × 22 bidirectional grid** with seven node types: travel, storage, reserved, obstacle, picking, replenishment, and empty-pallet recycling nodes. The experimental scenario contained **148 pallets, 36 storage groups, and 20 AGVs**. The objective was to shorten total travel and makespan, improve effective AGV utilization, and balance picking-station workloads without compromising order completeness or route safety.

<figure>
  <img src="/images/project/collision-free-agv/warehouse-layout.png" alt="Automated warehouse grid with storage, picking, reserved, and recycling nodes">
  <figcaption>Warehouse layout with wider inter-zone paths and reserved nodes that provide maneuvering space for concurrent AGV traffic.</figcaption>
</figure>

## Problem Formulation

The system was separated into three cohesive modules: order and pallet preprocessing, storage-resource pairing, and multi-AGV scheduling. They exchange only standardized order, pallet, node, and spatiotemporal trajectory data, allowing each optimization stage to be validated or replaced independently.

### Order and pallet preprocessing

Orders for the same SKU are first consolidated and then split according to pallet inventory so that each resulting sub-order can, whenever possible, be completed by a single outbound operation. Pallets are grouped to maximize within-group SKU similarity while balancing item quantities across groups. High-frequency pallet groups are then paired with shorter storage-to-picking routes.

<figure class="project-flow-figure">
  <img src="/images/project/collision-free-agv/order-splitting.png" alt="Example of splitting a consolidated order according to inventory on two pallets">
  <figcaption>A 36-unit SKU demand is split into sub-orders of 9 and 27 units, matching the available quantities on two pallets.</figcaption>
</figure>

### Multi-objective scheduling model

The scheduling model combines three objectives:

- **Minimize total travel:** Manhattan distance guides A* search for outbound, return, and recycling routes.
- **Maximize AGV time efficiency:** reduce picking-station queues and avoidance waits so more time is spent on productive transport.
- **Balance picking-station workload:** distribute tasks across stations to limit local congestion and conflict risk.

Feasibility is enforced through order-demand, SKU-category, inventory-quantity, unique pallet-state, and return-location constraints. Optimization is split into task assignment and path planning, keeping assignment logic independent from conflict resolution.

## Algorithm and Collision Avoidance

An improved genetic algorithm searches global task plans, while A* generates point-to-point paths. Each chromosome segment stores an AGV's assigned order and actual route. Sequential crossover exchanges complete AGV task segments, preserving the relationship between assignments and their paths.

The decoder selects target pallets, builds an AGV recommendation queue, chooses a picking station, and generates outbound and return-or-recycling routes. A candidate trajectory is committed only after conflict checks pass.

<figure class="project-flow-figure">
  <img src="/images/project/collision-free-agv/algorithm-flow.png" alt="Improved genetic algorithm flow from order decoding to outbound and return route generation">
  <figcaption>Genetic search determines the global task order; the constraint-aware decoder turns each chromosome into executable AGV assignments and routes.</figcaption>
</figure>

### Spatiotemporal conflict detection

A Conflict Avoidance Table (CAT) stores every planned `(x, y, t)` state and supports node-occupancy queries at any time. It detects:

- multiple AGVs occupying the same node at the same time;
- two AGVs entering the same edge in opposite directions;
- storage-node and entrance blocking that can produce deadlock;
- routes whose surrounding time-window region is repeatedly traversed by other AGVs.

### Hierarchical avoidance policy

When a risk is detected, the planner tries reserved-node waiting, rollback waiting, an alternate path, a less congested path, and a peripheral inter-zone path. Reassigning the task to another AGV is the final fallback. This priority isolates local path repair from global task reassignment and limits the impact of a single conflict on the overall schedule.

<figure>
  <img src="/images/project/collision-free-agv/collision-avoidance.png" alt="One AGV moving to a reserved node to resolve an opposite-direction conflict">
  <figcaption>Reserved-node avoidance: AGV 16 temporarily leaves the shared route while AGV 13 completes its movement through the conflict area.</figcaption>
</figure>

## Experiments and Results

Experiments used data from Problem B of the 2022 MathorCup Mathematical Modeling Challenge. Separate comparisons quantified the impact of order preprocessing, warehouse layout, and collision-avoidance logic.

| Experiment | Baseline | Optimized design | Main result |
| :--- | :--- | :--- | :--- |
| Order processing | Original orders | Consolidate, then split by pallet inventory | **55.86%** less travel and **72.97%** less waiting |
| Warehouse layout | Dense storage and narrow paths | Four zones, wider paths, and reserved nodes | In large-scale tests: **40.76%** less travel, **44.61%** less waiting, and **44.31%** fewer collision points |
| Avoidance algorithm | Conventional PSO and GA | Improved GA (GA*) | **Zero collision points** with 10, 15, and 20 AGVs while completing all tasks |

With 20 AGVs, conventional GA and PSO averaged 180.0 and 206.1 collision points, respectively, while GA* reduced collisions to zero. GA* accepted additional travel and waiting to guarantee safe paths, making the efficiency–safety trade-off explicit rather than hiding it inside a single score.

<figure>
  <img src="/images/project/collision-free-agv/algorithm-comparison.png" alt="Average transport distance of GA, PSO, and improved GA across different AGV fleet sizes">
  <figcaption>Average distance falls as fleet size increases; GA* incurs controlled detours in exchange for collision-free operation.</figcaption>
</figure>

## Outcomes

- Built an end-to-end pipeline from order splitting and pallet grouping to storage–station pairing and multi-AGV scheduling.
- Designed a CAT-based spatiotemporal occupancy model and six-level policy for conflicts, congestion, and deadlocks.
- Planned collision-free routes for 20 AGVs completing all tasks on the 32 × 22 grid.
- Quantified the independent and combined contribution of order, layout, and algorithm improvements through controlled comparisons.
