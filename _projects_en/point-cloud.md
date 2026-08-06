---
title: "PointNet Classification Inference with CUDA"
order: 7
track: "ai-engineering"
featured: true
period: "To be added"
role: "Course Project"
status: "complete"
visual: "ai-engineering"
icon: "◈"
visual_label: "CUDA · PointNet"
cover: "/images/project/cuda_inference/cover.jpg"
tech: ["CUDA", "PointNet", "3D MNIST", "PyTorch", "C++"]
summary: "Implemented end-to-end CUDA C++ inference for a simplified PointNet classifier on 3D MNIST, reaching 95.2% final accuracy in under 11.34 seconds."
redirect_from:
  - /en/projects/point-cloud-transformer/
---

## Overview

This project explores GPU inference for 3D MNIST point-cloud classification. The model is trained and exported with PyTorch, then its forward pass is implemented independently in CUDA C++. The work focuses on reliable parameter migration, correct custom operators, and end-to-end inference efficiency.

The network is a streamlined version of the PointNet classifier. Instead of relying on a regular grid or point order, it applies the same feature extractor to every point, aggregates the responses into a global representation, and predicts one of ten digit classes.

## Network Architecture

Following the original PointNet classification design, this implementation retains the `3×3` input transform, shared point-wise convolution, and global max pooling. The `64×64` feature transform is disabled, and the segmentation branch is not included. This keeps the model focused on the shortest complete path required for classification.

<figure>
  <img src="/images/project/cuda_inference/pointnet-architecture.png" alt="Complete classification and segmentation architecture from the PointNet paper">
  <figcaption>Complete PointNet architecture. <a href="https://arxiv.org/pdf/1612.00593" target="_blank" rel="noopener noreferrer">Source: Figure 2 in the original PointNet paper</a>. This project uses only the upper classification path's 3×3 input transform, shared point-wise convolution, global max pooling, and classification head; the 64×64 feature transform and lower segmentation branch are disabled.</figcaption>
</figure>

The implemented forward path is:

<figure>
  <img src="/images/project/cuda_inference/pointnet.png" alt="Actual forward path of the simplified PointNet classifier">
</figure>


### 3×3 Input Transform

The input T-Net predicts one `3×3` matrix for each point cloud. After adding the identity matrix, the transform aligns the input coordinates and improves robustness to changes in orientation while keeping the additional computation compact.

### Shared Point-wise Convolution

The backbone applies shared `1×1 Conv1D` layers to every point. Reusing the same weights across points makes the operation highly parallel and preserves independence from the input ordering.

### Global Aggregation and Classification

Global max pooling takes the strongest response in each channel and compresses `[N, 1024]` point features into a fixed `[1024]` global descriptor. The classification head produces ten logits, and inference uses `argmax` directly because Softmax would not change the predicted class.

## CUDA Inference Pipeline

1. **Train and export:** train the simplified PointNet in PyTorch and export convolution, BatchNorm, and fully connected parameters.
2. **Load data:** read 3D MNIST test point clouds and labels, then arrange them in the layout expected by the CUDA path.
3. **Run custom operators:** execute the input transform, shared point-wise convolution, normalization and activation, max reduction, and fully connected layers.
4. **Evaluate:** transfer predictions back and report test accuracy and CUDA inference time.

Correctness depends on keeping weight dimensions, tensor layouts, and BatchNorm parameters consistent with the training model. Reusing device buffers and controlling synchronization boundaries reduce avoidable overhead and make the reported timing representative of the inference path.

## Results

Using a consistent test set and timing boundary, the final CUDA results are:

| Metric | Final CUDA Result |
| --- | ---: |
| Test accuracy | **95.2%** |
| CUDA inference time | **< 11.34 s** |

The simplified classifier achieved **95.2%** final accuracy while completing CUDA inference in **under 11.34 seconds**. These results demonstrate that the reduced architecture remains effective for 3D digit classification and that the custom CUDA path executes the full model efficiently.

## Takeaways

- Understood how PointNet combines shared point-wise feature extraction with symmetric aggregation for unordered point sets.
- Mapped exported PyTorch parameters into a complete CUDA C++ inference path and validated its output.
- Implemented the computation flow around matrix transforms, point-wise convolution, max reduction, and fully connected layers.
- Reduced implementation complexity and module coupling by keeping only the components required for classification.
