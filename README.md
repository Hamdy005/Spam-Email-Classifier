# 📨 Spam Email Classifier (Machine Learning + Streamlit)

A simple and effective **Spam Detection Web App** built with **Streamlit**.  
It analyzes email text using NLP preprocessing and a trained machine learning model to classify messages as **Spam** or **Ham (Not Spam)**.

---

## 🔐 Requirements (Before Running)

| Requirement | Purpose | Needed? |
|------------|---------|---------|
| Python 3.8+ | Run the project | ✅ Yes |
| Virtual Environment (venv) | Keep dependencies isolated | 🔄 Recommended |
| requirements.txt | Install all needed libraries | ✅ Yes |

---

## ⭐ Key Features

- User-friendly Streamlit interface  
- Predicts **Spam** or **Ham** from email text  
- Clean NLP preprocessing pipeline  
- Uses a **saved TF-IDF Vectorizer**  
- Loads a trained machine learning model  
- Instant predictions with high accuracy  

---

## 🧠 How the App Works (Simple Explanation)

1. User enters an email message  
2. Text is cleaned using NLP preprocessing  
3. The **saved TF-IDF vectorizer** converts text into numerical features  
4. The **machine learning model** predicts:
   - ✔ **Ham (Safe)**  
   - ❌ **Spam (Suspicious)**  
5. Result is displayed immediately

---

## 🔧 Tools & Technologies Used

| Component | Technology |
|----------|------------|
| Web Interface | Streamlit |
| ML Model | Scikit-learn |
| Vectorizer | TF-IDF |
| NLP Tools | NLTK / Regex |
| Data Handling | Pandas / NumPy |
| Model Storage | Pickle (.pkl files) |

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/spam-email-classifier
cd spam-email-classifier
```

### 2️⃣ Create a Virtual Environment (venv)
```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```