# 🛡️ Phishing Email Detection System using NLP & Machine Learning

Phishing emails remain one of the most common and effective cybersecurity threats, exploiting human trust rather than technical vulnerabilities. This project focuses on building an **end-to-end phishing email detection system** using **Natural Language Processing (NLP)** and **machine learning**, deployed as an **interactive web application** for real-time inference.
<img width="1740" height="897" alt="image" src="https://github.com/user-attachments/assets/a5ed8329-85c2-45e9-9d53-2c9327f944ef" />

🔗 Web Link - https://detectemail.streamlit.app/

---

## 🚀 Project Overview

The goal of this project is to automatically classify emails as **phishing** or **legitimate** based on their textual content. The system processes raw email text, extracts meaningful linguistic features, and applies supervised machine learning models to make accurate predictions.

Key highlights:
- End-to-end **ML pipeline**: data preprocessing → modeling → evaluation → deployment
- Focus on **realistic phishing emails** that closely resemble genuine communication
- Fully deployed and accessible via a **Streamlit web interface**

---

## 📊 Dataset

The model was trained on a labeled dataset containing both phishing and legitimate email samples. The dataset includes a wide range of email styles, tones, and structures, helping the model generalize to real-world phishing attempts.

**Dataset characteristics:**
- Binary labels: `phishing` vs `legitimate`
- Text-based features extracted from email body
- Balanced to mitigate class bias

---

## 🧹 Data Preprocessing & NLP Pipeline

Before modeling, raw email text undergoes several preprocessing steps to reduce noise and improve signal quality:

- Text normalization (lowercasing)
- Tokenization using **NLTK**
- Stopword removal
- Stemming to reduce words to their root forms
- Reconstruction of cleaned text for vectorization

This preprocessing pipeline ensures consistent and meaningful feature extraction.

---

## 🧠 Feature Engineering

The cleaned text is transformed into numerical representations using:
- **Bag-of-Words / TF-IDF vectorization**
- Sparse feature matrices suitable for classical ML models

These features capture word frequency patterns commonly associated with phishing behavior.

---

## 🤖 Model Training & Evaluation

Multiple supervised learning models were trained and evaluated, including:
- Logistic Regression
- Naive Bayes
- Support Vector Machines (SVM)

Models were assessed using standard classification metrics:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**

The final model was selected based on its ability to balance precision and recall, minimizing false negatives (missed phishing emails).

---

## 🌐 Deployment

The trained model was deployed as an interactive **Streamlit web application**, allowing users to:
- Paste raw email text
- Instantly receive a phishing or legitimate prediction
- Test edge cases and realistic phishing samples

Deployment considerations included:
- Cloud-safe handling of NLTK resources
- Model serialization using `joblib`
- Lightweight, reproducible environment setup

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **NLP:** NLTK  
- **Machine Learning:** Scikit-learn  
- **Deployment:** Streamlit  
- **Version Control:** Git & GitHub  

---

## 📌 Key Learnings

- Realistic phishing emails require nuanced linguistic modeling
- NLP preprocessing significantly impacts downstream model performance
- Deployment environments differ from local setups and require careful dependency handling
- Even classical ML models can perform strongly with well-engineered features

---

## 🔮 Future Improvements

- Incorporate deep learning models (LSTM / Transformers)
- Add URL and metadata-based features
- Expand dataset with multilingual phishing samples
- Integrate explainability tools (e.g., SHAP) for prediction transparency

---

## 📎 Conclusion

This project demonstrates how **NLP and machine learning** can be effectively combined to tackle real-world cybersecurity problems. By focusing on realistic data, robust preprocessing, and deployable design, the system bridges the gap between experimentation and production-ready ML applications.

---

⭐ If you found this project interesting, feel free to star the repository and explore the code!
