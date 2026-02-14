---
layout: default
title: "ANTHEM: Human Centred Medicine"
one_liner: "Trustworthy health search and privacy preserving clinician in the loop retrieval, developed at UniMiB within the ANTHEM programme."
order: 1
keywords: ["healthcare AI", "conversational AI", "RAG", "health information retrieval", "clinical trials retrieval", "privacy", "evaluation", "human in the loop"]
---

<div class="card section">
  <h1>ANTHEM (UniMiB)</h1>
  <p class="muted">
    ANTHEM is the programme under which I have been hired at the University of Milano Bicocca to build and evaluate trustworthy AI systems for healthcare.
  </p>

  <h2>Programme</h2>
  <p class="small">
    ANTHEM stands for AdvaNced Technologies for Human centEred Medicine.
    Programme website:
    <a href="https://fondazioneanthem.it/en/" target="_blank" rel="noreferrer">fondazioneanthem.it</a>
  </p>

  <h2>Projects within ANTHEM</h2>
  <p class="muted small">
    A set of research and engineering projects aligned with ANTHEM. Each item includes a one line description, one line impact, and a publication link when available.
  </p>

  <div class="small" style="margin-top:12px;">

    <div class="item">
      <div class="item-title">Privacy preserving clinical trial retrieval with small LLMs</div>
      <div class="muted small">
        Uses small open source LLMs to generate effective search queries for clinical trial retrieval, designed for low compute settings and clinician oversight.
      </div>
      <div class="small" style="margin-top:6px;">
        <span class="muted">Impact:</span> Demonstrates that small models can match or exceed expert written queries while remaining practical for resource constrained deployments and expert in the loop workflows.
      </div>
      <div class="small" style="margin-top:6px;">
        <span class="muted">Publication:</span>
        <a href="https://ieeexplore.ieee.org/document/10973512/" target="_blank" rel="noreferrer">IEEE Xplore</a>
      </div>
    </div>

    <div class="item">
      <div class="item-title">Trust aware health search (fact driven ranking)</div>
      <div class="muted small">
        Ranks health web documents using both relevance and a correctness signal derived from knowledge graph grounded claim verification.
      </div>
      <div class="small" style="margin-top:6px;">
        <span class="muted">Impact:</span> Adds transparent trust signals that complement LLM only fact checking by grounding assessments in structured evidence.
      </div>
      <div class="small" style="margin-top:6px;">
        <span class="muted">Publication:</span>
        <a href="https://link.springer.com/chapter/10.1007/978-3-031-88714-7_17" target="_blank" rel="noreferrer">Springer</a>
      </div>
    </div>

    <div class="item">
      <div class="item-title">Factual medical QA (RAG assistant)</div>
      <div class="muted small">
        Internal prototype conversational assistant for factual medical question answering, grounded in general knowledge plus an internal document collection, with citation first responses and reliability checks.
      </div>
      <div class="small" style="margin-top:6px;">
        <span class="muted">Impact:</span> Targets higher answer reliability by design, combining retrieval, grounded generation, and structured error analysis.
      </div>
      <div class="small" style="margin-top:6px;">
        <span class="muted">Status:</span> Internal prototype
      </div>
    </div>

    <div class="item">
      <div class="item-title">Benchmark across genotype, phenotype, and clinical text</div>
      <div class="muted small">
        Benchmark and evaluation framework to compare systems across structured signals (genotype and phenotype) and unstructured clinical narratives.
      </div>
      <div class="small" style="margin-top:6px;">
        <span class="muted">Impact:</span> Enables comparable and reproducible evaluation across heterogeneous clinical inputs, supporting faster iteration and clearer progress tracking.
      </div>
      <div class="small" style="margin-top:6px;">
        <span class="muted">Status:</span> In preparation
      </div>
    </div>

  </div>

  <h2>Acknowledgement</h2>
  <p class="small muted">
    These works were supported by the National Plan for NRRP Complementary Investments (PNC, established with the decree-law 6 May 2021, n. 59, converted by law n. 101 of 2021) in the call for the funding of research initiatives for technologies and innovative trajectories in the health and care sectors (Directorial Decree n. 931 of 06-06-2022), project n. PNC0000003, AdvaNced Technologies for Human-centrEd Medicine (ANTHEM). This work reflects only the authors’ views and opinions. Neither the Ministry for University and Research nor the European Commission can be considered responsible for them.
  </p>
</div>
