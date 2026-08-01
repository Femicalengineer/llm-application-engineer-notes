# Table of Contents — LLM Application Engineer Curriculum

Full section-by-section index of every notebook in this folder, with a relevance score against the job target: **LLM Application Engineer**.

## How to read the relevance scores

- **1–5 scale**, scored against "would an LLM Application Engineer actually use or be expected to know this day-to-day / in an interview for this specific role."
- The three **theory notebooks** (`000a`/`000b`/`000c`) are scored **per section**, since they deliberately mix core-skill material with ML-research/training-infra material that's more interview trivia than daily-use skill for this role.
- The **applied notebooks** (`001`–`011`) are scored **once per notebook**, since each was purpose-built around a specific App Engineer skill and is internally consistent — the score applies to the whole notebook.
- A score reflects *job relevance*, not quality — a 2/5 section can still be well-built and worth knowing for interviews; it just isn't something this role does hands-on.

| Score | Meaning |
|---|---|
| 5 | Core, hands-on skill for this exact role — expect to use this regularly |
| 4 | Very useful, either hands-on in adjacent situations or a strong architectural-decision input |
| 3 | Good context/mental model, occasional practical use, not a daily tool |
| 2 | Mostly interview/trivia value — ML research or infra territory outside this role's usual scope |
| 1 | Background knowledge only |

---

## Quick reference — applied notebooks (001–011)

| # | Notebook | Core topic | Relevance |
|---|---|---|---|
| 001 | Build_Smarter_AI_Apps_LangChain_Anthropic_modern | LangChain/Anthropic fundamentals: chat models, messages, templates, structured output, RAG, memory, LCEL, tools & agents | **5/5** — the foundational toolkit everything else builds on |
| 002 | Summarize_Private_Documents_RAG_Anthropic_annotated_v4 | RAG pipeline + conversational memory, IBM-notebook-turned-Anthropic | **5/5** — core RAG + memory pattern |
| 003 | vector_databases_for_rag | Embeddings, distance metrics, ANN search, Chroma, chunking, hybrid search/re-ranking | **5/5** — core retrieval-quality depth |
| 004 | langgraph_fundamentals | What `create_agent` hides: `StateGraph`, nodes/edges, conditional branching, checkpointer | **5/5** — essential for debugging/customizing any agent |
| 005 | multi_agent_orchestration | Router, Handoffs, Subagents, Skills, Human-in-the-loop, Reflection | **5/5** — multi-agent patterns are increasingly expected in this role |
| 006 | advanced_retrievers | MultiQueryRetriever, SelfQueryRetriever, re-ranking | **5/5** — core RAG quality engineering |
| 007 | evaluation_for_llm_apps | Retrieval metrics, LLM-as-judge, LangSmith tracing/datasets | **5/5** — evaluation is a real differentiator for "production-ready" |
| 008 | production_reliability | Idempotency, tracing, retry/error handling, guardrails, secrets, cost/latency, testing | **5/5** — arguably the single most job-relevant notebook here |
| 009 | gradio_ui | Chat UI, streaming, per-user session state, LangGraph Store, guardrails in a live UI | **4/5** — great for demos/internal tools; Gradio itself isn't the usual production frontend |
| 010 | fastapi_docker_fundamentals | FastAPI service, async endpoints, Docker packaging, secrets in containers | **5/5** — the actual path from notebook to shipped service |
| 011 | mcp_fundamentals | MCP servers/clients, transports, wiring MCP tools into `create_agent` | **5/5** — current, in-demand standard for tool integration in 2026 |

---

## 000a — `000a_llm_foundations.ipynb` (theory precursor)

RLHF/DPO/Constitutional AI, scaling laws, MoE, model families, context windows, fine-tune-vs-RAG-vs-prompting.

| Section | Relevance | Why |
|---|---|---|
| 1. RLHF (SFT → Reward Model → PPO) | 2/5 | Training-infra internals; interview knowledge, not hands-on for this role |
| 2. DPO (Direct Preference Optimization) | 2/5 | Same — useful to explain *why* Claude behaves as it does, not something you build |
| 3. Constitutional AI / RLAIF | 3/5 | Interview trivia mostly, but the safety-alignment framing connects to 008's guardrails work |
| 4. Chinchilla Scaling Laws | 2/5 | ML research context; good interview one-liner, not a daily concern |
| 5. Mixture of Experts (MoE) | 2/5 | Model-architecture trivia; useful for reading model cards, not for building |
| 6. Modern Model Families | 3/5 | Useful context for model-tier selection decisions (echoes 008's cost/latency section) |
| 7. Context Windows (incl. "Lost in the Middle") | 4/5 | Directly informs chunking/retrieval design — the reasoning behind 001/003/006's chunk-size tradeoffs |
| 10. Fine-Tune vs RAG vs Prompting — Decision Framework | **5/5** | Core architectural decision every App Engineer has to justify; directly reused across this curriculum |

## 000b — `000b_prompting_techniques.ipynb` (theory precursor)

AI Engineer interview prep, Sections 8–12: prompting, function calling, fine-tuning decision, PEFT/LoRA, evaluation.

| Section | Relevance | Why |
|---|---|---|
| 8. Prompting Techniques (zero/few-shot, CoT, ReAct) | **5/5** | Core, daily-use skill — the actual vocabulary and technique set for every prompt you write |
| 9. Function Calling / Structured Outputs | **5/5** | The mechanism underlying every tool/agent built in 001–011 |
| 10. Fine-Tuning vs. RAG vs. Prompting | **5/5** | Same decision framework as 000a §10, reinforced here |
| 11. PEFT and LoRA / QLoRA Fine-Tuning (hands-on) | 2/5 | ML-engineering territory — rarely hands-on for an App Engineer; useful to recognize the tradeoff, not to implement |
| 12. LLM Evaluation | **5/5** | Core skill, built out fully and for real in 007 |

## 000c — `000c_production_inference.ipynb` (theory precursor)

Inference optimization: KV cache, quantization, batching, speculative decoding, prompt caching.

| Section | Relevance | Why |
|---|---|---|
| 13. KV Cache | 3/5 | Explains *why* prompt caching and per-token billing behave as they do; rarely configured directly by an App Engineer |
| 14. Quantisation at Inference (INT8/INT4) | 2/5 | Infra/ML-systems territory — interview knowledge, not a build task here |
| 15. Batching Strategies (static/continuous/PagedAttention) | 2/5 | Infra territory; useful for reading vendor docs on throughput, not something you implement |
| 16. Speculative Decoding | 2/5 | Interview trivia; not something an App Engineer configures |
| 17. Prompt Caching | **5/5** | Directly configurable via the Anthropic API — used for real in 008's cost/latency section |
| Summary — Production Inference Decision Framework | 4/5 | Useful mental model for choosing between model tiers/optimizations |

---

## 001 — Build_Smarter_AI_Apps_LangChain_Anthropic_modern.ipynb — **5/5**

- Setup note — fixing import errors from before
- 1. Chat Model — `ChatAnthropic`
- 2. Chat Messages — `SystemMessage`, `HumanMessage`, `AIMessage`
- 3. Exercise — Temperature and Sampling
- 4. Prompt Templates
- 5. Structured Output — `with_structured_output`
- 6. Documents & Text Splitters
- 7. Embeddings & Vector Store
- 8. Retrievers & Parent Document Retriever
- 9. RAG — Retrieval + Generation
- 10. Conversational Memory
- 11. LCEL — Composing Chains
- 12. Tools & Agents

## 002 — Summarize_Private_Documents_RAG_Anthropic_annotated_v4.ipynb — **5/5**

- Background — What is RAG? / RAG's two phases
- Objectives
- Setup — libraries, API key
- Preprocessing — load, split, embed, store
- LLM Model Construction (+ raw Anthropic SDK equivalent)
- Retrieval + Generation (+ raw SDK tool-use loop equivalent)
- Conversational Memory (+ raw SDK memory-without-a-checkpointer equivalent)
- Exercises (own document, return source, different Claude model)
- Conclusion / What to build next

## 003 — vector_databases_for_rag.ipynb — **5/5**

- 1. What is an embedding, really?
- 2. Distance metrics from scratch
- 3. Visualizing embedding space
- 4. How does ANN search actually work?
- 5. Chroma fundamentals
- 6. Chunking strategies — and why they change your results
- 7. Full RAG pipeline: Chroma + Claude
- 8. Evaluating retrieval quality
- 9. Advanced: hybrid search & re-ranking
- 10. Exercises — build understanding by extending this

## 004 — langgraph_fundamentals.ipynb — **5/5**

- 1. Setup
- 2. Core building blocks: `StateGraph`, state, nodes, edges
- 3. Conditional edges — real branching logic
- 4. Rebuilding `create_agent` from scratch
- 5. Checkpointer + `thread_id` — verified with real execution
- 6. Why you'd actually drop to raw LangGraph instead of `create_agent`
- 7. Optional — the raw Anthropic SDK equivalent

## 005 — multi_agent_orchestration.ipynb — **5/5**

- Setup — sample knowledge base, per-specialist retrieval tools
- 1. Router — classify, then dispatch
- 2. Handoffs, done right
- 3. Subagents — a main agent calls specialists as tools, stays in charge
- 4. Skills — no second agent at all
- 5. Human-in-the-loop — pausing for real approval
- Shared vs. private state
- Reflection / Reflexion — a genuinely different loop from ReAct
- Closing: Swarm, and which of the five patterns to actually reach for

## 006 — advanced_retrievers.ipynb — **5/5**

- Setup
- 1. The knowledge base — a policy set with real metadata to filter on
- 2. The problem: a single embedding can't represent a compound question
- 3. `MultiQueryRetriever` — casting a wider net across facets
- 4. `SelfQueryRetriever` — letting an LLM write the filter dict for you
- 5. Optional — raw Anthropic SDK equivalent of both retrievers
- 6. Re-ranking — fixing the final ordering
- 7. When to actually reach for these
- Exercises

## 007 — evaluation_for_llm_apps.ipynb — **5/5**

- Setup
- 1. Rebuilding the knowledge base and retrievers
- 2. A real labeled eval set
- 3. Retrieval metrics — precision@k/recall@k/MRR
- 4. Beyond retrieval: is the generated answer actually good? (LLM-as-judge)
- 5. LangSmith — tracing, a real dataset, regression testing
- 6. Optional — raw Anthropic SDK equivalent of the judge
- 7. Which layer actually matters, and when
- Exercises

## 008 — production_reliability.ipynb — **5/5**

- Setup
- 1. Idempotency in LLM pipelines
- 2. LangSmith tracing — from the ground up
- 3. Retry & error handling (`ModelRetryMiddleware`, `ModelFallbackMiddleware`)
- 4. Guardrails (PII detection, prompt-injection/jailbreak checks)
- 5. Secrets & config management (`getpass` → `.env`/`python-dotenv`)
- 6. Cost/latency optimization (prompt caching, batching, streaming, model-tier selection)
- 7. Testing LLM applications (mocking vs. LangSmith regression)
- Closing / What's next

## 009 — gradio_ui.ipynb — **4/5**

- Setup
- 1. What Gradio actually is, and the simplest possible chat UI
- 2. Streaming in the UI — 008's `.stream()`, actually used
- 3. Per-user session state — `thread_id` per browser session
- 4. LangGraph `Store` — the piece deliberately deferred out of 008
- 5. 008's guardrails and tracing, seen from inside a live UI
- 6. Running and sharing it — and where this stops, on purpose
- Closing

## 010 — fastapi_docker_fundamentals.ipynb — **5/5**

- Setup
- 1. What an API is, and what FastAPI specifically adds
- 2. Real request/response models — `BaseModel` applied to HTTP
- 3. Wiring in an actual agent — 008's PII-guarded agent
- 4. Async endpoints — measured, not just asserted
- 5. The free thing — auto-generated docs
- 6. What Docker actually is
- 7. A real Dockerfile, for the agent from Section 3
- 8. Secrets in a container
- Closing

## 011 — mcp_fundamentals.ipynb — **5/5**

- What this notebook covers / Setup
- 1. The problem MCP solves
- 2. The three primitives: Tools, Resources, Prompts
- 3. The simplest possible FastMCP server
- 4. A simple MCP client — connect, list, call
- 5. Transports: STDIO vs. HTTP
- 6. Wiring MCP tools into a real `create_agent`
- 7. The permission/approval model
- 8. Consuming a real external server you didn't write
- Closing

---

## Other files in this folder

- **`Roadmap.md`** — build history, what's done/planned, cross-notebook design decisions
- **`010_app/`** — supporting `.py` files for 010's FastAPI exercises and Sarah's own 011 server/client exercises (`app5_math_server.py`, `app5_test_client.py`)
- **`012` (Capstone)** — planned, not yet a file in this folder; see Roadmap.md for scope

## Highest-leverage sections for interview prep specifically

If time is limited, these are the sections that punch hardest for an LLM Application Engineer interview specifically (mix of "actually asked about" and "you'd be expected to have an opinion on"):

1. 000a/000b §10 — Fine-tune vs. RAG vs. Prompting decision framework
2. 000c §17 — Prompt Caching (real, billable Anthropic mechanism)
3. 004 — What `create_agent` actually hides (shows you understand the framework, not just the API)
4. 005 — The five multi-agent patterns and when to reach for each
5. 007 — Retrieval metrics + LLM-as-judge (shows you can prove an app works, not just that it runs)
6. 008 — Guardrails, retries, and secrets (production maturity signal)
7. 011 — MCP (current, and most interviewers will ask if you've used it)
