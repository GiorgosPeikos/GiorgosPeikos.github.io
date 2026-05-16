---
layout: default
title: Tutorials & Workshops
description: "Selected external tutorials and workshops in NLP, Information Retrieval, and applied AI."
permalink: /tutorials/
---

{% assign external = site.data.teaching.external %}

<div id="external-tutorials-workshops" class="card section">
  <h1>{{ external.title }}</h1>

  <p class="muted">
    {{ external.description }}
  </p>

  {% if external.items and external.items.size > 0 %}
  <div class="project-grid">
    {% for item in external.items %}
      <div class="project-card">
        <div class="item-title">{{ item.title }}</div>
        <div class="muted small" style="margin-top:6px;">{{ item.org }} · {{ item.year }}</div>
        {% if item.description %}
          <div class="small" style="margin-top:6px;">{{ item.description }}</div>
        {% endif %}
        {% if item.links and item.links.size > 0 %}
          <div class="project-meta small">
            <span class="muted">Links:</span>
            {% for link in item.links %}
              <a href="{{ link.url | relative_url }}" target="_blank" rel="noreferrer">{{ link.label }}</a>{% unless forloop.last %} · {% endunless %}
            {% endfor %}
          </div>
        {% endif %}
      </div>
    {% endfor %}
  </div>
  {% else %}
    <p class="small">
      Selected tutorial and workshop materials will be added here.
    </p>
  {% endif %}
</div>
