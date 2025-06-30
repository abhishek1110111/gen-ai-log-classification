# 🧠 GenAI + NLP Log Classification System

A hybrid log classification system built from scratch using **Regex**, **BERT**, **Deepseek R1, LLaMA (LLMs)**, and **Logistic Regression** to categorize system logs into actionable categories like *Security Alerts*, *Workflow Errors*, *User Actions*, and more. The system leverages the power of traditional NLP and modern Generative AI, wrapped in a production-ready **FastAPI** interface.

> 🚀 Designed to support DevOps and SRE teams with smarter debugging, anomaly detection, and operational efficiency—while optimizing cost and improving accuracy.

---

## 📌 Project Highlights

- 🧩 **Hybrid Architecture** combining Regex, BERT, Logistic Regression, and LLMs (Deepseek R1, LLaMA)
- 🧠 **Zero-shot/few-shot classification** using LLaMA when labeled data is scarce
- ⚡ **FastAPI-powered REST API** for real-time log analysis and integration
- 📊 Designed for **real-world log analytics** in production environments
- 🔁 **Scalable & cost-efficient**, ideal for large-scale DevOps pipelines

---

## 🧱 Architecture Overview

### 🔷 Classification Pipeline:
1. **Regex Classification**  
   Fast, rule-based classification for known log patterns

2. **Unknown Logs → BERT / Deepseek R1 / LLaMA**
   - If **enough labeled data** → BERT classifier
   - If **few or no samples** → LLaMA-powered LLM for contextual classification

3. **Output → DevOps / SRE, SDE Teams**
   Based on log category: alerting, workflow error, user action, etc.

> ✅ This architecture ensures high accuracy, scalability, and optimized cost-performance balance.

---

## 💡 Why Hybrid Classification?

| Benefit               | Description |
|-----------------------|-------------|
| 💸 **Cost Optimization** | Prioritizes fast, cheap methods (Regex/LogReg), using LLMs only when needed |
| 🎯 **Better Accuracy**   | Combines rule-based precision with learned contextual inference |
| 📈 **Scalability**       | Adapts to new log types with minimal retraining |
| 🔧 **Maintainability**   | Modular design for easy upgrades and experimentation |

---

## 🛠️ Tech Stack

| Component      | Technology                |
|----------------|---------------------------|
| NLP/Embedding  | BERT, Regex, TF-IDF       |
| GenAI          | Deepseek R1, LLaMA / LLMs |
| Classifier     | Logistic Regression       |
| Backend/API    | FastAPI                   |
| Language       | Python                    |

---
