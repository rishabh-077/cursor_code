# Side project: Small RAG pipeline (resume + interviews)

**Timeline:** Build MVP **Week 14** · Polish + GCP story **Week 19**  
**Pairs with:** Endeavour Vertex AI story (production LLM) + this (data/RAG fundamentals)

---

## Scope (keep it small — 1 weekend + 2 evenings)

| In scope | Out of scope |
|----------|----------------|
| PDF or markdown docs ingested | Fine-tuning LLMs |
| Chunk + embed + store vectors | Custom vector DB cluster |
| Ask question → retrieve top-k → answer with citations | Multi-tenant auth |
| README + architecture diagram | Production SLA |

---

## Suggested stack (aligns with your GCP skills)

| Layer | Option A (simple) | Option B (more GCP) |
|-------|-------------------|---------------------|
| Ingest | Local folder / GCS bucket | GCS |
| Chunk | LangChain `RecursiveCharacterTextSplitter` | Same |
| Embed | OpenAI API or **Vertex AI embeddings** | Vertex AI |
| Vector store | Chroma (local) or **pgvector** | Vertex AI Vector Search (stretch) |
| LLM | Gemini API / Vertex | Gemini |
| Serve | CLI script | Cloud Run + FastAPI |

**Resume line (after done):**  
*Built an end-to-end RAG pipeline on GCP: document ingestion, semantic chunking, Vertex embeddings, vector retrieval, and Gemini-grounded Q&A with source citations.*

---

## Build steps (checklist)

- [ ] Pick domain you know (e.g. “DE interview notes” from your own markdown files)
- [ ] `ingest.py` — load files, metadata (source path, page)
- [ ] `chunk.py` — chunk size 500–1000 tokens, overlap 100
- [ ] `embed_index.py` — embed chunks, upsert to vector store
- [ ] `query.py` — user question → top 5 chunks → prompt Gemini with context
- [ ] `README.md` — diagram + how to run + design decisions
- [ ] `ARCHITECTURE.md` — 1 page: failure modes (stale docs, hallucination, chunk boundaries)

---

## Interview talking points

1. **Why RAG vs fine-tune?** — Cheaper, updatable docs, citations.  
2. **Chunking tradeoff** — Small chunks = precision; large = context.  
3. **Eval** — 5 hand-written questions; did answer cite right chunk?  
4. **Prod extras** — Caching embeddings, batch refresh, cost per query.

---

## Link to Endeavour project

| Endeavour (prod) | RAG side project |
|------------------|------------------|
| Structured match records | Unstructured documents |
| Classification prompt | Retrieval + generation |
| Vertex Gemini | Same stack family |
| Business: match quality | Business: Q&A over knowledge base |

*“Endeavour taught me operational LLM integration; RAG project taught me retrieval layer design.”*
