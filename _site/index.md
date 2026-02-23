---
layout: default
---

<div id="top" class="card hero">
    <div class="avatar">
      <img
        src="/assets/img/profile.png"
        alt="Profile photo"
        width="120"
        height="120"
        decoding="async"
        fetchpriority="high"
        onerror="this.style.display='none'; this.parentElement.innerHTML='<div style=&quot;padding:14px&quot; class=&quot;muted small&quot;>Add assets/img/profile.png</div>';"
      >
    </div>
  <div>
    <h1>Georgios Peikos</h1>
    <div class="muted">
      Search and NLP Researcher (RTDA), University of Milano Bicocca · ex Marie Curie ESR (DoSSIER)
    </div>

    <div class="pills">
      {% for s in site.data.social.links %}
        {% if s.label == "Email" %}
          <a class="pill" id="email-pill" href="{{ s.url }}">{{ s.label }}</a>
        {% else %}
          <a class="pill" href="{{ s.url }}" target="_blank" rel="noreferrer">{{ s.label }}</a>
        {% endif %}
      {% endfor %}
      <a class="pill" href="/assets/cv/Georgios_Peikos_CV.pdf" target="_blank" rel="noreferrer">CV (PDF)</a>
    </div>

    <div class="muted small" style="margin-top:10px;">
       <span class="accent-strong">Focus <span>·</span> </span> LLMs, Retrieval Augmented Generation, Semantic Search, Ranking and Evaluation.
    </div>
  </div>
</div>

<div id="about" class="card section">
  <h2>About</h2>

  <p>
    I am a Search and NLP Researcher at the University of Milano-Bicocca, mainly working on <span class="accent-strong">trustworthy AI</span> systems for <span 
class="accent-strong">healthcare</span> within the ANTHEM programme.
  </p>

  <p>
    My core expertise is <span class="accent-strong">Information Retrieval</span> and <span class="accent-strong">NLP</span>, with a focus on <span class="accent-strong">LLM-based systems</span> 
and <span class="accent-strong">Retrieval Augmented Generation</span>.
  </p>

  <p>
    I <span class="accent-strong">build</span> end-to-end pipelines that combine <span class="accent-strong">retrieval</span>, <span class="accent-strong">ranking</span>, and <span class="accent-strong">generation</span> for <span class="accent-strong">domain-specific search</span>.
    System design is guided by user tasks and real-world constraints such as <span class="accent-strong">evidence grounding</span>, <span class="accent-strong">privacy</span>, and <span class="accent-strong">efficiency</span>.
  </p>

  <p>
    I also <span class="accent-strong">teach</span> <span class="accent-strong">Information Retrieval</span> and <span class="accent-strong">Recommender Systems</span> at Bachelor’s and Master’s 
level,
with an emphasis on evaluation and practical system building.
  </p>

  <p>
   I am open to collaborations that combine applied research and development of search and LLM-based systems, particularly in professional domains such as healthcare, enterprise, and legal.
   I am also open to projects that match the technical directions and practical focus reflected in my projects. </p>
</div>

<div id="focus" class="card section">
  <h2>Focus</h2>
  <ul class="small">
    <li><span class="accent-strong">RAG pipelines</span>: retrieval, reranking, query understanding, and context construction</li>
    <li><span class="accent-strong">Large Language Models</span>: training, fine-tuning, context understanding, and generation</li>
    <li><span class="accent-strong">(LLM/IR) System Evaluation</span> and system diagnostics: offline metrics, error analysis, and user-oriented evaluation</li>
    <li><span class="accent-strong">Trustworthy AI</span> constraints: evidence-grounded outputs, privacy, efficiency, and expert oversight</li>
  </ul>
</div>

<div id="projects" class="card section">
  <h2>Programmes & Projects</h2>

  <p class="muted small">
  Selected programmes and projects showing how I build and evaluate retrieval and NLP systems, with clear scope, my contributions, and links to code, papers, and prototypes when available.
  </p>

  {% assign featured = site.projects | default: empty | sort: "order" %}

  {% if featured.size == 0 %}
    <div class="muted small" style="margin-top:10px;">
      No projects found. Ensure the <code>projects</code> collection is enabled in <code>_config.yml</code>.
    </div>
  {% endif %}

  <div class="project-grid">
    {% for pr in featured limit:4 %}
      <div class="project-card">
        <div class="item-title">
          <a href="{{ pr.url }}">{{ pr.title }}</a>
        </div>

        <div class="small" style="margin-top:6px;">
          {% if pr.type %}
            <span class="pill pill-type-{{ pr.type }}">{{ pr.type | replace: "_", " " | capitalize }}</span>
          {% endif %}

          {% if pr.status %}
            <span class="pill pill-status-{{ pr.status }}">{{ pr.status | replace: "_", " " | capitalize }}</span>
          {% endif %}

          {% if pr.context and pr.context.size > 0 %}
            {% for c in pr.context %}
              <span class="pill pill-context-{{ c }}">{{ c | replace: "_", " " | capitalize }}</span>
            {% endfor %}
          {% endif %}
        </div>

        {% if pr.one_liner %}
          <div class="muted small" style="margin-top:8px;">{{ pr.one_liner }}</div>
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
  <h2>Selected Publications</h2>
  <p class="muted small">
    Selected publications (most recent and most cited). Full list available on <a href="https://scholar.google.com/citations?user=-0ObuR0AAAAJ&hl=en" target="_blank" rel="noreferrer">Google 
Scholar</a>.
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
        <div class="pub-label">Recent Publication</div>
        {% if lpub %}
          <div class="item">
            <div class="item-title">{{ lpub.title }}</div>

            {% if lpub.impact %}
              <div class="muted small item-meta">{{ lpub.impact }}</div>
            {% else %}
              <div class="muted small item-meta">{{ lpub.authors }} · {{ lpub.venue }} · {{ lpub.year }}</div>
            {% endif %}

            <div class="small">
              <span class="muted">Link:</span>
              {% for l in lpub.links %}
                <a href="{{ l.url }}" target="_blank" rel="noreferrer">{{ l.label }}</a>{% unless forloop.last %} · {% endunless %}
              {% endfor %}
            </div>
          </div>
        {% else %}
          <div class="muted small">No entry.</div>
        {% endif %}
      </div>

      <div class="pub-cell">
        <div class="pub-label">Influential Publication</div>
        {% if rpub %}
          <div class="item">
            <div class="item-title">{{ rpub.title }}</div>

            {% if rpub.impact %}
              <div class="muted small item-meta">{{ rpub.impact }}</div>
            {% else %}
              <div class="muted small item-meta">{{ rpub.authors }} · {{ rpub.venue }} · {{ rpub.year }}</div>
            {% endif %}

            <div class="small">
              <span class="muted">Link:</span>
              {% for l in rpub.links %}
                <a href="{{ l.url }}" target="_blank" rel="noreferrer">{{ l.label }}</a>{% unless forloop.last %} · {% endunless %}
              {% endfor %}
            </div>
          </div>
        {% else %}
          <div class="muted small">No entry.</div>
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