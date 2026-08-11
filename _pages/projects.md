---
permalink: /projects/
title: "项目"
excerpt: "智能调度、机器学习、隐私保护与 AI 工程项目"
author_profile: true
lang: zh
---

<div class="projects-intro">
  <p class="eyebrow">PROJECT INDEX</p>
  <h1>从问题建模到系统实现</h1>
</div>

{% assign items = site.projects | sort: 'order' %}
{% for track in site.data.project_tracks %}
<section class="project-track-section" id="{{ track.key }}">
  <div class="project-track-heading">
    <span class="project-track-icon" aria-hidden="true">{{ track.icon }}</span>
    <div>
      <h2>{{ track.title }}</h2>
      <p>{{ track.description }}</p>
    </div>
  </div>
  <div class="resume-project-cards resume-project-cards--compact">
    {% assign track_items = items | where: 'track', track.key %}
    {% for p in track_items %}{% include project-card.html project=p %}{% endfor %}
  </div>
</section>
{% endfor %}
