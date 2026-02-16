---
layout: default
title: Projects
description: "Selected projects in RAG, conversational search, evaluation, and domain specific AI systems."
permalink: /projects/
---

<div class="card section">
  <h1>Projects</h1>

  <p class="muted">
    A curated set of projects that show what I build, how I evaluate it, and how it is used.
    Each page includes context, my contributions, and supporting artifacts when publicly available.
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

        <div class="small" style="margin-top:6px;">
          {% if pr.status %}
            <span class="pill pill-status-{{ pr.status }}">{{ pr.status | replace: "_", " " | capitalize }}</span>
          {% endif %}

          {% if pr.type %}
            <span class="pill pill-type-{{ pr.type }}">{{ pr.type | replace: "_", " " | capitalize }}</span>
          {% endif %}

          {% if pr.context and pr.context.size > 0 %}
            {% for c in pr.context %}
              <span class="pill pill-context-{{ c }}">{{ c | replace: "_", " " | capitalize }}</span>
            {% endfor %}
          {% endif %}
        </div>

        {% if pr.one_liner %}
          <div class="muted small" style="margin-top:6px;">{{ pr.one_liner }}</div>
        {% endif %}

        {% if pr.impact %}
          <div class="small" style="margin-top:6px;">
            <span class="muted">Impact:</span> {{ pr.impact }}
          </div>
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
