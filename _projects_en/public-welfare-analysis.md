---
title: "University Students' Awareness of and Participation in Public Welfare"
order: 5
track: "modeling"
featured: false
period: "2023"
role: "Programming & Data Processing | Provincial Second Prize"
status: "complete"
visual: "modeling"
icon: "◎"
visual_label: "RF · K-Means · SEM"
cover: "/images/project/public-welfare-analysis/cover.svg"
tech: ["Random Forest", "K-Means", "Structural Equation Modeling", "SPSS / AMOS"]
summary: "Built an end-to-end survey and modeling workflow from 758 valid responses to identify student segments and explain the factors influencing participation in public-welfare activities."
---

## Project Overview

This project was developed for the 13th CP Cup National College Student Market Survey and Analysis Competition. It investigated how university students understand public welfare, what drives or prevents participation, and how activities can be designed for different student groups. Focusing on universities in Changsha, Zhuzhou, and Xiangtan, the team combined web data mining, survey research, machine learning, and structural equation modeling in one analytical workflow.

I was primarily responsible for **programming and data processing**, supporting web-data preparation, survey-data analysis, model implementation, and interpretation. The project received a **Provincial Second Prize in 2023**.

## Research Design

### Scope and Data Collection

Before designing the formal survey, the team analyzed **1,140** activity records from the China Volunteer Service website and **14,401** activity and location records from the Hunan Volunteer Service website. Frequency analysis and word clouds were used to identify major themes and geographic concentrations, which supported the selection of university students in the Changsha-Zhuzhou-Xiangtan region as the target population.

The formal study used stratified sampling and multi-stage probability-proportional-to-size sampling across cities, universities, departments, and classes. A total of **940 questionnaires** were distributed and **758 valid responses** were collected, giving an effective response rate of approximately **81%**.

### Questionnaire Quality

The questionnaire covered demographics, participation frequency, information channels, motivations and barriers, as well as five latent constructs: willingness, attitude, expected gains, awareness, and motivation. The instrument was refined through a pilot survey, interviews, and expert consultation; inconsistent and low-quality responses were removed before analysis.

The final scale achieved a Cronbach's alpha of **0.913** and a KMO value of **0.937**, with a significant Bartlett's test, supporting subsequent principal-component and factor analyses.

<figure class="half">
  <img src="/images/project/public-welfare-analysis/participation-overview.jpeg" alt="Survey charts summarizing student awareness of and participation in public welfare" loading="lazy">
  <img src="/images/project/public-welfare-analysis/participation-reasons.jpeg" alt="Distribution of students' motivations for participating in public-welfare activities" loading="lazy">
  <figcaption>Survey overview: the left panel summarizes awareness and participation patterns, while the right panel shows the leading motivations for participation.</figcaption>
</figure>

## Analytical Workflow

The analysis followed four connected stages:

1. **Descriptive and contingency analysis:** summarized participation patterns and used chi-square tests to examine associations between participation and gender, student-leadership experience, monthly living expenses, and political affiliation.
2. **Random forest modeling:** predicted participation from background variables and assessed feature importance. With 1,000 trees, the out-of-bag error stabilized at **0.165**.
3. **K-Means segmentation:** grouped respondents into core, primary, secondary, and peripheral public-welfare participation segments based on awareness, attitude, willingness, and expected gains.
4. **Factor analysis and structural equation modeling:** reduced 22 scale indicators to five principal components explaining **62.1%** of cumulative variance, then used Pearson correlations and a structural equation model to examine relationships among the latent constructs.

### Random Forest Validation

<figure class="half">
  <img src="/images/project/public-welfare-analysis/random-forest-importance.jpeg" alt="Random forest feature-importance ranking" loading="lazy">
  <img src="/images/project/public-welfare-analysis/random-forest-oob.png" alt="Random forest out-of-bag error by number of trees" loading="lazy">
  <figcaption>Random forest results: feature importance is shown on the left; the out-of-bag error on the right converges to approximately 0.165 as the number of trees increases.</figcaption>
</figure>

### K-Means Segmentation

<figure class="half">
  <img src="/images/project/public-welfare-analysis/kmeans-process.png" alt="Illustration of the iterative K-Means clustering process" loading="lazy">
  <img src="/images/project/public-welfare-analysis/kmeans-clusters.png" alt="Cluster distribution of university student public-welfare participation groups" loading="lazy">
  <figcaption>K-Means analysis: repeated assignment and centroid updates divided respondents into four public-welfare participation segments.</figcaption>
</figure>

### Modeling the Participation Mechanism

<figure class="project-flow-figure">
  <img src="/images/project/public-welfare-analysis/impact-model.png" alt="Hypothesized paths among attitude, expected gains, motivation, awareness, and willingness" loading="lazy">
  <figcaption>Conceptual model of participation willingness, organizing the hypothesized paths among five latent constructs.</figcaption>
</figure>

<figure>
  <img src="/images/project/public-welfare-analysis/sem-model.png" alt="Structural equation model of student public-welfare participation with estimated path coefficients" loading="lazy">
  <figcaption>Structural equation model: 22 observed variables are mapped to five latent constructs, with coefficients estimated for the paths among those constructs.</figcaption>
</figure>

## Key Findings

- Students preferred activities that contributed personal time and effort; Ant Forest, step-donation programs, and online donations were among the most popular forms of micro-philanthropy.
- Women, students with monthly living expenses above RMB 1,000, student leaders, and Party or Youth League members showed higher participation overall.
- Helping others, building relationships, and developing skills were the main motivations. Formalistic activities, insufficient publicity, and a lack of organizer expertise were major barriers.
- More than half of respondents showed relatively strong willingness to participate, while most demonstrated a sound awareness of public welfare.
- The structural equation model indicated that awareness and expected gains had significant positive effects on willingness; awareness also influenced participation through expected gains and attitude.

## Recommendations

The study recommended strengthening public-welfare education and communication through universities and student organizations, connecting campus initiatives with broader community programs, and designing activities that are more accessible and engaging. It also suggested improving organizer training and transparency, while using appropriate incentives such as certificates, volunteer-hour credits, transport support, or meal allowances to improve the participant experience.

## Personal Contributions

- Handled programming and data processing, including web-data preparation, survey cleaning, and analytical dataset construction.
- Supported the implementation and result organization of the random forest and K-Means models, and contributed to interpretation of the statistical findings.
- Translated analytical outputs into audience segments, key findings, and report-ready content.
