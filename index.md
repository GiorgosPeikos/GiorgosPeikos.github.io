---
layout: default
---

<div id="top" class="card hero">
  <div class="avatar">
    <img src="/assets/img/profile.png" alt="Profile photo" onerror="this.style.display='none'; this.parentElement.innerHTML='<div style=&quot;padding:14px&quot; class=&quot;muted small&quot;>Add assets/img/profile.png</div>';">
  </div>
  <div>
    <h1>Georgios Peikos</h1>
    <div class="muted">
      Search and NLP Researcher (RTDA), University of Milano Bicocca · ex Marie Curie ESR (DoSSIER)
    </div>
    <div class="pills">
      {% for s in site.data.social.links %}
      <a class="pill" href="{{ s.url }}" target="_blank" rel="noreferrer">{{ s.label }}</a>
      {% endfor %}
      <a class="pill" href="/assets/cv/Georgios_Peikos_CV.pdf" target="_blank" rel="noreferrer">CV (PDF)</a>
    </div>
    <div class="muted small" style="margin-top:10px;">
      Focus: LLMs, Retrieval Augmented Generation, semantic search, ranking, and evaluation.
    </div>
  </div>
</div>

<div id="about" class="card section">
  <h2>About</h2>
  <p>
    I work on AI for Natural Language Processing, with a focus on LLM based systems and Retrieval Augmented Generation.
    I design and evaluate end to end pipelines that combine retrieval, ranking, and generation for real user tasks.
  </p>
</div>

<div id="focus" class="card section">
  <h2>Focus</h2>
  <ul class="small">
    <li>RAG pipelines: retrieval, reranking, query understanding, context construction</li>
    <li>Semantic search and conversational search</li>
    <li>Evaluation: offline metrics, user oriented evaluation, error analysis</li>
    <li>Applications in professional domains (for example healthcare)</li>
  </ul>
</div>

<div id="projects" class="card section">
  <h2>Projects</h2>

  <p class="muted small">
    Selected work that highlights what I build and how I evaluate it. See the full list for additional projects and details.
  </p>

  {% assign featured = site.projects | default: empty | sort: "order" %}

  {% if featured.size == 0 %}
    <div class="muted small" style="margin-top:10px;">
      No projects found. Ensure the <code>projects</code> collection is enabled in <code>_config.yml</code>.
    </div>
  {% endif %}

  <div class="project-grid">
    {% for pr in featured limit:3 %}
      <div class="project-card">
        <div class="item-title">
          <a href="{{ pr.url }}">{{ pr.title }}</a>
        </div>

        {% if pr.one_liner %}
          <div class="muted small">{{ pr.one_liner }}</div>
        {% endif %}

        {% if pr.impact %}
          <div class="small" style="margin-top:8px;">
            <span class="muted">Impact:</span> {{ pr.impact }}
          </div>
        {% endif %}

        {% if pr.keywords and pr.keywords.size > 0 %}
          <div class="project-meta small">
            <span class="muted">Keywords:</span> {{ pr.keywords | join: ", " }}
          </div>
        {% endif %}
      </div>
    {% endfor %}
  </div>

  <div class="small" style="margin-top:10px;">
    <a href="/projects/">View all projects</a>
  </div>
</div>

<div id="publications" class="card section">
  <h2>Publications</h2>
  <p class="muted small">
    Full list: <a href="https://scholar.google.com/citations?user=-0ObuR0AAAAJ&hl=en" target="_blank" rel="noreferrer">Google Scholar</a>
  </p>

  {% assign left = site.data.publications.most_recent %}
  {% assign right = site.data.publications.top_cited %}

  <div class="pub-table">
    <div class="pub-head">
      <div class="pub-hcell"><h3>Most recent</h3></div>
      <div class="pub-hcell"><h3>Most influential</h3></div>
    </div>

    {% for i in (0..2) %}
      {% assign lpub = left[i] %}
      {% assign rpub = right[i] %}

      <div class="pub-row">
        <div class="pub-cell">
          {% if lpub %}
            <div class="item">
              <div class="item-title">{{ lpub.title }}</div>

              {% if lpub.impact %}
                <div class="muted small item-meta">{{ lpub.impact }}</div>
              {% else %}
                <div class="muted small item-meta">{{ lpub.authors }} · {{ lpub.venue }} · {{ lpub.year }}</div>
              {% endif %}

              <div class="small">
                {% for l in lpub.links %}
                  <a href="{{ l.url }}" target="_blank" rel="noreferrer">{{ l.label }}</a>{% unless forloop.last %} · {% endunless %}
                {% endfor %}
              </div>
            </div>
          {% endif %}
        </div>

        <div class="pub-cell">
          {% if rpub %}
            <div class="item">
              <div class="item-title">{{ rpub.title }}</div>

              {% if rpub.impact %}
                <div class="muted small item-meta">{{ rpub.impact }}</div>
              {% else %}
                <div class="muted small item-meta">{{ rpub.authors }} · {{ rpub.venue }} · {{ rpub.year }}</div>
              {% endif %}

              <div class="small">
                {% for l in rpub.links %}
                  <a href="{{ l.url }}" target="_blank" rel="noreferrer">{{ l.label }}</a>{% unless forloop.last %} · {% endunless %}
                {% endfor %}
              </div>
            </div>
          {% endif %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>


<div id="teaching" class="card section">
  <h2>Teaching</h2>
  {% for t in site.data.teaching.items %}
  <div class="item">
    <div class="item-title">{{ t.title }}</div>
    <div class="muted small">{{ t.org }} · {{ t.year }}</div>
    {% if t.notes %}<div class="small">{{ t.notes }}</div>{% endif %}
  </div>
  {% endfor %}
</div>

<div id="cv" class="card section">
  <h2>CV</h2>
  <p class="small"><a href="/assets/cv/Georgios_Peikos_CV.pdf" target="_blank" rel="noreferrer">Download CV (PDF)</a></p>
</div>

<div id="contact" class="card section">
  <h2>Contact</h2>
  <p class="small">
    LinkedIn is the best contact channel: <a href="https://www.linkedin.com/in/peikosgeorgios/" target="_blank" rel="noreferrer">/in/peikosgeorgios</a>
  </p>
</div>
