---
layout: default
title: Projects
description: "Selected projects in RAG, conversational search, evaluation, and domain specific AI systems."
permalink: /projects/
---

<div class="card section">
  <h1>Projects</h1>
  <p class="muted">
    A curated list of work that shows what I build, how I evaluate it, and where it is used.
    For each project, I provide a short problem statement, my contributions, and links to artifacts.
  </p>

  <div class="small" style="margin-top:14px;">
    {% assign sorted = site.projects | sort: "order" %}
    {% for pr in sorted %}
      <div class="item">
        <div class="item-title"><a href="{{ pr.url }}">{{ pr.title }}</a></div>
        {% if pr.one_liner %}<div class="muted small">{{ pr.one_liner }}</div>{% endif %}
        <div class="small" style="margin-top:6px;">
          {% if pr.keywords %}<span class="muted">Keywords:</span> {{ pr.keywords | join: ", " }}{% endif %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>
