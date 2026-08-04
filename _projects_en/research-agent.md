---
title: "Research Agent Workspace"
order: 8
track: "ai-engineering"
featured: true
visual: "ai-engineering"
icon: "✦"
visual_label: "Research · RAG"
cover: "/images/project/research-agent/overview.png"
tech: ["Next.js", "React", "TypeScript", "FastAPI", "RAG", "Knowledge Graph"]
summary: "An evidence-centered research workspace that connects multi-source literature discovery, PDF ingestion, project-scoped knowledge modeling, domain trees, knowledge graphs, and grounded research conversations."
---

## Overview

Research Agent is designed for research workflows that involve continuously finding, reading, organizing, and comparing papers. Instead of scattering context across search engines, PDF readers, notes, and general-purpose chat tools, it turns literature discovery, project curation, knowledge modeling, and evidence-grounded Q&A into one connected workflow.

The system uses a decoupled web architecture: a Next.js, React, and TypeScript frontend provides the research workspace, while a FastAPI backend exposes literature, project, parsing, background-job, and research endpoints. Search providers, project storage, domain analysis, relation modeling, and answer generation remain separate modules so that each capability can evolve independently.

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/overview.png" width="100%">
    <source src="/images/project/research-agent/overview.webm" type="video/webm">
    Your browser does not support HTML5 video. The poster image shows the recorded workflow.
  </video>
  <figcaption>Product overview: moving from literature discovery and project curation to domain modeling, knowledge graphs, and evidence-grounded conversations.</figcaption>
</figure>

## A Unified Research Workspace

The landing page provides direct entry points to research conversations, the dataset center, project knowledge spaces, and settings, with both light and dark themes. A persistent top-level navigation keeps these modules easy to reach without forcing users to rebuild their research context whenever they switch tasks.

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/home-navigation.png" width="100%">
    <source src="/images/project/research-agent/home-navigation.webm" type="video/webm">
    Your browser does not support HTML5 video. The poster image shows the recorded workflow.
  </video>
  <figcaption>Landing page and global navigation, including module entry points and light/dark theme switching.</figcaption>
</figure>

## Multi-source Literature Discovery

The dataset center combines online search and a local library in one workspace. Search criteria include keywords, year range, target results per source, source selection, CCF tier, and minimum impact factor. The interface reports progress independently for arXiv, PubMed, Crossref, IEEE, and open-access sources, while the backend normalizes provider-specific responses into a common paper model.

Search results and local PDFs can be added to a project. The ingestion pipeline extracts document text and structure, making each usable paper available to downstream domain analysis and retrieval-augmented generation. Search, parsing, and project membership are separate concerns, allowing external providers or parsers to change without coupling them to the core project workflow.

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/paper-search.png" width="100%">
    <source src="/images/project/research-agent/paper-search.webm" type="video/webm">
    Your browser does not support HTML5 video. The poster image shows the recorded workflow.
  </video>
  <figcaption>Paper search with source, date, CCF-tier, and impact-factor filters plus per-source progress.</figcaption>
</figure>

## Project-scoped Knowledge

A project is the isolation boundary for analysis. Users can create a project, search and filter its papers, and explicitly decide which documents participate in its conversations, domain tree, and knowledge graph. The interface keeps the number of papers, knowledge nodes, and relations visible so that both corpus scope and processing state remain understandable.

The same boundary is enforced on the backend: project membership controls the trusted corpus consumed by domain analysis and retrieval. Papers and prior answers from unrelated projects cannot silently enter the evidence set.

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/project-literature.png" width="100%">
    <source src="/images/project/research-agent/project-literature.webm" type="video/webm">
    Your browser does not support HTML5 video. The poster image shows the recorded workflow.
  </video>
  <figcaption>Project literature management: create a workspace, find papers, and explicitly apply the corpus used for analysis.</figcaption>
</figure>

## From Papers to Structured Knowledge

### Literature Map

The literature map turns a paper collection into a browsable research trajectory. Papers can be filtered by year and inspected through summaries, topical tags, and key claims. Each claim can be traced to supporting text, making the view useful for comparing research tasks, methods, and experimental conclusions across papers.

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/literature-map.png" width="100%">
    <source src="/images/project/research-agent/literature-map.webm" type="video/webm">
    Your browser does not support HTML5 video. The poster image shows the recorded workflow.
  </video>
  <figcaption>Literature map with year-based navigation, research facets, key claims, and supporting evidence.</figcaption>
</figure>

### Domain Tree

The domain tree summarizes the project corpus into a hierarchy of research topics while retaining links back to source chunks. Users can generate or rebuild a tree, edit and remove nodes, and inspect the original document outline and evidence for the selected topic. When no matching chunk exists, the interface reports the evidence gap instead of presenting an untraceable explanation.

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/domain-tree.png" width="100%">
    <source src="/images/project/research-agent/domain-tree.webm" type="video/webm">
    Your browser does not support HTML5 video. The poster image shows the recorded workflow.
  </video>
  <figcaption>Domain tree generation and editing with direct access to source outlines and document chunks.</figcaption>
</figure>

### Knowledge Graph

The knowledge graph organizes extracted entities, relations, and evidence into a filterable relation browser. Users can narrow results by keyword, entity type, relation type, research area, and linked paper. Relation cards expose direction, confidence, and evidence count; the detail panel provides entity attributes and source evidence. Editing controls let researchers correct automatically extracted entities and relations.

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/knowledge-graph.png" width="100%">
    <source src="/images/project/research-agent/knowledge-graph.webm" type="video/webm">
    Your browser does not support HTML5 video. The poster image shows the recorded workflow.
  </video>
  <figcaption>Knowledge-graph browsing with entity and relation filters, confidence, linked papers, and source evidence.</figcaption>
</figure>

## Evidence-grounded Research Conversations

Research conversations operate within the active project and selected-paper scope. The pipeline resolves conversational context and question constraints, retrieves candidates, assembles evidence, evaluates coverage, runs bounded follow-up retrieval when needed, composes an answer, and validates its citations. Inline citation markers connect to a side panel that displays retrieval progress, coverage, cited papers, and relevant full-text passages.

The workspace also includes research memory, global preferences, and report export for longer-running investigations. Previous answers help resolve conversational references but are never treated as factual evidence by themselves, separating conversational continuity from source reliability.

<figure>
  <video controls muted loop playsinline preload="metadata" poster="/images/project/research-agent/research-chat.png" width="100%">
    <source src="/images/project/research-agent/research-chat.webm" type="video/webm">
    Your browser does not support HTML5 video. The poster image shows the recorded workflow.
  </video>
  <figcaption>Research chat with numbered citations, retrieval coverage, paper provenance, and full-text evidence.</figcaption>
</figure>

## System Design

The architecture follows high-cohesion, low-coupling boundaries:

- **Interaction layer:** Next.js App Router structures dataset, project-knowledge, and research-chat views; React components provide reusable interactions; TypeScript defines data contracts.
- **API layer:** FastAPI routes handle validation and response mapping, with separate endpoints for papers, projects, domain trees, literature maps, settings, and background jobs.
- **Domain services:** search dispatch, PDF parsing, project scoping, document indexing, candidate retrieval, evidence assembly, and knowledge modeling each have focused responsibilities.
- **Agent orchestration:** agents coordinate research workflows and tools without owning persistence, third-party networking, or every retrieval detail.
- **Jobs and storage:** long-running parsing and knowledge-building operations run as background jobs with persisted task, conversation, project, and knowledge state, supporting status inspection, cancellation, retry, and recovery.

The main answer pipeline follows a one-way dependency flow: context → question contract → structure indexing → candidate retrieval → evidence assembly → coverage evaluation → refinement or generation → grounding validation. Explicit contracts connect the stages, and downstream components do not rewrite upstream constraints, making retrieval and model implementations easier to test and replace.

## Outcome

The project delivers an end-to-end path from discovery to reusable research knowledge. Multi-source search grows the corpus, project spaces fix its trusted boundary, literature maps and domain trees reveal macro structure, knowledge graphs expose fine-grained relations, and research conversations turn the same evidence into traceable answers. By treating project isolation, evidence coverage, and citation validation as system-level constraints, Research Agent moves beyond a general chat interface toward an inspectable, cumulative research workspace.
