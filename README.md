# 🚀 Material Setu — AI-Driven Material Code Standardization & Harmonization

[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)](#)
[![React](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-61DAFB)](#)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791)](#)
[![pgvector](https://img.shields.io/badge/Vector%20DB-pgvector-purple)](#)
[![Docker](https://img.shields.io/badge/Deployment-Docker-2496ED)](#)
[![License](https://img.shields.io/badge/License-MIT-blue)](#)

> **Material Setu** is an AI-driven platform designed to standardize, classify, match, and harmonize material codes used across Central Public Sector Enterprises (CPSEs).

Different CPSEs often maintain their own local material codes, descriptions, specifications, units of measurement, and classifications for the same or functionally equivalent materials.

**Material Setu** uses NLP, semantic similarity, attribute matching, and engineering-aware validation to identify duplicate and equivalent materials and recommend a **Common National Material Code (NMC)** while preserving the original CPSE material codes.

---

## 🌟 Key Features

### 🤖 AI-Powered Material Matching

Material Setu combines multiple matching techniques to identify whether two material records represent the same or functionally equivalent item:

* Lexical similarity
* Semantic similarity using **Sentence-BERT**
* Attribute/specification matching
* Manufacturer part-number matching
* Critical-attribute conflict detection
* Combined confidence scoring

The AI system recommends potential matches, while final approval remains with an authorized human steward.

---

### 🧹 Material Standardization

Automatically standardizes inconsistent material descriptions and units.

Examples:

```text
"BEARING BALL 6205"
"BALL BRG 6205"
"BEARING-6205"

        ↓

Standardized Material

"Ball Bearing 6205"
```

Common UOM variations can also be normalized:

```text
NOS / No. / PC / Nr
        ↓
       EA
```

---

### 🏷️ Material Classification

Materials are classified using **4-digit Federal Supply Classification (FSC)** codes.

Examples:

```text
3110 → Bearings
6145 → Electrical Cable
```

Classification helps organize materials into meaningful families and improves the matching process.

---

### 🔎 Semantic Similarity with Sentence-BERT

Material descriptions are converted into vector embeddings using:

```text
all-MiniLM-L6-v2
```

These embeddings allow the system to understand semantic similarity rather than relying only on exact keywords.

For example:

```text
"Ball Bearing 6205 SKF"
```

can be identified as semantically similar to:

```text
"SKF Deep Groove Ball Bearing 6205"
```

even though the descriptions are not identical.

---

### ⚠️ Engineering Safety Guardrails

Material matching must not result in unsafe engineering substitutions.

Material Setu therefore checks critical attributes such as:

* Voltage
* Pressure rating
* Material grade
* Bore size
* Valve body material
* Cable specifications
* Other family-specific engineering attributes

If a critical attribute conflicts, the system reduces the confidence score and can send the candidate for steward review.

> **Important:** AI only recommends material identity candidates. It does not approve engineering substitutions.

---

### 👨‍💼 Human-in-the-Loop Review

Every important AI recommendation can be reviewed by an authorized material steward.

```text
AI Candidate Match
        ↓
Confidence Score
        ↓
Human Steward Review
        ↓
 ┌──────┴──────┐
 ↓             ↓
Approve       Reject
 ↓
NMC Mapping
```

---

### 🆔 Common National Material Code (NMC)

Approved standardized materials receive a unique Common National Material Code.

Format:

```text
NMC-<FSC>-<Sequence>
```

Example:

```text
NMC-3110-00042
```

Existing CPSE local material codes are **never deleted or overwritten**.

---

# 🏗️ System Architecture

```text
                     ┌─────────────────────┐
                     │    CPSE Data       │
                     │ CSV / Excel / API  │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │       INGEST        │
                     │ Data Validation     │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │    STANDARDIZE      │
                     │ Description + UOM   │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │     CLASSIFY        │
                     │      FSC Code      │
                     └──────────┬──────────┘
                                │
                                ▼
              ┌─────────────────────────────────┐
              │          AI MATCHING            │
              │                                 │
              │ • Lexical Similarity            │
              │ • Sentence-BERT Embeddings      │
              │ • Attribute Matching             │
              │ • Part Number Matching           │
              │ • Critical Conflict Detection    │
              └────────────────┬────────────────┘
                               │
                               ▼
                     ┌─────────────────────┐
                     │       REVIEW        │
                     │ Human Steward       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │       PUBLISH       │
                     │ NMC + Crosswalk    │
                     └─────────────────────┘
```

---

# 🧠 AI/ML Pipeline

```text
Material A
    ↓
Text Preprocessing
    ↓
Feature Extraction
    ↓
 ┌───────────────┬────────────────┬────────────────┐
 ↓               ↓                ↓
Lexical       Semantic        Attributes
Similarity    Similarity       Matching
                  ↓
           Sentence-BERT
 └───────────────┬────────────────┘
                 ↓
        Part Number Matching
                 ↓
       Combined Match Score
                 ↓
     Critical Attribute Check
                 ↓
      Candidate Recommendation
```

---

# 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* JWT Authentication
* REST APIs

### AI / ML

* Sentence-BERT
* `all-MiniLM-L6-v2`
* Scikit-learn
* NumPy
* Semantic embeddings
* Similarity scoring

### Database

* PostgreSQL
* pgvector
* Material metadata
* Vector embeddings
* Match results
* Procurement information

### Frontend

* React
* Vite
* Dashboard UI
* Material management
* Match review
* NMC management
* Procurement analytics

### Deployment

* Docker
* Docker Compose
* Environment-based configuration

---

# 📁 Project Structure

```text
material-setu/
│
├── frontend/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── ml/
│   │   └── utils/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── database/
│   ├── schema.sql
│   └── seed.sql
│
├── data/
│   └── demo_materials.csv
│
├── model/
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/abhaytarkar51/material-setu.git
cd material-setu
```

---

## 2. Backend Setup

```bash
cd backend
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Backend:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

---

# 🖥️ Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🗄️ Database Setup

Material Setu uses PostgreSQL with the `pgvector` extension.

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

The database stores:

```text
Materials
    │
    ├── Material Attributes
    ├── Embeddings
    ├── Match Results
    ├── Steward Reviews
    ├── National Material Codes
    ├── CPSE Crosswalk
    └── Procurement Data
```

> The embedding/vector dimension must match the actual Sentence-BERT model configuration used by the backend.

---

# 🔐 Environment Configuration

Create `.env`:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/material_setu

JWT_SECRET=your-secret-key

MODEL_NAME=all-MiniLM-L6-v2

ENVIRONMENT=development
```

> Never commit `.env` or database credentials to GitHub.

---

# 🔌 REST API

### Materials

```http
GET /materials
POST /materials
GET /materials/{id}
```

### Matching

```http
GET /matches
POST /matches
```

### National Material Codes

```http
GET /nmc
POST /nmc
```

### Procurement

```http
GET /procurement/opportunities
```

---

# 🔄 End-to-End Workflow

```text
1. Upload CPSE Material Data
              ↓
2. Validate Input
              ↓
3. Standardize Description
              ↓
4. Normalize UOM
              ↓
5. Classify Material
              ↓
6. Generate Embedding
              ↓
7. Search Similar Materials
              ↓
8. Calculate Match Score
              ↓
9. Check Critical Attributes
              ↓
10. Generate Candidate Match
              ↓
11. Human Steward Review
              ↓
12. Generate NMC
              ↓
13. Create CPSE Crosswalk
              ↓
14. Publish Standardized Material
```

---

# 👥 User Roles

| Role        | Responsibility                        |
| ----------- | ------------------------------------- |
| **Admin**   | System and user management            |
| **Steward** | Review and approve material matches   |
| **Viewer**  | View materials, matches and analytics |

---

# 📊 Demo Dataset

The demonstration dataset represents material information across multiple CPSEs and sectors.

```text
~124 Materials
~18 CPSEs
~5 Sectors
~430 Procurement Lines
```

Illustrative results:

```text
~104 Candidate Matches
~19 NMC Recommendations
```

Potential illustrative procurement savings:

```text
~₹80 Lakh
```

> These are demonstration/sample figures and not verified production KPIs.

---

# 📈 Prototype ML Metrics

| Metric    | Result |
| --------- | -----: |
| Precision |  77.6% |
| Recall    |  65.2% |
| F1 Score  |  70.9% |

These metrics are based on the prototype/demo evaluation.

---

# 🚀 Production Deployment

Recommended architecture:

```text
Internet / CPSE Network
          │
          ▼
    HTTPS / Domain
          │
          ▼
        Nginx
       /     \
      ▼       ▼
 React/Vite  FastAPI
                │
                ▼
       PostgreSQL + pgvector
                │
                ▼
        ML Matching Engine
                │
                ▼
        Sentence-BERT Model
```

Production deployment should include:

* HTTPS
* Secure JWT configuration
* PostgreSQL backups
* Database monitoring
* Application logging
* API authentication
* ML model versioning
* Error monitoring
* Audit logs

---

# 🐳 Docker Deployment

Example:

```bash
docker compose up --build
```

Example services:

```yaml
services:

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"

  backend:
    build: ./backend
    ports:
      - "8000:8000"

  postgres:
    image: pgvector/pgvector:pg16
```

---

# 🔮 Future Scope

* Live SAP/ERP integration
* CPSE enterprise-system connectors
* Multilingual material descriptions
* Advanced embedding models
* Active learning from steward decisions
* Advanced procurement analytics
* Automated duplicate detection
* Material master synchronization
* Cloud-native deployment
* Monitoring and observability
* Enterprise SSO integration

---

# 👨‍💻 Project Role

### AI/ML & Deployment

The AI/ML and deployment layer focuses on:

* Material text preprocessing
* Description standardization
* Sentence-BERT embeddings
* Semantic similarity
* Multi-signal matching
* Attribute validation
* Critical attribute conflict detection
* Match confidence scoring
* ML model integration with backend APIs
* PostgreSQL + pgvector integration
* Docker containerization
* Production deployment

---

# 🎯 Vision

> **One standardized material identity across CPSEs — while preserving every organization's existing material code.**

Material Setu provides an AI-powered bridge between fragmented material master data and a harmonized national material ecosystem.

---

# 🏆 Smart India Hackathon 2026

**Problem ID:** SIH26099
**Problem:** AI-Driven Standardization and Harmonization of Material Codes Across CPSEs
**Theme:** Smart Automation
**Category:** Software

---

## 📄 License

This project is licensed under the **MIT License**.
