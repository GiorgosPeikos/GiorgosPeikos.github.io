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

  <div class="small">
    <p>
      I am an <span class="accent-strong">Applied AI Engineer</span> and
      <span class="accent-strong">Search/NLP Researcher</span> at the University of Milano-Bicocca,
      with a background in <span class="accent-strong">Electrical and Computer Engineering</span>.
      My work focuses on <span class="accent-strong">Large Language Models</span>,
      <span class="accent-strong">Retrieval Augmented Generation</span>, and
      <span class="accent-strong">Information Retrieval</span>, with applications in
      <span class="accent-strong">healthcare</span> and other high reliability domains.
    </p>

    <p>
      I design and deploy <span class="accent-strong">end-to-end AI systems</span> that combine
      <span class="accent-strong">data pipelines</span>, <span class="accent-strong">semantic retrieval</span>,
      <span class="accent-strong">reranking</span>, <span class="accent-strong">model training</span>,
      <span class="accent-strong">inference</span>, and <span class="accent-strong">evaluation</span>.
      My recent work includes evidence-grounded RAG systems, conversational search, clinical trial retrieval,
      and trustworthy AI workflows.
    </p>

    <p>
      I have experience training and adapting small and mid-scale language models, including
      <span class="accent-strong">1B-7B parameter models</span>, using
      <span class="accent-strong">PyTorch DDP</span> on
      <span class="accent-strong">Slurm-managed HPC infrastructure</span>.
      System design is guided by real-world constraints such as
      <span class="accent-strong">evidence grounding</span>, <span class="accent-strong">privacy</span>,
      <span class="accent-strong">efficiency</span>, and expert oversight.
    </p>

    <p>
      I also <span class="accent-strong">teach</span> <span class="accent-strong">Information Retrieval</span> and
      <span class="accent-strong">Recommender Systems</span> at Bachelor’s and Master’s level, with an emphasis on
      evaluation and practical system building.
    </p>

    <p>
      I am open to collaborations and technical roles involving the design and evaluation of
      <span class="accent-strong">applied AI systems</span>, particularly in
      <span class="accent-strong">healthcare</span>, <span class="accent-strong">enterprise search</span>,
      <span class="accent-strong">legal search</span>, and other domains where reliability, grounding,
      and evaluation matter.
    </p>
  </div>
</div>

<div id="focus" class="card section">
  <h2>Focus</h2>

  <div class="item">
    <div class="small">
      <span class="accent-strong">RAG pipelines</span>: retrieval, reranking, query understanding, and context construction
    </div>
  </div>

  <div class="item">
    <div class="small">
      <span class="accent-strong">Large Language Models</span>: training, fine-tuning, context understanding, and generation
    </div>
  </div>

  <div class="item">
    <div class="small">
      <span class="accent-strong">(LLM/IR) System Evaluation</span> and system diagnostics: offline metrics, error analysis, and user-oriented evaluation
    </div>
  </div>

  <div class="item">
    <div class="small">
      <span class="accent-strong">Trustworthy AI</span> constraints: evidence grounding, privacy, efficiency, and expert oversight
    </div>
  </div>
</div>

<div id="projects" class="card section">
  <h2>Programmes & Projects</h2>

  <p class="muted small">
  Selected work showing how I design, build, and evaluate retrieval, NLP, and applied AI systems, with links to code, papers, and prototypes where available.
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
  <p class="small">
    I teach <span class="accent-strong">Information Retrieval</span> and
    <span class="accent-strong">Recommender Systems</span> at the University of Milano-Bicocca,
    with a focus on evaluation, retrieval models, modern search systems, and practical system building.
  </p>

  <div class="small" style="margin-top:10px;">
    <a href="/teaching/">View teaching materials</a>
  </div>
</div>

<div id="tutorials" class="card section">
  <h2>External Tutorials & Workshops</h2>
  <p class="small">
    I also deliver external tutorials and workshops on
    <span class="accent-strong">NLP</span>, <span class="accent-strong">Information Retrieval</span>,
    and applied AI topics for research schools and professional audiences.
  </p>

  <div class="small" style="margin-top:10px;">
    <a href="/tutorials/">View tutorial and workshop materials</a>
  </div>
</div>

[//]: # (<div id="cv" class="card section">)

[//]: # (  <h2>CV</h2>)

[//]: # (  <p class="small"><a href="/assets/cv/Georgios_Peikos_CV.pdf" target="_blank" rel="noreferrer">Download CV &#40;PDF&#41;</a></p>)

[//]: # (</div>)

<div id="contact" class="card section">
  <h2>Contact</h2>
  <p class="small">
    If you would like to discuss collaborations, research, or applied AI projects, you can reach me on LinkedIn:
    <a href="https://www.linkedin.com/in/peikosgeorgios/" target="_blank" rel="noreferrer">/in/peikosgeorgios</a>
  </p>
  <p class="small">
    <span class="accent-strong">Final Note</span> I would like to thank all the people who have accompanied me during the activities presented above and, over the years, have shaped how I think and work.
  </p>
</div>
