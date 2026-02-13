---
layout: default
---

<div id="top" class="card hero">
  <div class="avatar">
    <img src="/assets/img/profile.jpg" alt="Profile photo" onerror="this.style.display='none'; this.parentElement.innerHTML='<div style=&quot;padding:14px&quot; class=&quot;muted small&quot;>Add assets/img/profile.jpg</div>';">
  </div>
  <div>
    <h1>Giorgos Peikos</h1>
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

<div id="publications" class="card section">
  <h2>Publications</h2>
  <p class="muted small">
    Full list: <a href="https://scholar.google.com/citations?user=-0ObuR0AAAAJ&hl=en" target="_blank" rel="noreferrer">Google Scholar</a>
  </p>

  <h3 style="margin:12px 0 6px 0;">Top cited</h3>
  {% for pub in site.data.publications.top_cited %}
  <div class="item">
    <div class="item-title">{{ pub.title }}</div>
    <div class="muted small item-meta">{{ pub.authors }} · {{ pub.venue }} · {{ pub.year }} · Cited by {{ pub.citations }}</div>
    <div class="small">
      {% for l in pub.links %}
        <a href="{{ l.url }}" target="_blank" rel="noreferrer">{{ l.label }}</a>{% unless forloop.last %} · {% endunless %}
      {% endfor %}
    </div>
  </div>
  {% endfor %}

  <h3 style="margin:14px 0 6px 0;">Most recent</h3>
  {% for pub in site.data.publications.most_recent %}
  <div class="item">
    <div class="item-title">{{ pub.title }}</div>
    <div class="muted small item-meta">{{ pub.authors }} · {{ pub.venue }} · {{ pub.year }}</div>
    <div class="small">
      {% for l in pub.links %}
        <a href="{{ l.url }}" target="_blank" rel="noreferrer">{{ l.label }}</a>{% unless forloop.last %} · {% endunless %}
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>

<div id="projects" class="card section">
  <h2>Projects</h2>
  {% for pr in site.data.projects.items %}
  <div class="item">
    <div class="item-title">{{ pr.title }}</div>
    <div class="muted small">{{ pr.one_liner }}</div>
  </div>
  {% endfor %}
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
