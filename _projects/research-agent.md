---
title: "Research Agent 智能研究助手"
order: 8
track: "ai-engineering"
featured: true
visual: "ai-engineering"
icon: "✦"
visual_label: "Research · RAG"
cover: "/images/project/research-agent/overview.png"
tech:
  - "Next.js"
  - "React"
  - "TypeScript"
  - "FastAPI"
  - "RAG"
  - "知识图谱"
summary: "面向学术研究的一站式智能工作台，将多源文献检索、PDF 解析、项目知识组织、领域树与知识图谱构建，以及带证据的研究问答串联为完整工作流。"
---

## 项目概述

Research Agent 面向需要持续阅读、整理和比较大量论文的研究场景。传统工作流通常分散在搜索引擎、PDF 阅读器、笔记和通用对话工具之间，文献范围、阅读上下文与回答引用难以保持一致。项目因此以“**文献获取—项目归档—知识建模—证据问答**”为主线，将研究资料沉淀为可检索、可追溯、可继续扩展的项目知识空间。

系统采用前后端分离架构：前端以 Next.js、React 与 TypeScript 构建研究工作台，后端以 FastAPI 提供文献、项目、解析、后台任务和研究问答接口。功能模块按职责划分，搜索供应商、项目存储、领域分析、关系建模与问答管线可以独立演进，避免把全部研究逻辑耦合在单一 Agent 或页面组件中。

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/overview.png" width="100%">
    <source src="/images/project/research-agent/overview.webm" type="video/webm">
    当前浏览器不支持 HTML5 视频，可直接查看演示封面。
  </video>
  <figcaption>产品总览：从文献检索与项目归档出发，进入领域树、文献地图、知识图谱和研究对话。</figcaption>
</figure>

## 统一的研究工作台

首页提供研究对话、数据集中心、项目知识空间与设置四个入口，并支持亮色、暗色主题切换。进入应用后，顶部导航保持各模块的位置与状态一致，使用户能够在检索、知识组织和问答之间快速切换，而无需重新建立研究上下文。

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/home-navigation.png" width="100%">
    <source src="/images/project/research-agent/home-navigation.webm" type="video/webm">
    当前浏览器不支持 HTML5 视频，可直接查看演示封面。
  </video>
  <figcaption>首页与全局导航：展示模块入口、亮暗主题及从首页进入研究工作区的过程。</figcaption>
</figure>

## 多源文献检索与资料沉淀

数据集中心将在线检索与本地文献库放在同一工作区。在线检索支持按关键词、年份区间、每源目标篇数、数据源、CCF 等级和最低影响因子组合筛选，并并行呈现各来源的搜索进度与结果。当前接入 arXiv、PubMed、Crossref、IEEE 与开放获取来源；不同来源的返回结果在后端被标准化为统一论文结构，前端无需感知各平台字段差异。

用户可把检索结果或本地 PDF 纳入项目。解析环节负责提取论文正文与结构信息，并将可用文献转换为后续领域分析和检索增强问答能够消费的语料。搜索、解析与项目归档分别封装，既便于替换外部数据源，也避免解析失败阻塞基础文献管理。

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/paper-search.png" width="100%">
    <source src="/images/project/research-agent/paper-search.webm" type="video/webm">
    当前浏览器不支持 HTML5 视频，可直接查看演示封面。
  </video>
  <figcaption>论文检索：组合数据源、时间、CCF 等级与影响因子条件，并查看分来源检索进度。</figcaption>
</figure>

## 以项目为边界的知识空间

项目是系统中的研究隔离单元。用户可以建立项目、搜索与筛选文献，并控制哪些论文参与当前项目的问答、领域树与知识图谱构建。界面同步汇总项目文献数、知识节点数和关系数，使语料范围及知识加工状态保持可见。

这一边界不仅存在于界面层：后端由项目仓储维护论文成员关系，领域分析和研究检索只消费当前项目的可信语料范围，避免其他项目的论文或历史回答意外混入证据集合。

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/project-literature.png" width="100%">
    <source src="/images/project/research-agent/project-literature.webm" type="video/webm">
    当前浏览器不支持 HTML5 视频，可直接查看演示封面。
  </video>
  <figcaption>项目文献管理：创建研究项目、检索项目论文，并显式应用参与分析的文献范围。</figcaption>
</figure>

## 从论文集合到结构化知识

### 文献地图

文献地图把项目论文组织为可浏览的研究脉络。用户可按年份筛选论文，查看每篇工作的摘要、主题标签和核心声明，并继续展开与声明关联的原文证据。相比仅按文件名维护 PDF，这一视图更适合横向比较研究任务、方法与实验结论。

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/literature-map.png" width="100%">
    <source src="/images/project/research-agent/literature-map.webm" type="video/webm">
    当前浏览器不支持 HTML5 视频，可直接查看演示封面。
  </video>
  <figcaption>文献地图：按年份浏览论文脉络，查看研究标签、核心声明与对应证据。</figcaption>
</figure>

### 领域树

领域树把项目语料归纳为分层研究主题，并保留从分类标签回到原始文献分块的入口。用户可以触发模型生成或重建领域树，也可以编辑、删除节点；选中节点后可在侧栏核对对应原文目录与证据。当证据不足时，系统明确提示缺少匹配分块，而不是生成无法追溯的说明。

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/domain-tree.png" width="100%">
    <source src="/images/project/research-agent/domain-tree.webm" type="video/webm">
    当前浏览器不支持 HTML5 视频，可直接查看演示封面。
  </video>
  <figcaption>领域树：生成和编辑分层主题，并从节点回溯原始目录及文献分块。</figcaption>
</figure>

### 知识图谱

知识图谱把论文中的实体、关系与证据组织成可筛选的关系浏览器。用户可以按关键词、实体类型、关系类型、研究领域和关联文献缩小范围；关系列表展示关系方向、置信度与证据数量，详情面板支持继续核对实体属性和原文证据。关系编辑与删除入口使自动抽取结果能够由研究者校正。

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/knowledge-graph.png" width="100%">
    <source src="/images/project/research-agent/knowledge-graph.webm" type="video/webm">
    当前浏览器不支持 HTML5 视频，可直接查看演示封面。
  </video>
  <figcaption>知识图谱：筛选实体与关系，查看置信度、关联文献和支持关系的原文证据。</figcaption>
</figure>

## 带证据的研究对话

研究对话以当前项目和所选论文为检索边界。系统先解析对话上下文与问题约束，再进行候选召回、证据组装、证据覆盖评估和必要的补偿检索，最后生成回答并校验引用。界面在正文中标注引用编号，右侧同步展示检索进度、证据覆盖率、引用论文和全文相关片段，用户可以从答案直接回到支撑该结论的材料。

对话区还支持研究记忆、全局偏好与报告导出，适合在同一主题下继续追问和沉淀阶段性结论。历史回答只用于解析上下文，不会自动作为新的事实证据，从而把“对话连续性”与“证据可信度”分开处理。

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/research-chat.png" width="100%">
    <source src="/images/project/research-agent/research-chat.webm" type="video/webm">
    当前浏览器不支持 HTML5 视频，可直接查看演示封面。
  </video>
  <figcaption>研究对话：生成带编号引用的综述，并在侧栏核对检索覆盖、论文来源与全文证据。</figcaption>
</figure>

## 系统设计

系统以高内聚、低耦合为模块划分原则：

- **交互层：** Next.js App Router 组织数据集、项目知识与研究对话页面，React 组件负责可复用交互，TypeScript 约束前后端数据形状。
- **接口层：** FastAPI 路由只处理请求校验与响应映射，文献、项目、领域树、文献地图、设置和后台任务各有独立入口。
- **领域服务层：** 搜索分发、PDF 解析、项目范围、文档结构索引、候选召回、证据组装与知识建模均由单一职责服务承担。
- **Agent 编排层：** Agent 负责研究流程协调和工具调用，不直接承担持久化、第三方网络请求或全部检索细节。
- **任务与存储层：** 长耗时解析和知识构建通过后台任务运行，并保存任务、会话、项目与知识结果，支持状态查询、取消、重试和失败恢复。

研究问答的主依赖方向保持为“上下文 → 问题契约 → 结构索引 → 候选召回 → 证据组装 → 覆盖评估 → 补偿检索或答案生成 → 引用校验”。各阶段通过明确的数据契约衔接，下游不反向修改上游约束，便于独立测试和替换检索或模型实现。

## 项目成果

项目完成了从资料发现到知识复用的端到端闭环：多源搜索负责扩展文献集合，项目空间固定可信语料范围，文献地图与领域树提供宏观结构，知识图谱呈现细粒度关系，研究对话再把这些材料转化为带原文证据的回答。通过把项目隔离、证据覆盖与引用校验作为系统级约束，Research Agent 从通用聊天界面扩展为可核查、可持续积累的研究工作台。
