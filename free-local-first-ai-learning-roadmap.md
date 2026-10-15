# Free, Local-First AI Learning Roadmap

This 12-week plan uses free learning resources and open-source/local tooling. You do not need paid model APIs: run models locally with [Ollama](https://ollama.com/) and use public or sanitized sample data.

## Week 0 — Set up your lab

**Focus:** Create a repeatable local environment.

- Install [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/downloads), [Ollama](https://ollama.com/), and [Docker](https://docs.docker.com/get-started/).
- Create one Git repository for all exercises and a `learning-journal.md` file.

**Deliverable:** A local model responds from the command line; your repository documents the setup.

## Weeks 1–2 — LLM fundamentals

**Focus:** Tokens, prompts, context, structured output, embeddings, inference, and model limitations.

- Study the [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1).
- Read the [Ollama API documentation](https://docs.ollama.com/api).
- Learn data validation using [Pydantic](https://docs.pydantic.dev/).

**Build:** A local CLI that turns a bug report into validated JSON containing `summary`, `affected_component`, `severity`, `likely_cause`, and `questions_to_ask`.

**Success criterion:** Code rejects invalid JSON rather than silently accepting it.

## Week 3 — Build a basic AI application

**Focus:** Expose a local model through an API and simple user interface.

- Follow the [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/).
- Use [Streamlit](https://docs.streamlit.io/) or [Gradio](https://www.gradio.app/guides/quickstart).

**Build:** A local test-case drafting assistant that accepts an acceptance criterion and returns structured test ideas.

**Success criterion:** Output follows a fixed schema and is reviewed by a human before use.

## Weeks 4–5 — RAG fundamentals

**Focus:** Document ingestion, chunking, embeddings, metadata, retrieval, grounding, and citations.

- Read [Sentence Transformers documentation](https://www.sbert.net/).
- Use [Chroma](https://docs.trychroma.com/) for a lightweight local vector store or [Qdrant](https://qdrant.tech/documentation/) for a more production-like option.
- Study the [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit1/introduction), including its agentic-RAG material.

**Build:** A RAG assistant over public API documentation or non-sensitive Markdown notes.

**Success criterion:** Every answer names its source file/chunk and declines answers when retrieval is weak.

## Week 6 — RAG evaluation

**Focus:** Measure retrieval and answer quality instead of trusting a demo.

- Learn evaluation concepts from [OpenAI Evals](https://developers.openai.com/learn/evals); the principles apply to local models too.
- Explore [Ragas](https://docs.ragas.io/) and [Promptfoo](https://www.promptfoo.dev/docs/intro/).

**Build:** A version-controlled set of 30–50 questions with expected sources and answer characteristics.

**Success criterion:** Track retrieval recall, citation correctness, unsupported-claim rate, latency, and failure examples.

## Week 7 — Tool calling and controlled workflows

**Focus:** Give an LLM narrow, safe abilities through deterministic tools.

- Read [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents).
- Study the [Model Context Protocol](https://modelcontextprotocol.io/) and [OpenAI Agents guide](https://developers.openai.com/api/docs/guides/agents).

**Build:** A read-only CI-log investigator that searches test logs, inspects reports, and retrieves known failures.

**Success criterion:** Tool arguments are schema-validated and no tool can modify files, contact production systems, or expose secrets.

## Week 8 — Agent fundamentals

**Focus:** Planning, state, retries, stopping conditions, and human approval.

- Continue the [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit2/smolagents/introduction).
- Implement one workflow in plain Python first; then optionally explore [LangGraph](https://langchain-ai.github.io/langgraph/) or [LlamaIndex](https://docs.llamaindex.ai/).

**Build:** A workflow that turns a failed test run into a triage report: failure cluster, evidence, likely cause, and next diagnostic action.

**Success criterion:** It has a maximum-step limit, timeout, explicit stop state, and human review before action.

## Week 9 — AI for test automation

**Focus:** Turn requirements into high-quality, traceable test assets.

- Learn [pytest](https://docs.pytest.org/) and [Playwright](https://playwright.dev/docs/intro).
- For API testing, explore [REST Assured](https://rest-assured.io/) or [Karate](https://docs.karatelabs.io/).

**Build:** A requirement-to-test-case assistant that drafts positive, negative, boundary, security, and error-path cases.

**Success criterion:** Every case maps to an acceptance criterion; only human-approved cases become executable tests.

## Week 10 — AI for performance testing

**Focus:** Use AI to explain measured results, never to invent measurements.

- Learn [k6](https://grafana.com/docs/k6/latest/), [Locust](https://docs.locust.io/), and [Grafana](https://grafana.com/docs/grafana/latest/).

**Build:** A performance-report assistant that compares two k6 or Locust result files.

**Success criterion:** Conventional code calculates p95, error rate, throughput, and regression thresholds; the model only explains evidence-backed findings.

## Week 11 — Security, safety, and quality gates

**Focus:** Prompt injection, sensitive data, over-permissioned tools, hallucinations, auditability, and rollback.

- Read the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/).
- Review [Promptfoo red teaming](https://www.promptfoo.dev/docs/red-team/) and [evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

**Build:** Adversarial tests for malicious instructions in documents, fabricated citations, secret-like text, unsafe tool calls, and ambiguous requests.

**Success criterion:** Known attacks fail safely and remain in the regression suite.

## Week 12 — Integrate into a safe SDLC flow

**Focus:** Make AI changes repeatable, reviewable, and measurable.

- Learn [GitHub Actions](https://docs.github.com/en/actions) and [pre-commit](https://pre-commit.com/).
- Follow practical developments through the [GitHub AI & ML blog](https://github.blog/ai-and-ml/generative-ai/).

**Build:** CI that runs formatters, unit tests, RAG/agent evaluations, and security regressions whenever prompts, retrieval settings, tools, or model settings change.

**Success criterion:** A change is promoted only when it meets pre-agreed evaluation thresholds.

## Long-term routine

- **Weekly:** 30 minutes for official releases; 60 minutes reproducing one idea locally; 30 minutes recording capability, use case, risk, evaluation result, and decision.
- **Monthly:** Rerun your benchmark against one new local model or pipeline change.
- **First projects:** Begin with an engineering-documentation RAG assistant and a read-only test-failure triage assistant.

## Guardrails

Keep production permissions, release decisions, secrets, numeric calculations, and policy checks outside the model. Use deterministic code for measurements and validation; use the model for synthesis, ambiguity, and drafting.
