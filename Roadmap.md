LLM Application Engineer Curriculum — Full Roadmap
Already built
Theory foundations

Phase 1 — LLM foundations
Phase 1 — Production LLM
FFNN Diabetes
loss_functions
tensors_and_operations
transformer from scratch
pytorch_transformer_bootcamp_test

AI Engineer tutorial
Applied notebooks (moved into Phase 2/03_Anthropic_Notes/ alongside the collaborative series, numbered 001-003)

001 — Build_Smarter_AI_Apps — LangChain modern
002 — Summarize_Private_Documents_RAG — includes conversational memory
003 — vector_databases_for_rag
Collaborative series (Phase 2/03_Anthropic_Notes/, renumbered 004-007 to stay consistent with 001-003 above)

004 — LangGraph fundamentals (reviewed only, never edited — Sarah's standing instruction is "don't touch 004 at all"; known cosmetic issues noted but left alone: cells 22-27 are near-duplicate exploratory cells, cell 28 is empty, cell 11's comment is separated from its code)
005 — Multi-agent orchestration — fully rebuilt (2026-07-xx): hardcoded-key issue fixed, Q&A folded into prose, `langgraph-supervisor`/`create_supervisor` cut entirely (out of date per docs), added real sections for Subagents, Skills (explicitly flagged as "not really multi-agent"), and Human-in-the-loop/interrupts. Reviewed fresh afterward — solid.
006 — Advanced Retrievers — built and reviewed. MultiQueryRetriever + SelfQueryRetriever (with a hand-written SimpleChromaTranslator since langchain_community isn't installed) + a re-ranking section (CrossEncoder) added after Sarah asked whether anything else was worth including. Confirmed current against docs-langchain MCP.
007 — Evaluation for LLM Apps — built and reviewed. Retrieval metrics (precision@k/recall@k/MRR), LLM-as-judge, full LangSmith pipeline (tracing/dataset/evaluate()/regression testing). Content judged complete for its scope — no missing technique identified.
  ⚠️ Open bug (unfixed, review-only mode per Sarah's request): cell 14 shows "Mean recall@3: 2.611" — impossible since recall ∈ [0,1]. Root cause confirmed via isolated repro: `Chroma.from_documents(..., collection_name=...)` is not idempotent and was re-run multiple times in the same kernel session, duplicating documents in the collection. Fix = restart kernel + rebuild vectorstore fresh (fixes today's numbers) but the notebook code itself has no guard against recurrence (no delete_collection()/existence check) — worth an actual code fix, not just a restart habit. Same latent non-idempotent-Chroma pattern exists in 004/005/006/midterm too (flagged, not touched elsewhere since none of those are currently corrupted).
Planned
008 — Production Reliability

with_structured_output (replacing manual JsonOutputParser)
Retry/error handling
LangSmith tracing
supervisor vs swarm
Guardrails: prompt-injection awareness plus output filtering, PII redaction, jailbreak resistance
Secrets/config management (motivated by the hardcoded key found in notebook 005)
Cost/latency optimization: prompt caching, batching, model-tier selection (Haiku vs. Sonnet vs. Opus)

009 — Gradio UI
Real chat UI, streaming, per-user session state, wrapping a LangGraph agent from 004/005. Paired with session state: check whether the 004/005 agents need a LangGraph checkpointer/store persistence section — distinct from the chat-level memory already covered in Summarize_Private_Documents_RAG — and add it only if that's still an open gap once you get here.

010 — MCP Fundamentals
Real FastMCP server (tools/resources/prompts), client (STDIO/HTTP), permission/approval model — covering both building your own server and consuming external MCP servers as tools from a LangChain/LangGraph agent.

011 — Capstone
End-to-end system: Chroma + advanced retrievers (006) + multi-agent LangGraph system (004/005) + MCP integration (010) + eval suite (007) proving it works + production reliability (008) + FastAPI backend (from zero) + Docker (from zero) + Gradio frontend calling the API — plus actually shipping the container somewhere (basic cloud/PaaS deploy) and light production monitoring. Large enough to split into checkpoints if needed: 011a (FastAPI + Docker + deploy) then 011b (full integration).

Deliberately out of scope
Fine-tuning / model customization — ML-engineering territory, not typically required for this role
Multi-provider abstraction — minor, since LangChain already abstracts most of it
Midterm project (Projects/midterm_throne_of_glass_companion.ipynb) — self-implemented by Sarah with Claude debugging support, now complete through Sections 1-7: vector store, two specialist retrieval tools, self-query spoiler filtering, Subagents-based multi-agent orchestration (redone from an initial Router pattern) with real cross-thread memory, eval set, pooled full-system retrieval metrics, and an LLM-as-judge spoiler-leakage check that reads actual retrieved context (not just the question/answer). Only the closing Reflection is still unwritten.

Saved to memory as the current version of record (project_curriculum_roadmap.md). Next up: 008 — Production Reliability, and/or finishing the midterm's Reflection, unless you want to reorder.
