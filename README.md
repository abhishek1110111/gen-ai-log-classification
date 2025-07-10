# 🧠 GenAI + NLP Log Classification System

A hybrid log classification system built from scratch using **Regex**, **BERT**, **Deepseek R1, LLaMA (LLMs)**, and **Logistic Regression** to categorize system logs into actionable categories like *Security Alerts*, *Workflow Errors*, *User Actions*, and more. The system leverages both traditional NLP and modern Generative AI, wrapped in a production-ready **FastAPI** interface.

> 🚀 Designed to support DevOps and SRE teams with smarter debugging, anomaly detection, and operational efficiency—while optimizing cost and improving accuracy.

---

## 📌 Project Highlights

- 🧹 **Hybrid Architecture** combining Regex, BERT, Logistic Regression, and LLMs (Deepseek R1, LLaMA)
- 🧠 **Zero-shot/few-shot classification** using LLaMA when labeled data is scarce
- ⚡ **FastAPI-powered REST API** for real-time log analysis and integration
- 📊 Designed for **real-world log analytics** in production environments
- ♻️ **Scalable & cost-efficient**, ideal for large-scale DevOps pipelines

---

## 🛠️ Tech Stack

| Component     | Technology                        |
| ------------- | --------------------------------- |
| NLP/Embedding | BERT, Regex, Sentence Transformer |
| GenAI         | Deepseek R1, LLaMA/LLMs           |
| Classifier    | Logistic Regression               |
| Backend/API   | FastAPI                           |
| Language      | Python                            |

---

## 🧱 Architecture Overview
![architecture](resources/project_architecture.png)


---

## 🔍 Classification Approaches

1. **Regular Expression (Regex)**

   - Rule-based, fast classification for well-defined log patterns.

2. **Sentence Transformer + Logistic Regression**

   - Uses embeddings from Sentence Transformers and Logistic Regression for supervised classification when labeled data is available.

3. **LLMs (Large Language Models)**

   - LLaMA or Deepseek R1 used for complex, low-data scenarios (zero/few-shot learning).

### 🔹 Classification Pipeline

1. **Regex Classification**\
   Quick detection using predefined rules.

2. **Unknown Logs → BERT / Deepseek R1 / LLaMA**

   - If **enough labeled data** → BERT classifier
   - If **few or no samples** → LLaMA-powered zero/few-shot classification

3. **Output** → Results are returned with classified log categories like `Security Alert`, `Workflow Error`, `User Action`, etc.

> ✅ This hybrid approach ensures high accuracy, scalability, and optimized cost-performance balance.

---

## 💡 Why Hybrid Classification?

| Benefit                  | Description                                                                 |
| ------------------------ | --------------------------------------------------------------------------- |
| 💸 **Cost Optimization** | Prioritizes fast, cheap methods (Regex/LogReg), using LLMs only when needed |
| 🌟 **Better Accuracy**   | Combines rule-based precision with contextual inference from ML/LLM         |
| 📈 **Scalability**       | Easily adapts to new log types with minimal retraining                      |
| 🔧 **Maintainability**   | Modular design enables easy upgrades and experimentation                    |

---

## 📁 Folder Structure

```
.
├── main.py                   # FastAPI server code
├── requirements.txt          # Project dependencies
├── resources/                # Output CSVs, test files, project image
├── training_dataset/
│   ├── dataset/              # Labeled training datasets
│   ├── models/               # Saved Sentence Transformer and Logistic Regression models
│   └── notebooks/            # Jupyter notebooks for model training
├── regex_classifier.py       # Regex-based classification logic
├── bert_classifier.py        # BERT model for supervised classification
├── llm_classifier.py         # LLM (Deepseek R1/LLaMA) classification
|__ .env                      # Need to API integrated LLM model
└── venv/                     # Virtual environment (optional, ignored in .git)
```

---

## ⚙️ Setup Instructions

1. **Install Dependencies**

   Make sure Python is installed, then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI Server**

   Start the server:

   ```bash
   uvicorn main:app --reload
   ```

   Once the server is up, access:

   - API base: `http://127.0.0.1:8000/`
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🚀 Usage

Upload a CSV file to the FastAPI endpoint for classification. The file **must include** the following columns:

- `source`
- `log_message`

The system will return a CSV file with an additional column:

- `target_label`: the predicted category for each log entry.

---

## 🧪 API Testing

- You can test the API using **Postman** or any other API client.
- Use the `/classify/` POST endpoint and upload a `.csv` file in `multipart/form-data` format.

