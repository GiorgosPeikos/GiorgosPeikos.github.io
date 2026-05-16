---
layout: default
title: Teaching
description: "Selected teaching materials in Information Retrieval, Recommender Systems, NLP, and applied AI."
permalink: /teaching/
---

<div class="card section">
  <h1>Teaching</h1>

  <p class="muted">
    Selected teaching materials from university courses, labs, tutorials, and workshops.
    Materials include lecture slides, hands-on labs, and practical student projects.
  </p>
</div>

{% assign university = site.data.teaching.university %}

<div class="card section">
  <h2>{{ university.title }}</h2>
  <p class="muted small">
    {{ university.org }} · {{ university.year }}
  </p>
  <p class="small">
    {{ university.description }}
  </p>
</div>

<div class="card section">
  <h2>Lecture Slides</h2>

  <div class="project-grid">
    {% for item in university.lectures %}
      <div class="project-card">
        <div class="item-title">{{ item.title }}</div>
        <div class="muted small" style="margin-top:6px;">{{ item.description }}</div>
        <div class="project-meta small">
          <span class="muted">Material year:</span> {{ university.materials_year }}
          <span class="muted" style="margin-left:10px;">Link:</span>
          <a href="{{ item.file | relative_url }}" target="_blank" rel="noreferrer">Slides</a>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<div class="card section">
  <h2>Labs</h2>

  <div class="project-grid">
    {% for item in university.labs %}
      <div class="project-card">
        <div class="item-title">{{ item.title }}</div>
        <div class="muted small" style="margin-top:6px;">{{ item.description }}</div>
        <div class="project-meta small">
          <span class="muted">Material year:</span> {{ university.materials_year }}
          <span class="muted" style="margin-left:10px;">Link:</span>
          <a href="{{ item.file | relative_url }}" target="_blank" rel="noreferrer">Lab</a>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<div class="card section">
  <h2>Student Projects</h2>
  <p class="muted small">
    Practical IR problems developed for students to solve as part of the Information Retrieval and Recommender Systems course.
  </p>

  <div class="project-grid">
    {% for item in university.projects %}
      <div class="project-card">
        <div class="item-title">{{ item.title }}</div>
        <div class="muted small" style="margin-top:6px;">{{ item.description }}</div>
        <div class="project-meta small">
          <span class="muted">Material year:</span> {{ university.materials_year }}
          <span class="muted" style="margin-left:10px;">Link:</span>
          <a href="{{ item.file | relative_url }}" target="_blank" rel="noreferrer">Project description</a>
        </div>
      </div>
    {% endfor %}
  </div>
</div>
