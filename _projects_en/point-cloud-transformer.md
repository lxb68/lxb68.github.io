---
title: "PointNet Inference with CUDA and Triton"
order: 7
track: "ai-engineering"
featured: true
period: "To be added"
role: "Course Project"
status: "draft"
visual: "ai-engineering"
icon: "◈"
visual_label: "CUDA · Triton"
cover: "/images/project/cuda_inference/cover.jpg"
tech: ["CUDA", "Triton", "PointNet", "3D MNIST", "PyTorch"]
summary: "Trained PointNet for 3D MNIST classification and implemented equivalent inference paths in CUDA C++ and Triton to compare accuracy and end-to-end latency."
---

## Background

This project is a hands-on deep-learning inference exercise. A PointNet classifier is first trained in PyTorch, after which its forward pass is implemented independently in CUDA C++ and Triton. The goal is not to redesign the network, but to migrate trained parameters reliably to two GPU backends and evaluate both correctness and execution efficiency.

The task uses the [3D MNIST dataset](https://www.kaggle.com/datasets/daavoo/3d-mnist/data) and the [PointNet architecture](https://arxiv.org/abs/1612.00593) for 3D point-cloud digit classification.

## Pipeline

1. `train.py` loads the training set, trains PointNet, and exports model parameters.
2. The test set is processed with the same layout, data type, sampling, and normalization rules used during training.
3. `test.cu` loads the parameters and performs the forward pass in CUDA C++.
4. `test.py` implements the equivalent forward path with Triton kernels.
5. Both implementations are evaluated using classification accuracy and inference time.

## Model and Workload

3D MNIST represents handwritten digits as voxels or point clouds. PointNet applies shared feature transformations to individual points, uses a symmetric reduction to produce an order-invariant global representation, and passes that representation to a classification head.

The workload therefore combines highly parallel point-wise linear operations with cross-point max reductions. This makes it a useful exercise in memory layout, coalesced access, reduction design, synchronization, and kernel launch configuration.

## CUDA Implementation

The CUDA path uses `test.cu` as its inference entry point and coordinates parameter loading, device memory, kernel launches, and result transfer. Correctness depends on matching the exported weight layout, using a consistent feature layout between layers, covering arbitrary point counts in reduction kernels, and applying explicit synchronization at timing boundaries. Device buffers should be reused where possible to avoid measuring repeated allocation and unnecessary host-device transfers.

## Triton Implementation

The Triton path uses `test.py` to organize the inference pipeline and express the main GPU operations as blocked Triton programs. Its tuning space includes tile sizes, memory coalescing, masking, and parallel reductions. Both backends share the same trained parameters, samples, preprocessing, and prediction rules so that measured differences are attributable to the inference implementation.

## Validation and Benchmarking

Before optimization, intermediate tensors should be compared against the PyTorch reference on a small sample set. This isolates common errors such as transposed weights, indexing mistakes, incompatible layouts, or unexpected floating-point differences.

| Metric | CUDA | Triton | Notes |
| --- | ---: | ---: | --- |
| Test accuracy | Pending | Pending | Compare with the PyTorch reference |
| Per-sample / batch latency | Pending | Pending | Report the batch size and statistic |
| End-to-end inference time | Pending | Pending | Use identical timing boundaries |
| GPU kernel time | Pending | Pending | Warm up, then aggregate repeated runs |

The source code, logs, and hardware configuration are not currently present in this repository, so this page intentionally does not invent accuracy or speedup numbers. A reproducible conclusion can be added once the GPU model, CUDA and Triton versions, batch size, repetition count, and measured outputs are available.

## Takeaways

The project covers the full path from model training and parameter export to custom GPU kernels, numerical validation, and performance measurement. It demonstrates practical understanding of PointNet computation, cross-backend parameter mapping, GPU data layouts and reductions, synchronization-aware benchmarking, and fair comparison between CUDA C++ and Triton.
