# AI-Powered Resume Screening System

> 🚧 **Project Status: Under Development**
>
> An AI-powered resume screening and candidate evaluation system designed to automate parts of the recruitment workflow using **Django, Django REST Framework, NLP, and Machine Learning**.

## 📌 Overview

Recruiters often need to review a large number of resumes for a single job opening. Manually comparing resumes with job requirements can be time-consuming and inconsistent.

This project aims to build a web-based **Resume Screening System** that can analyze candidate resumes against a given job description and provide relevant information such as:

* Resume parsing
* Skill extraction
* Job description analysis
* Candidate-job matching
* Resume scoring
* Candidate ranking
* Missing skill identification
* Screening results through a REST API
* Recruiter-friendly dashboard

The project is being developed from scratch with a focus on building a practical **AI/ML-powered backend application** rather than only creating a standalone ML model.

---

## 🎯 Objectives

The main objectives of this project are:

1. Build a resume upload and management system.
2. Extract useful information from resumes automatically.
3. Analyze job descriptions and required skills.
4. Compare candidate profiles with job requirements.
5. Generate a relevance/matching score.
6. Rank candidates based on their suitability.
7. Identify matching and missing skills.
8. Provide the functionality through REST APIs.
9. Build a clean backend architecture using Django.
10. Eventually integrate an AI/ML/NLP pipeline into the application.

---

## 🏗️ Planned Architecture

```text
                    ┌─────────────────────┐
                    │     Recruiter       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Django Backend    │
                    │    + REST API       │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      Resume Upload      Job Description     Candidate
             │               Analysis         Management
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   NLP Processing    │
                    │                     │
                    │ • Text Extraction   │
                    │ • Skill Extraction  │
                    │ • Embeddings        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Matching / Scoring  │
                    │                     │
                    │ Candidate ↔ Job     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Candidate Ranking   │
                    │ & Screening Result  │
                    └─────────────────────┘
```

---

## 🛠️ Planned Technology Stack

### Backend

* Python
* Django
* Django REST Framework

### AI / Machine Learning

* Scikit-learn
* Hugging Face Transformers
* NLP techniques
* Text embeddings
* Semantic similarity

### Database

* PostgreSQL

### Supporting Libraries

* Pandas
* NumPy
* PyPDF
* python-docx
* Joblib

### Development Tools

* Git
* GitHub
* VS Code
* Postman

---

## 📂 Planned Project Structure

```text
resume-screening-system/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── resumes/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── jobs/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── screening/
│   ├── services/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── tests.py
│
├── ml/
│   ├── preprocessing/
│   ├── embeddings/
│   ├── matching/
│   └── scoring/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

> **Note:** The project structure is currently being developed and may change as implementation progresses.

---

## 🔄 Planned Workflow

### 1. Recruiter Creates a Job

The recruiter provides:

* Job title
* Job description
* Required skills
* Preferred skills
* Experience requirements
* Education requirements

### 2. Candidate Resume Upload

The system accepts resumes in supported formats such as:

```text
PDF
DOCX
```

### 3. Resume Processing

The system extracts text and identifies relevant information such as:

* Name
* Contact information
* Education
* Experience
* Skills
* Projects
* Certifications

### 4. NLP Processing

The extracted resume text will be processed using NLP techniques.

The system will generate representations of:

```text
Resume
   ↓
Preprocessing
   ↓
Text Representation
   ↓
Embedding
```

The same process will be applied to the job description.

### 5. Candidate Matching

The system will compare the candidate's resume with the job requirements using semantic similarity and other matching techniques.

Example:

```text
Job Requirement
       │
       ▼
Required Skills
       │
       ▼
Candidate Resume
       │
       ▼
Skill + Semantic Matching
       │
       ▼
Matching Score
```

### 6. Candidate Ranking

Candidates will eventually be ranked based on their overall relevance to the job.

Example:

| Candidate   | Match Score | Status         |
| ----------- | ----------: | -------------- |
| Candidate A |         91% | Strong Match   |
| Candidate B |         82% | Good Match     |
| Candidate C |         67% | Moderate Match |
| Candidate D |         43% | Low Match      |

*Example output only. Actual scoring will be implemented during development.*

---

## 📊 Planned Screening Result

The system is intended to provide results similar to:

```text
Candidate: John Doe

Overall Match: 87%

Matching Skills:
✓ Python
✓ Django
✓ REST API
✓ PostgreSQL
✓ Git

Missing / Preferred Skills:
✗ Docker
✗ AWS

Experience Relevance: High

Recommendation:
Strong Match
```

The scoring methodology is still under development and may evolve as different approaches are evaluated.

---

## 🚧 Development Status

This project is currently **under active development**.

### Completed

* [x] Repository created
* [x] Project idea and requirements defined
* [x] Initial system architecture planned
* [x] Technology stack selected
* [x] Backend architecture planned

### In Progress

* [ ] Django project setup
* [ ] Authentication system
* [ ] Resume management
* [ ] Job management
* [ ] REST API development
* [ ] Resume text extraction
* [ ] NLP preprocessing
* [ ] Skill extraction
* [ ] Semantic matching
* [ ] Candidate scoring
* [ ] Candidate ranking

### Planned

* [ ] Recruiter dashboard
* [ ] Screening history
* [ ] Advanced candidate filtering
* [ ] Model evaluation
* [ ] API documentation
* [ ] Automated tests
* [ ] Docker support
* [ ] Deployment
* [ ] Production optimization

---

## 🧠 AI/ML Approach

The AI component will be developed incrementally.

The initial approach will focus on establishing a reliable baseline using:

```text
Text Preprocessing
        ↓
Skill Extraction
        ↓
Text Embeddings
        ↓
Semantic Similarity
        ↓
Candidate Scoring
        ↓
Candidate Ranking
```

Different NLP and embedding approaches may be evaluated during development to determine the most suitable method for resume-job matching.

---

## 🔐 Security Considerations

Since resumes contain personal information, security will be considered during development.

Planned considerations include:

* Authentication and authorization
* Secure file uploads
* Input validation
* File type validation
* Environment variables for secrets
* API permissions
* Database security
* Protection of uploaded resumes

---

## 🧪 Testing

Testing will be added throughout development.

Planned testing includes:

* Django unit tests
* API testing
* Authentication testing
* Resume upload testing
* NLP pipeline testing
* Matching/scoring evaluation
* Edge-case testing

---

## 📈 Future Improvements

Possible future improvements include:

* Better semantic candidate matching
* Improved skill extraction
* Experience-aware scoring
* Explainable candidate scoring
* Multiple job postings
* Candidate comparison
* Resume analytics
* Recruiter analytics dashboard
* Background processing for large-scale screening
* Containerized deployment
* Cloud deployment

---

## 👨‍💻 Development Philosophy

This project is being developed incrementally, starting with the backend and core data models before integrating the AI/ML pipeline.

The goal is to demonstrate the complete lifecycle of a practical AI-powered application:

```text
Problem
  ↓
System Design
  ↓
Backend Development
  ↓
Data Processing
  ↓
Machine Learning
  ↓
API Integration
  ↓
Testing
  ↓
Deployment
```

---

## 📌 Project Status

**Status:** 🚧 Work in Progress

This repository is actively being developed. Features, architecture, and implementation details may change as the project evolves.

---

## 📄 License

This project is currently being developed as a personal portfolio project.
