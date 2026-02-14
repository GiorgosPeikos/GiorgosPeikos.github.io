---
layout: default
title: "ANTHEM: Human Centred Medicine"
one_liner: "Trustworthy health search and privacy preserving clinician in the loop retrieval, developed at UniMiB within the ANTHEM programme."
order: 1
impact: "Prototyped and evaluated healthcare AI under real constraints: privacy, low compute, expert oversight, and evidence grounded outputs."
keywords: ["healthcare AI", "conversational AI", "RAG", "health information retrieval", "clinical trials retrieval", "privacy", "evaluation", "human in the loop"]
---

<div class="card section">
  <h1>ANTHEM (UniMiB)</h1>

  <p class="muted">
    ANTHEM (AdvaNced Technologies for Human centEred Medicine) is the programme under which I have been hired as a Fixed-term Researcher (RTDA) at the University of Milano-Bicocca to build and evaluate trustworthy AI systems for healthcare.
    Programme website:
    <a href="https://fondazioneanthem.it/en/" target="_blank" rel="noreferrer">fondazioneanthem.it</a>
  </p>

<div class="card section">
  <h2>Projects within ANTHEM</h2>

  <div class="project-grid">

    <div class="project-card">
      <div class="item-title">Privacy preserving clinical trial retrieval with small LLMs</div>
      <div class="muted small">
        Uses small open source LLMs to generate effective search queries for clinical trial retrieval, designed for low compute settings and clinician oversight.
      </div>
      <div class="small" style="margin-top:8px;">
        <span class="muted">Impact:</span> Demonstrates that small models can match or exceed expert written queries while remaining practical for resource constrained deployments and expert in the loop workflows.
      </div>
      <div class="project-meta small">
        <span class="muted">Status:</span> Published
      </div>
    </div>

    <div class="project-card">
      <div class="item-title">Combining LLMs with knowledge bases for trustworthy health search</div>
      <div class="muted small">
        Extracts health related claims from documents and verifies them against a knowledge base to produce a correctness signal that complements relevance based ranking.
      </div>
      <div class="small" style="margin-top:8px;">
        <span class="muted">Impact:</span> Adds transparent trust signals by grounding correctness estimates in structured evidence rather than relying only on model judgement.
      </div>
      <div class="project-meta small">
        <span class="muted">Status:</span> Published
      </div>
    </div>

    <div class="project-card">
      <div class="item-title">Factual medical QA (RAG assistant)</div>
      <div class="muted small">
        Internal prototype conversational assistant for factual medical question answering, grounded in general knowledge plus an internal document collection, with citation first responses and reliability checks.
      </div>
      <div class="small" style="margin-top:8px;">
        <span class="muted">Impact:</span> Targets higher answer reliability by design, combining retrieval, grounded generation, and structured error analysis.
      </div>
      <div class="project-meta small">
        <span class="muted">Status:</span> Internal prototype
      </div>
    </div>

    <div class="project-card">
      <div class="item-title">Benchmark for phenotype centric medical NLP</div>
      <div class="muted small">
        Benchmark that standardises medical tasks involving phenotypes across heterogeneous inputs, including structured phenotype data and raw clinical text.
      </div>
      <div class="small" style="margin-top:8px;">
        <span class="muted">Impact:</span> Enables fast and comparable evaluation of LLMs, language models, and classical pipelines on essential tasks such as phenotype extraction, entity linking, and relation identification from text.
      </div>
      <div class="project-meta small">
        <span class="muted">Status:</span> In preparation
      </div>
    </div>

  </div>

  <h2 style="margin-top:18px;">Publications</h2>
  <div class="project-grid" style="margin-top:10px;">

    <div class="project-card">
      <div class="item-title">Privacy preserving clinical trial retrieval with small LLMs</div>
      <div class="muted small">
        Small open source LLMs for query generation under constraints of low compute and clinician oversight.
      </div>
      <div class="project-meta small">
        <span class="muted">Link:</span>
        <a href="https://ieeexplore.ieee.org/document/10973512/" target="_blank" rel="noreferrer">IEEE Xplore</a>
      </div>
    </div>

    <div class="project-card">
      <div class="item-title">Combining LLMs with knowledge bases for trustworthy health search</div>
      <div class="muted small">
        Knowledge grounded claim verification used as a correctness signal to support trustworthy ranking.
      </div>
      <div class="project-meta small">
        <span class="muted">Link:</span>
        <a href="https://link.springer.com/chapter/10.1007/978-3-031-88714-7_17" target="_blank" rel="noreferrer">Springer</a>
      </div>
    </div>

  </div>
</div>

<div class="card section">
  <h2>Acknowledgement</h2>
  <p class="small muted">
    These works were supported by the National Plan for NRRP Complementary Investments (PNC, established with the decree-law 6 May 2021, n. 59, converted by law n. 101 of 2021) in the call for the
    funding of research initiatives for technologies and innovative trajectories in the health and care sectors (Directorial Decree n. 931 of 06-06-2022), project n. PNC0000003, AdvaNced Technologies
    for Human-centrEd Medicine (ANTHEM). These works reflect only the authors’ views and opinions. Neither the Ministry for University and Research nor the European Commission can be considered
    responsible for them.
  </p>
</div>
