# 🚀 Master 24-Week Data Engineering + GenAI Infra Tracker

## 📊 Daily Time Split Strategy
- 🧮 90 Mins: Python Coding & Data Structures (Hands-on LeetCode)
- 🏗️ 90 Mins: Core Big Data, Systems Architecture & Streaming
- 🤖 30 Mins (Phases 2-3): GenAI & LLM Data Engineering Frameworks

---

## 📅 PHASE 1: Coding Foundations & Core DE Internals (Weeks 1–8)
*Goal: Clear Tier-1 coding screening rounds and deep-dive into your existing GCP/DBT stack.*

### Week 1: Big-O & HashMap Basics
- [ ] Learn Time & Space Complexity (O(1), O(N), O(N^2)).
- [ ] Master Python `dict` and `set` memory mechanics under the hood.
- [ ] Solve LeetCode: 217 (Contains Duplicate), 1 (Two Sum), 242 (Valid Anagram).
- [ ] Deep Dive: Read the official BigQuery Architecture Whitepaper (Capacitor Storage engine).

### Week 2: Array Manipulation & BigQuery Optimizations
- [ ] Learn In-place Array mutations and the Two-Pointer technique.
- [ ] Solve LeetCode: 88 (Merge Sorted Array), 121 (Best Time to Buy Stock), 167 (Two Sum II).
- [ ] Deep Dive: Implement and contrast BQ Table Partitioning vs. Clustering on a 10TB scale.

### Week 3: Sliding Window & DBT Architecture
- [ ] Learn the contiguous subarray tracking pattern (Sliding Window).
- [ ] Solve LeetCode: 3 (Longest Substring Without Repeating Characters), 219 (Contains Duplicate II).
- [ ] Deep Dive: Master DBT Materializations (Incremental strategies, merge vs. append, predicates).

### Week 4: Matrices & Advanced SQL Part 1
- [ ] Learn 2D Array traversal and coordinate manipulation in Python.
- [ ] Solve LeetCode: 48 (Rotate Image), 54 (Spiral Matrix).
- [ ] Deep Dive: Complete LeetCode SQL 50 (Focus: Analytical Window Functions & Partition By).

### Week 5: Stacks, Queues, & Advanced SQL Part 2
- [ ] Learn Last-In-First-Out (LIFO) and First-In-First-Out (FIFO) pipeline processing logic.
- [ ] Solve LeetCode: 20 (Valid Parentheses), 155 (Min Stack).
- [ ] Deep Dive: Master SQL Recursive CTEs, Self Joins, and query optimization tools (EXPLAIN plans).

### Week 6: PySpark & Dataproc Core Internals
- [ ] Learn Binary Search logic (O(log N) operations).
- [ ] Solve LeetCode: 704 (Binary Search), 74 (Search a 2D Matrix).
- [ ] Deep Dive: Master Spark Driver/Executor memory structure (Storage vs. Execution memory).

### Week 7: Spark Shuffle & Optimization
- [ ] Learn basic Sorting algorithms and their complexities.
- [ ] Solve LeetCode: 912 (Sort an Array), 56 (Merge Intervals).
- [ ] Deep Dive: Study Wide vs Narrow dependencies, Adaptive Query Execution (AQE), and Broadcast Joins.

### Week 8: Production Automation & Containerization
- [ ] Solve 5 random LeetCode Arrays/HashMaps Medium problems for speed.
- [ ] Deep Dive: Dockerize a Python processing app, deploy it to GCP Cloud Run via Azure DevOps (ADO).
- [ ] Phase 1 Milestone Check: Can you confidently solve a LeetCode Medium array problem in under 25 minutes?

---

## 📅 PHASE 2: Advanced Systems, Streaming, & GenAI Data Infra (Weeks 9–16)
*Goal: Bridge the streaming gap, study distributed systems design, and start AI data pipelines.*

### Week 9: Distributed Data Store Internals (DDIA Part 1)
- [ ] Learn Two-Pointer sliding window combinations.
- [ ] Read DDIA Book: Chapters 1 & 2 (Reliability, Scalability, Data Models).
- [ ] Deep Dive: Understand LSM-Trees vs. B-Trees storage systems.
- [ ] 🤖 AI Module: Read "AI Engineering" (Chip Huyen) Chapter 1. Learn the scale differences between traditional data vs. LLM token embeddings.

### Week 10: Partitioning & Replication (DDIA Part 2)
- [ ] Learn Linked List basics in Python (Node creation, traversal).
- [ ] Read DDIA Book: Chapters 5 & 6 (Replication, Partitioning/Sharding).
- [ ] Deep Dive: Handle data skewness and hot spots in distributed nodes.
- [ ] 🤖 AI Module: Study Vector Databases (Pinecone, Milvus, pgvector). Learn how vector indices (HNSW, IVF-FLAT) work.

### Week 11: Real-Time Ingestion (Kafka / Pub/Sub)
- [ ] Solve LeetCode: 206 (Reverse Linked List), 141 (Linked List Cycle).
- [ ] Deep Dive: Study Kafka/Pub/Sub architecture (Partitions, Consumer Groups, Offsets, Commit logs).
- [ ] 🤖 AI Module: Build a Python script that takes unstructured text, passes it to an embedding model API, and loads vectors into a database.

### Week 12: Stream Processing Mechanics
- [ ] Learn Fast & Slow pointer techniques.
- [ ] Deep Dive: Read "Streaming Systems" (Tyler Akidau) Chapters 1-2. Event time vs. Processing time.
- [ ] Master Windowing: Tumbling, Hopping, and Session windows.
- [ ] 🤖 AI Module: Study data pipelines for Retrieval-Augmented Generation (RAG). Learn chunking strategies (fixed-size vs semantic chunking).

### Week 13: Late Data Handling & Schema Evolution
- [ ] Learn Tree traversal concepts (Breadth-First Search vs. Depth-First Search).
- [ ] Deep Dive: Understand Watermarks, Allowed Lateness, and Exactly-Once delivery semantics.
- [ ] Master Avro & Parquet schema evolution management.
- [ ] 🤖 AI Module: Study real-time context injection pipelines for AI Agents.

### Week 14: Airflow/Composer Optimization
- [ ] Solve LeetCode: 104 (Maximum Depth of Binary Tree), 112 (Path Sum).
- [ ] Deep Dive: Cloud Composer scalability, Celery/Kubernetes Executors, dynamic DAG creation, and XCom backends.
- [ ] 🤖 AI Module: Learn how to orchestrate LLM evaluation pipelines using Airflow.

### Week 15: Big Data System Design Patterns
- [ ] Solve LeetCode: 98 (Validate Binary Search Tree).
- [ ] System Design: Whiteboard an E-commerce Batch Metrics platform (Scale: 100 Million daily active events).
- [ ] 🤖 AI Module: Architect a pipeline to continuously ingest, clean, and fine-tune an open-source LLM model.

### Week 16: Streaming System Design Patterns
- [ ] Re-solve 5 complex LeetCode Medium questions from previous weeks.
- [ ] System Design: Whiteboard a Real-Time Log Analytics and Fraud Monitoring dashboard using Kafka, Dataflow, and BigQuery.
- [ ] Phase 2 Milestone Check: Can you design a fault-tolerant streaming architecture on a whiteboard from scratch?

---

## 📅 PHASE 3: System Design Mocking, Behavioral & Interview Loop (Weeks 17–24)
*Goal: Optimize your resume, polish your delivery via live mocks, and secure your target offers.*

### Week 17: End-to-End Enterprise System Architecture
- [ ] Solve LeetCode: Top 5 tagged questions for Amazon/Google (Filter: Medium).
- [ ] System Design: Practice Change Data Capture (CDC) architectures from transactional DBs (Postgres) to BigQuery.
- [ ] 🤖 AI Module: Design an enterprise-grade RAG pipeline framework, focusing on caching strategies for high-frequency queries.

### Week 18: Behavioral Round Mastery (The STAR Method)
- [ ] Solve LeetCode: Review 10 High-frequency Hash Map/Array problems.
- [ ] Behavioral Prep: Draft 5 core project stories from your Tiger Analytics & Accenture experience.
- [ ] Structure stories using STAR: **S**ituation, **T**ask, **A**ction (highlighting your technical choice), **R**esult (quantify with % or metrics).

### Week 19: Resume Optimization & Portfolio Polish
- [ ] Solve LeetCode: 5 Medium Matrix / String problems.
- [ ] Resume Overhaul: Remove vague text. Rewrite statements using the Google X-Y-Z formula: "Accomplished [X] as measured by [Y], by doing [Z]".
- [ ] *Example*: "Optimized BigQuery processing cost by 40% (Y) by implementing table clustering and re-architecting DBT incremental materializations (Z) across 15 core data models (X)."

### Week 20: Technical Speed-Running
- [ ] LeetCode: Solve 15 random Medium problems using a strict 20-minute timer per question.
- [ ] System Design: Practice lightning-fast components layout (API gateways, stream buffers, compute layers, data lakes).

### Week 21: Live Mock Technical Rounds
- [ ] Practice 2 live coding mock interviews on platforms like Pramp or Interviewing.io.
- [ ] Practice 2 data system design mock interviews with peers or mentors.
- [ ] Note down any areas where you stumbled or hesitated during explanations.

### Week 22: Active Job Application Sprints
- [ ] Target tech recruiters directly via LinkedIn. Focus on Tier-1 Product MNCs, high-growth startups, and elite FinTech firms.
- [ ] Tailor application profiles specifically highlighting your dual expertise in GCP Cloud Data Engineering and Vector/AI Infra pipelines.

### Week 23: Live Interview Loop Execution
- [ ] Attend actual company interview processes. Treat the first 2-3 interview loops as practice to shed any live-session nervousness.
- [ ] Keep notes on actual questions asked to review and fix any unexpected gaps.

### Week 24: Offer Analysis & Compensation Negotiation
- [ ] Manage multiple pipeline offers. Leverage competing counter-offers to maximize base salary and stock grants.
- [ ] Target compensation range: ₹40LPA – ₹55LPA based on your deep architectural stack execution.
