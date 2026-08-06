---
title: "基于 CUDA 的 PointNet 分类网络推理"
order: 2
track: "ai-engineering"
featured: true
period: "2025"
role: "独立完成"
status: "complete"
visual: "ai-engineering"
icon: "◈"
visual_label: "CUDA · PointNet"
cover: "/images/project/cuda_inference/cover.jpg"
tech:
  - "CUDA"
  - "PointNet"
  - "3D MNIST"
  - "PyTorch"
  - "C++"
summary: "面向 3D MNIST 点云分类任务，使用 CUDA C++ 实现简化 PointNet 的完整推理流程，最终准确率达到 95.2%，推理时间低于 11.34 秒。"
---

## 项目概述

本项目围绕 3D MNIST 点云分类开展 GPU 推理实践：首先使用 PyTorch 完成模型训练与参数导出，再以 CUDA C++ 独立实现前向计算，重点验证训练参数迁移、自定义算子正确性以及端到端推理效率。

模型基于 PointNet 分类网络进行简化。它不依赖规则网格或点的排列顺序，而是对每个点应用相同的特征提取函数，再通过对称聚合获得整个点云的全局表示，最终输出 10 个数字类别的得分。

## 网络结构

参考原始 PointNet 分类架构，本项目保留三项核心设计：`3×3` 输入变换、共享逐点卷积和全局最大池化；未启用 `64×64` 特征变换，也不包含分割分支。由此将计算链路集中在分类任务所需的最小闭环上。

<figure>
  <img src="/images/project/cuda_inference/pointnet-architecture.png" alt="PointNet 论文中的分类网络与分割网络完整架构图">
  <figcaption>PointNet 完整架构。<a href="https://arxiv.org/pdf/1612.00593" target="_blank" rel="noopener noreferrer">图源：PointNet 原论文 Figure 2</a>。本项目仅采用上方分类主干中的 3×3 输入变换、共享逐点卷积、全局最大池化与分类头，未启用 64×64 特征变换及下方分割分支。</figcaption>
</figure>

本项目实际采用的前向路径如下：

<div class="pointnet-path" aria-label="简化 PointNet 前向路径">
  <div class="pointnet-path__step">
    <span class="pointnet-path__index">01</span>
    <strong>输入点云</strong>
    <span class="pointnet-path__meta">N × 3</span>
  </div>
  <div class="pointnet-path__step">
    <span class="pointnet-path__index">02</span>
    <strong>输入变换</strong>
    <span class="pointnet-path__meta">T-Net · 3 × 3</span>
  </div>
  <div class="pointnet-path__step">
    <span class="pointnet-path__index">03</span>
    <strong>共享逐点卷积</strong>
    <span class="pointnet-path__meta">3 → 64 → 128 → 1024</span>
  </div>
  <div class="pointnet-path__step">
    <span class="pointnet-path__index">04</span>
    <strong>全局最大池化</strong>
    <span class="pointnet-path__meta">N × 1024 → 1024</span>
  </div>
  <div class="pointnet-path__step pointnet-path__step--final">
    <span class="pointnet-path__index">05</span>
    <strong>分类输出</strong>
    <span class="pointnet-path__meta">1024 → 512 → 256 → 10</span>
  </div>
  <div class="pointnet-path__scope" aria-label="模型启用范围">
    <span class="pointnet-path__tag pointnet-path__tag--enabled">✓ 分类路径</span>
    <span class="pointnet-path__tag">— 64×64 特征变换</span>
    <span class="pointnet-path__tag">— 分割分支</span>
  </div>
</div>

### 3×3 输入变换

输入 T-Net 根据每个点云预测一个 `3×3` 矩阵，并将其与单位矩阵相加后用于坐标对齐。这一步提升了模型对点云旋转与坐标姿态变化的适应能力，同时保留了较低的计算开销。

### 共享逐点卷积

主干网络使用共享的 `1×1 Conv1D` 对每个点执行相同的通道变换。卷积权重在所有点之间共享，因此既能并行提取局部点特征，又不会引入对输入排列顺序的依赖。

### 全局最大池化与分类

全局最大池化在所有点上提取每个通道的最大响应，将 `[N, 1024]` 聚合为固定长度的 `[1024]` 全局特征。分类头随后输出 10 类 logits；推理阶段直接取 `argmax`，无需额外计算 Softmax。

## CUDA 推理流程

1. **训练与导出**：使用 PyTorch 训练简化 PointNet，并导出卷积、BatchNorm 与全连接层参数。
2. **数据加载**：读取 3D MNIST 测试点云与标签，整理为 CUDA 前向计算所需的数据布局。
3. **自定义算子执行**：依次完成输入变换、共享逐点卷积、归一化与激活、最大值归约和全连接计算。
4. **结果汇总**：回传分类结果，统计测试集准确率与 CUDA 推理耗时。

CUDA 实现的关键在于保持训练端与推理端的权重维度、张量布局和 BatchNorm 参数一致，并正确处理矩阵变换、逐点并行计算与跨点最大值归约。设备端缓冲区复用和同步边界控制则用于减少额外开销，使计时结果更能反映实际推理性能。

## 实验结果

在统一测试集与计时口径下，CUDA 版本的最终结果如下：

| 指标 | CUDA 最终结果 |
| --- | ---: |
| 测试集准确率 | **95.2%** |
| CUDA 推理时间 | **< 11.34 s** |

最终准确率达到 **95.2%**，说明简化网络在移除 `64×64` 特征变换和分割分支后，仍能有效完成 3D 点云数字分类；推理时间控制在 **11.34 秒以内**，验证了 CUDA 实现的完整性与执行效率。

## 项目收获

- 理解 PointNet 通过共享逐点特征提取与对称聚合处理无序点集的核心机制；
- 完成 PyTorch 参数到 CUDA C++ 推理链路的映射与结果验证；
- 实践矩阵变换、逐点卷积、最大值归约和全连接层的 CUDA 算子组织；
- 在明确模型边界的前提下，以更精简的分类网络降低实现复杂度和模块耦合。
