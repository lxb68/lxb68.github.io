---
title: "P³RF: Packed Privacy-Preserving Random-Forest Inference"
order: 4
track: "privacy"
featured: true
period: "2026"
role: "First Author"
status: "complete"
visual: "privacy"
icon: "🔐"
visual_label: "CKKS · Random Forest"
cover: "/images/project/privacy-preserving-random-forest/protocol-overview.png"
tech:
  - "Fully Homomorphic Encryption"
  - "Random Forest"
  - "CKKS / SIMD"
  - "OpenFHE"
summary: "Proposed P³RF, a non-interactive encrypted random-forest inference framework that removes the forest-voting bottleneck through a low-degree path-indicator polynomial and packed group aggregation, achieving up to 70.7× end-to-end speedup with provable correctness and privacy."
---

## Overview

Random forests improve generalization by aggregating many decision trees, but homomorphic encryption turns this aggregation into a major bottleneck. Each encrypted tree produces leaf-path scores; the server can neither identify the valid leaf nor directly perform discrete majority voting. Prior approaches require client interaction for intermediate conversion or arrange every tree as a complete binary tree, causing extra round trips, wasted SIMD slots, and multiplicative depth that grows rapidly with the model.

This project introduces **P³RF (Packed Privacy-Preserving Random Forest)**. The client uploads an encrypted feature vector once. The model owner performs node comparison, path evaluation, class alignment, and forest aggregation entirely over CKKS ciphertexts, then returns a small set of grouped vote ciphertexts. After decryption and rounding, the client recovers exact class counts without exposing the input or prediction to the server.

<figure class="project-flow-figure">
  <img src="/images/project/privacy-preserving-random-forest/protocol-overview.png" alt="P³RF pipeline from client-side feature packing to server-side node comparison, path evaluation, slot alignment, and forest aggregation" loading="eager">
  <figcaption>P³RF pipeline: the client packs and encrypts features for batched comparison; the server evaluates all tree paths and converts them into grouped class-vote ciphertexts through slot alignment and polynomial evaluation.</figcaption>
</figure>

## Diagnosing the Aggregation Bottleneck

After `SumPath`, a tree assigns score 0 to its valid leaf and an integer from 1 to depth D to every invalid leaf. The central challenge is therefore not merely encrypted node comparison, but converting a large collection of discrete path scores into class votes without revealing which leaves are active.

The system is separated into three cohesive modules. `TECMP` handles encrypted node comparisons, `SumPath` produces bounded leaf-path scores, and the new **PPI + PGA** layer converts those scores into forest votes. Their interfaces are limited to a fixed ciphertext-slot layout and bounded integer scores, so the comparison protocol, polynomial configuration, and forest partitioning strategy can evolve independently.

The design targets four constraints:

- **Non-interactivity:** no client-assisted Boolean-to-arithmetic conversion or intermediate decryption;
- **Bounded depth:** aggregation depth does not grow linearly with tree depth D;
- **Recoverable votes:** accumulated approximation and CKKS errors remain within the rounding radius;
- **Scalable packing:** irregular trees consume slots for actual nodes and leaves rather than a full binary-tree layout.

## Low-Degree Path-Indicator Polynomial

The ideal indicator maps score 0 to a scaling constant N and every nonzero score to 0, but CKKS cannot evaluate this discrete function directly. P³RF constructs a low-degree polynomial PPI(x) with `PPI(0) = N` while bounding the largest response on all nonzero points of the discrete path-score domain by ε.

A linear program jointly chooses the coefficients, N, and ε. For a group of g trees, at most Mmax leaves per class, and empirical CKKS error bound δ, the constraint

`N ≥ 2 · g · Mmax · (ε + δ)`

keeps the accumulated class error within N/2. Dividing the decrypted value by N and rounding therefore recovers the exact per-group vote count. The PIPS parameter-selection algorithm searches candidate degrees and scaled domains for the lowest-degree feasible polynomial, then derives a safe group size from the remaining error budget.

<figure>
  <img src="/images/project/privacy-preserving-random-forest/polynomial-parameters.png" alt="Selected path-indicator polynomial degree and minimum-to-maximum approximation error across tree depths" loading="lazy">
  <figcaption>PIPS parameter selection: as the path-score domain expands with tree depth, the selected degree increases adaptively while the worst nonzero-path response remains around or below 10⁻⁵.</figcaption>
</figure>

The work also proves existence and degree bounds for feasible polynomials. The minimum required degree is at most D, while a shifted Chebyshev construction yields a tighter logarithmic upper bound. This turns polynomial selection from an empirical tuning step into a configuration process with explicit correctness conditions.

## Packed Group Aggregation

PGA (Packed Group Aggregation) uses CKKS SIMD slots to combine paths from many trees and classes into a small number of ciphertexts:

1. **Slot alignment:** rotate each leaf score into a shared “class × within-class leaf offset” layout;
2. **Polynomial evaluation:** evaluate PPI in parallel so the valid leaf approaches N and invalid leaves approach 0;
3. **Class reduction:** apply plaintext masks and rotations to reduce all leaves of the same class into fixed class slots;
4. **Group accumulation:** sum trees within the safe error-budget group size, producing K grouped vote ciphertexts.

The layout operates on actual leaves and does not require padding each tree into a complete depth-D binary tree. Total multiplicative depth is bounded by `⌈log₂ l⌉ + ⌈log₂ p⌉ + 1`, where l is comparison precision and p is the PPI degree. Communication is `O(m + K)` ciphertexts for m input features and K forest groups.

## Correctness and Privacy Boundary

When each group stays within the N/2 error budget and the plaintext vote has a strict margin of at least one, deterministic rounding recovers every class count exactly, so the final encrypted prediction equals plaintext random-forest voting. Real models can occasionally produce exact vote ties; in that case, tiny residual CKKS noise may change the final `argmax` tie break. This is a difference in tie-handling policy, not a homomorphic evaluation error on non-tied samples.

The security analysis adopts a semi-honest two-party model and CKKS IND-CPA security. The server observes only public/evaluation keys and encrypted inputs, while the client receives per-group class votes and public metadata, not tree structures, thresholds, or intermediate node outcomes. Permitted public leakage is limited to general parameters such as comparison precision, tree count, class count, maximum depth, maximum leaves per class, and CKKS configuration.

## Evaluation

Experiments cover six UCI datasets: Iris, Wine, Heart, Steel, Breast, and Spam. The implementation uses OpenFHE CKKS with ring dimension 16,384 and 128-bit security. The evaluation varies forest size from 50 to 300 trees, depth from 7 to 15, and input precision across 6, 13, 26, and 53 bits, with HRF and Concrete-ML as baselines.

<figure class="project-flow-figure">
  <img src="/images/project/privacy-preserving-random-forest/accuracy-by-depth.png" alt="Plaintext and encrypted P³RF accuracy across tree depths on Breast, Heart, Spam, and Steel" loading="lazy">
  <figcaption>End-to-end accuracy: encrypted P³RF closely tracks plaintext P³RF and the Concrete-ML plaintext baseline on four representative datasets; the small differences come only from exact voting ties.</figcaption>
</figure>

| Evaluation | Baseline | P³RF result |
| --- | --- | ---: |
| Aggregation on 64-tree models | HRF | **7.1×–39.9×** speedup |
| End-to-end inference on 64-tree models | HRF | **1.2×–4.6×** speedup |
| End-to-end inference across tree counts, depths, and precision | Concrete-ML | **3.6×–70.7×** speedup |
| Ciphertext accuracy | Plaintext P³RF / Concrete-ML | Identical on non-tied samples |

PGA reduces tree-level aggregation from 25%–60% of HRF's total latency to roughly 3%–7%. Once aggregation is amortized, encrypted node comparison becomes the dominant bottleneck. End-to-end latency scales approximately linearly with both tree count and depth, identifying a clear direction for future optimization.

## Contributions

- Proposed the non-interactive P³RF protocol for scaling private decision-tree evaluation to random forests;
- Developed the path-indicator polynomial and PIPS parameter-selection algorithm, with proofs for exact group-vote recovery and polynomial-degree bounds;
- Designed the PGA slot layout and adaptive forest partitioning mechanism to improve CKKS SIMD utilization on irregular trees;
- Evaluated accuracy, forest size, tree depth, and input precision on six public datasets against HRF and Concrete-ML;
- Formalized client-data privacy, server-model privacy, permitted leakage, and communication complexity under the semi-honest model.
