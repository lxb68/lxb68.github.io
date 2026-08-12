---
permalink: /en/
title: ""
excerpt: "Wanhua Li's homepage"
author_profile: true
lang: en
redirect_from:
  - /en/about/
  - /en/about.html
---

<span class="anchor" id="about-me"></span>
# Hello, I'm Wanhua Li

I am a graduate student in Electronic Information (Computer Science) at the University of Chinese Academy of Sciences. My work spans **intelligent scheduling, machine learning, privacy-preserving computing, and AI engineering**—from problem formulation and simulation to GPU training and web application development.

I am currently seeking opportunities in privacy-preserving machine learning. Contact: [lwh430321@163.com](mailto:lwh430321@163.com)

<div class="capability-grid" aria-label="Research and project areas">
  {% for track in site.data.project_tracks %}
  <a class="capability-card" href="{{ '/en/projects/' | relative_url }}#{{ track.key }}" target="_self">
    <span class="capability-icon" aria-hidden="true">{{ track.icon }}</span>
    <h2>{{ track.title_en }}</h2>
    <p>{{ track.description_en }}</p>
  </a>
  {% endfor %}
</div>

<span class="anchor" id="projects"></span>
## 🧩 Selected Projects

{% assign items = site.projects_en | sort: 'order' %}
<div class="resume-project-cards">
  {% for p in items %}
    {% if p.featured %}{% include project-card.html project=p %}{% endif %}
  {% endfor %}
</div>

<p class="projects-more"><a class="btn btn--primary" href="{{ '/en/projects/' | relative_url }}" target="_self">Explore all projects by track →</a></p>

<span class="anchor" id="education"></span>
## 🎓 Education

<div class="resume-grid education-grid">
  <article class="resume-card education-card">
    <header class="education-card__header">
      <img class="education-card__logo" src="{{ '/images/中国科学院.png' | relative_url }}" alt="" style="width: 56px; height: 56px; object-fit: contain;">
      <div class="education-card__identity">
        <h3>University of Chinese Academy of Sciences</h3>
        <p class="education-card__degree">Electronic Information (Computer Science)</p>
      </div>
      <span class="education-card__level education-card__level--graduate">Master’s</span>
    </header>
    <p class="education-card__meta">Sep. 2024 - Present · GPA <span class="metric">3.78/4.0</span></p>
    <p>Selected coursework: Applied Cryptography (91), GPU Architecture and Programming (95), Optimization Methods and Implementation (94), Pattern Recognition and Machine Learning (84).</p>
  </article>
  <article class="resume-card education-card">
    <header class="education-card__header">
      <img class="education-card__logo" src="{{ '/images/湖南科技大学.png' | relative_url }}" alt="" style="width: 56px; height: 56px; object-fit: contain;">
      <div class="education-card__identity">
        <h3>Hunan University of Science and Technology</h3>
        <p class="education-card__degree">Information and Computing Science (B+)</p>
      </div>
      <span class="education-card__level education-card__level--undergraduate">Bachelor’s</span>
    </header>
    <p class="education-card__meta">Sep. 2020 - Jun. 2024 · GPA <span class="metric">3.68/4.0</span> · Rank <span class="metric">4/132</span></p>
  </article>
</div>

<span class="anchor" id="work-experience"></span>
## 💼 Internships

### Xiaomi Corporation

**Data R&D | Feb. 2025 - Jun. 2025**

- **End-to-end data science:** Managed the full workflow from data acquisition, cleaning, and feature engineering to model training, evaluation, and production deployment. Cleaned, segmented by dimension, aggregated, and structured millions of daily user-browsing records, providing data support for lending operations and cost control.
- **Text semantic analysis:** Used Word2Vec to create vector representations of a domain-specific text corpus, enabling similar-text retrieval and supporting semantic analysis for relevant business scenarios.
- **Knowledge base development:** Led the design and implementation of a team knowledge base, systematically organizing technical documentation and business processes to improve onboarding, information retrieval, and knowledge reuse.

<span class="anchor" id="honors"></span>
## 🏅 Honors

- 2025: Outstanding Student, University of Chinese Academy of Sciences
- 2024: Outstanding Graduate of Hunan Province; National Encouragement Scholarship
- 2023: Provincial Second Prize, National Market Survey and Analysis Competition
- 2022: National Second Prize, CUMCM (Team Leader)
- 2022: Provincial First Prize, National College Mathematics Competition (Category B)

<span class="anchor" id="skills"></span>
## 🛠️ Skills

- Proficient in C/C++ and Python; foundational knowledge of Java
- Familiar with common algorithms, data structures, and GPU architecture
- Former class monitor and deputy secretary of the Mathematical Modeling Association Youth League branch
