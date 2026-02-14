---
layout: default
title: Projects
description: "Selected projects in RAG, conversational search, evaluation, and domain specific AI systems."
permalink: /projects/
---

<div class="card section">
  <h1>Projects</h1>

  <p class="muted">
    A curated set of projects that demonstrate what I build, how I evaluate it, and how it is used.
    Each page includes the problem context, my contributions, and links to supporting artifacts when available.
  </p>

  <div class="small" style="margin-top:14px;">
    {% assign sorted = site.projects | default: empty | sort: "order" %}

    {% if sorted.size == 0 %}
      <div class="muted small">
        No projects found. If you are using a <code>_projects/</code> collection, ensure it is enabled in <code>_config.yml</code> and each project has an <code>order</code> field.
      </div>
    {% endif %}

    {% for pr in sorted %}
      <div class="item">
        <div class="item-title">
          <a href="{{ pr.url }}">{{ pr.title }}</a>
        </div>

        {% if pr.one_liner %}
          <div class="muted small">{{ pr.one_liner }}</div>
        {% endif %}

        {% if pr.keywords and pr.keywords.size > 0 %}
          <div class="small" style="margin-top:6px;">
            <span class="muted">Keywords:</span> {{ pr.keywords | join: ", " }}
          </div>
        {% endif %}
      </div>
    {% endfor %}
  </div>
</div>
