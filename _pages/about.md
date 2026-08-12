---
permalink: /
title: ""
excerpt: "李婉华的个人主页"
author_profile: true
lang: zh
redirect_from:
  - /about/
  - /about.html
---

<div class="resume-hero" id="about-me">
  <h1>你好，我是李婉华</h1>
  <p>现就读于<strong>中国科学院大学</strong>电子信息（计算机）专业，关注智能优化、机器学习与 AI 系统工程。我的项目覆盖从问题建模、算法设计和仿真验证，到 GPU 模型训练与 Web 应用实现的完整流程。</p>

  <div class="focus-tags"><span>智能调度</span><span>机器学习</span><span>隐私计算</span><span>CUDA</span><span>AI Agent</span><span>Python / C++</span></div>
</div>

<div class="capability-grid" aria-label="研究与项目方向">
  {% for track in site.data.project_tracks %}
  <a class="capability-card" href="{{ '/projects/' | relative_url }}#{{ track.key }}" target="_self">
    <span class="capability-icon" aria-hidden="true">{{ track.icon }}</span>
    <h2>{{ track.title }}</h2>
    <p>{{ track.description }}</p>
  </a>
  {% endfor %}
</div>

<span class="anchor" id="projects"></span>
## ✨ 代表项目

{% assign items = site.projects | sort: 'order' %}
<div class="resume-project-cards">
  {% for p in items %}
    {% if p.featured %}{% include project-card.html project=p %}{% endif %}
  {% endfor %}
</div>

<p class="projects-more"><a class="btn btn--primary" href="{{ '/projects/' | relative_url }}" target="_self">按四条主线查看全部项目 →</a></p>

<span class="anchor" id="education"></span>
## 🎓 教育背景

<div class="resume-grid education-grid">
  <article class="resume-card education-card">
    <header class="education-card__header">
      <img class="education-card__logo" src="{{ '/images/中国科学院.png' | relative_url }}" alt="" style="width: 56px; height: 56px; object-fit: contain;">
      <div class="education-card__identity">
        <h3>中国科学院大学</h3>
        <p class="education-card__degree">电子信息（计算机）</p>
      </div>
      <span class="education-card__level education-card__level--graduate">硕士研究生</span>
    </header>
    <p class="education-card__meta">2024.09 - 至今｜GPA <span class="metric">3.78/4.0</span></p>
    <p>应用密码学（91）、GPU 架构与编程（95）、算法中的最优化方法与实现（94）、模式识别与机器学习（84）。</p>
  </article>
  <article class="resume-card education-card">
    <header class="education-card__header">
      <img class="education-card__logo" src="{{ '/images/湖南科技大学.png' | relative_url }}" alt="" style="width: 56px; height: 56px; object-fit: contain;">
      <div class="education-card__identity">
        <h3>湖南科技大学</h3>
        <p class="education-card__degree">信息与计算科学（B+）</p>
      </div>
      <span class="education-card__level education-card__level--undergraduate">本科</span>
    </header>
    <p class="education-card__meta">2020.09 - 2024.06｜GPA <span class="metric">3.68/4.0</span>｜专业排名 <span class="metric">4/132</span></p>
    <p>数学分析（91）、高等代数（88）、概率论与数理统计（97）、数据结构（90）、操作系统（98）、C++ 面向对象程序设计（94）。</p>
  </article>
</div>

<span class="anchor" id="work-experience"></span>
## 💼 工作实习

<div class="project-item">
  <h3>小米科技有限责任公司</h3>
  <p><strong>数据研发｜2025.02 - 2025.06</strong></p>
  <ul>
    <li><strong>自动化流程：</strong>重构报表生成项目与 SQL 文件管理流程，基于 Shell 脚本、飞书 API 和 AI 大模型设计并实现自动化工作流，减少人工干预，提升效率并降低人力成本。</li>
    <li><strong>大模型应用：</strong>利用 Dify 平台与 RAG 技术构建数据分析、智能客服等 AI 工作流，推动业务智能化并优化应用效果。</li>
    <li><strong>数据科学全流程：</strong>负责从数据获取、清洗、特征工程，到模型训练、评估及生产级部署的完整数据科学工作流。</li>
    <li><strong>文本分类与语义分析：</strong>实现基于朴素贝叶斯模型的文本分类任务；利用 Word2Vec 为特定文本库生成词向量，支持相似文本检索。</li>
    <li><strong>知识库建设：</strong>主导设计并搭建团队知识库系统，系统化沉淀技术文档与流程，提升新人入职效率及团队信息检索与复用能力。</li>
  </ul>
</div>

<span class="anchor" id="honors"></span>
## 🏅 荣誉奖项

- **2025.06** 中国科学院大学校级三好学生
- **2024.06** 湖南省优秀毕业生、国家励志奖学金
- **2023** “正大杯”全国大学生市场调查与分析大赛省级二等奖（编程及数据处理）
- **2023** 全国大学生电子商务“创新、创意及创业”挑战赛省级三等奖（队长）
- **2022** 高教社杯全国大学生数学建模竞赛国家二等奖（队长）
- **2022** 全国大学生数学竞赛 B 类省级一等奖
- **2022** 湖南省大学生计算机程序设计竞赛省级三等奖

<span class="anchor" id="skills"></span>
## 🛠️ 技能与经历

- **编程：** 熟练使用 C/C++、Python，掌握 Java 基础；熟悉常见算法与数据结构，了解 GPU 底层架构。
- **综合能力：** 曾任湖南科技大学数学建模协会团支部副部长、班长，具备团队协作、表达沟通和快速学习能力。
