---
title: "高校大学生公益认知及参与度调查"
order: 7
track: "modeling"
featured: false
period: "2023"
role: "编程及数据处理｜正大杯省级二等奖"
status: "complete"
visual: "modeling"
icon: "◎"
visual_label: "RF · K-Means · SEM"
cover: "/images/project/public-welfare-analysis/cover.jpg"
tech:
  - "随机森林"
  - "K-Means"
  - "结构方程模型"
  - "SPSS / AMOS"
summary: "面向长株潭高校大学生，以 758 份有效问卷构建从抽样调查、群体画像到影响机制检验的分析链路，为校园公益活动设计与参与提升提供数据依据。"
---

## 项目概述

本项目为第十三届“正大杯”全国大学生市场调查与分析大赛参赛作品，围绕“大学生如何认识公益、哪些因素影响其参与、不同群体需要怎样的公益活动”展开研究。团队以长株潭高校大学生为调查对象，将网络数据挖掘、问卷调查、机器学习与结构方程模型结合起来，形成从研究对象选择、样本获取、数据检验到策略建议的完整调研流程。

我主要负责项目中的**编程及数据处理**，为网络数据整理、问卷数据分析、模型实现和结果解释提供技术支持。项目最终获得 **2023 年“正大杯”全国大学生市场调查与分析大赛省级二等奖**。

## 研究设计

### 研究对象与数据来源

在正式问卷调查前，团队先爬取并分析中国志愿服务网的 **1,140 条**活动数据和湖南志愿服务网的 **14,401 条**活动及地区数据，通过词频与词云分析识别湖南公益活动的关注主题及地域分布，并据此将长株潭高校学生确定为主要研究对象。

正式调查采用分层抽样与多阶段 PPS 抽样：先按长沙、湘潭、株洲的高校分布进行分层，再按高校规模、院系与班级逐级抽样，并结合线上和线下方式发放问卷。项目共发放问卷 **940 份**，回收有效问卷 **758 份**，有效回收率约 **81%**。

### 问卷与质量控制

问卷覆盖个人背景、公益参与频率、参与渠道、参与或未参与原因，以及公益意愿、公益态度、期望收获、公益认知和公益动机五类潜变量。团队通过预调查、深度访谈和专家咨询迭代问卷，并对明显错误、前后矛盾或量表答案异常一致的样本进行清理。

正式量表的 Cronbach's Alpha 为 **0.913**，KMO 为 **0.937**，Bartlett 球形检验显著，表明数据具有较好的内部一致性，并适合继续开展主成分分析和因子分析。

<figure class="half">
  <img src="/images/project/public-welfare-analysis/participation-overview.jpeg" alt="大学生公益认知与参与现状统计图" loading="lazy">
  <img src="/images/project/public-welfare-analysis/participation-reasons.jpeg" alt="大学生参与公益活动原因分布图" loading="lazy">
  <figcaption>调研结果可视化：左图呈现公益认知与参与现状，右图展示大学生参与公益活动的主要动因。</figcaption>
</figure>

## 分析方法

项目构建了“**描述现状—验证差异—识别人群—解释机制**”的四层分析链路：

1. **描述性统计与列联分析：** 描述样本构成、公益参与方式与信息渠道，并通过卡方检验判断性别、学生干部经历、生活费和政治面貌与参与频率之间是否存在显著关联。
2. **随机森林：** 以学生干部经历、生活费和政治面貌等变量预测公益参与情况，并检验不同特征的重要程度。设置 1,000 棵决策树后，袋外错误率稳定在 **0.165**。
3. **K-Means 群体画像：** 基于公益认知、公益态度、公益意愿和期望收获等量表变量，将受访者划分为公益参与核心群体、主要群体、次要群体和边缘群体，为差异化触达提供依据。
4. **因子分析与结构方程模型：** 对 22 个量表指标进行主成分分析，提取 5 个主成分，累计解释方差为 **62.1%**；进一步结合 Pearson 相关分析和结构方程模型，检验公益认知、态度、动机、期望收获与参与意愿之间的路径关系。

### 随机森林验证

<figure class="half">
  <img src="/images/project/public-welfare-analysis/random-forest-importance.jpeg" alt="随机森林变量重要程度排序" loading="lazy">
  <img src="/images/project/public-welfare-analysis/random-forest-oob.png" alt="随机森林袋外错误率随决策树数量变化曲线" loading="lazy">
  <figcaption>随机森林结果：左图比较参与特征的重要程度，右图显示袋外错误率随决策树数量增加逐步稳定在约 0.165。</figcaption>
</figure>

### K-Means 群体划分

<figure class="half">
  <img src="/images/project/public-welfare-analysis/kmeans-process.png" alt="K-Means 聚类中心迭代过程示意图" loading="lazy">
  <img src="/images/project/public-welfare-analysis/kmeans-clusters.png" alt="大学生公益参与群体聚类结果分布图" loading="lazy">
  <figcaption>K-Means 分析：通过“分配样本—更新中心—重新分配”的迭代过程，将受访者划分为四类公益参与群体。</figcaption>
</figure>

### 影响机制建模

<figure class="project-flow-figure">
  <img src="/images/project/public-welfare-analysis/impact-model.png" alt="公益态度、期望收获、公益动机、公益认知和公益意愿之间的假设路径模型" loading="lazy">
  <figcaption>参与公益意愿影响因素概念模型：以五类潜变量组织待检验的关系路径。</figcaption>
</figure>

<figure>
  <img src="/images/project/public-welfare-analysis/sem-model.png" alt="大学生公益参与意愿结构方程模型及标准化路径系数" loading="lazy">
  <figcaption>结构方程模型结果：将 22 个观测变量映射到五类潜变量，并估计潜变量之间的路径系数。</figcaption>
</figure>

## 核心发现

- 大学生更偏好投入个人时间与精力的公益方式，蚂蚁森林、捐步和在线捐款等微公益形式较受欢迎。
- 女性、月生活费超过 1,000 元的学生，以及担任学生干部、党员或团员的学生，整体公益参与更积极。
- 帮助他人、增强人际关系和锻炼能力是参与公益的主要动因；活动流于形式、宣传不足和组织者专业性不足，是阻碍参与的重要问题。
- 超过一半的受访大学生具有较强的公益参与意愿，多数受访者对公益具备较好的认知。
- 结构方程模型显示，公益认知和期望收获对参与意愿具有显著正向影响；公益认知还会通过期望收获和公益态度形成进一步影响。

## 策略建议

基于分析结果，项目提出三类改进方向：高校可通过公益知识讲座、团委和学生组织加强公益教育与信息传播；公益组织可将校园公益与社会公益结合，设计形式更新颖、参与门槛更低的项目；活动组织方应加强专业培训和过程透明度，并通过证书、志愿时长、交通或餐饮补贴等适度激励提升参与体验。

## 个人贡献

- 负责项目编程与数据处理，参与网络数据整理、问卷数据清洗和分析数据集构建；
- 支撑随机森林、K-Means 等模型的实现与结果整理，并参与统计分析结果解释；
- 将数据分析结果转化为可呈现的群体画像、关键结论与调研报告内容。
