---
permalink: /en/projects/
title: "Projects"
excerpt: "Projects in scheduling, machine learning, privacy, and AI engineering"
author_profile: true
lang: en
---

<div class="projects-intro">
  <p class="eyebrow">PROJECT INDEX</p>
  <h1>From problem formulation to system implementation</h1>
</div>

{% assign items = site.projects_en | sort: 'order' %}
{% for track in site.data.project_tracks %}
<section class="project-track-section" id="{{ track.key }}">
  <div class="project-track-heading">
    <span class="project-track-icon" aria-hidden="true">{{ track.icon }}</span>
    <div>
      <h2>{{ track.title_en }}</h2>
      <p>{{ track.description_en }}</p>
    </div>
  </div>
  <div class="resume-project-cards resume-project-cards--compact">
    {% assign track_items = items | where: 'track', track.key %}
    {% for p in track_items %}{% include project-card.html project=p %}{% endfor %}
  </div>
</section>
{% endfor %}
