---

title: HR AI Content System
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
----------------

# 🤖 HR AI Content Optimization System

This project is a **mini enterprise-grade AI system** that transforms unstructured HR content into **AI-ready, governed, and retrievable knowledge assets**.

It simulates how organizations modernize HR content for AI-powered employee experiences.

---

# 🚨 Problem

HR content is often:

* Unstructured (PDFs, policies, FAQs)
* Inconsistent and hard to search
* Not optimized for AI systems
* Lacking governance and traceability

---

# 💡 Solution

This system builds a **complete AI-ready content pipeline**:

### 1. Ingestion

* Loads HR documents from raw text

### 2. Content Optimization

* Semantic chunking (section-aware)
* Clean, structured formatting

### 3. Metadata & Taxonomy

* Document tagging
* Title-based classification
* Chunk-level traceability

### 4. Embeddings + Retrieval

* Sentence-transformers embeddings
* Vector similarity search
* Top-k relevant retrieval

### 5. Governance Layer

* PII redaction (SSN, salary, etc.)
* Role-based access control (RBAC)

### 6. Answer Generation

* Context-grounded responses
* Source attribution
* Confidence scoring
* Irrelevant query handling

### 7. Evaluation System

* Golden dataset (relevant + irrelevant queries)
* Accuracy measurement
* Retrieval validation

---

# 🎯 Key Features

* AI-ready HR content pipeline
* Semantic chunking + embeddings
* Metadata tagging & traceability
* Role-based access (RBAC)
* PII redaction for compliance
* Retrieval quality evaluation
* Safe handling of irrelevant queries

---

# 🌐 Live Demo

👉 https://aiversesavant-hr-ai-content-system.hf.space

---

# 🧪 Example Queries

### ✅ Relevant Questions

* How many PTO days do employees get?
* Can PTO be carried over?
* How long is parental leave?
* How many sick leave days are given?
* How many days can employees work remotely?

### ❌ Irrelevant Questions (Handled Safely)

* What is the company stock price?
* Who is the CEO?
* Tell me a joke

---

# 🏗️ Project Structure

```
hr-ai-content-system/
│
├── app.py
├── requirements.txt
├── README.md
│
├── pipeline/
│   ├── ingestion.py
│   ├── chunking.py
│   ├── metadata.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── governance.py
│   └── evaluation.py
│
├── data/
│   └── sample_hr_docs.txt
```

---

# 📊 Evaluation

The system includes:

* Golden question set
* Accuracy tracking
* Retrieval validation

This ensures:

* Answer correctness
* Grounded responses
* Reliable AI behavior

---

# 🔐 Governance & Compliance

* PII redaction (SSN, salary)
* Role-based filtering (employee vs HR)
* Safe response handling for non-HR queries

---

# 🚀 Tech Stack

* Python
* Gradio (UI)
* Sentence Transformers
* NumPy
* Scikit-learn

---

# 🧠 Why This Project

This project demonstrates:

* AI-ready content engineering
* Retrieval-augmented systems (RAG)
* Information architecture & metadata design
* Governance & compliance patterns
* Evaluation & observability

---

# 👤 Author

Built by Chaitu
GitHub: https://github.com/aiversesavant/hr-ai-content-system
