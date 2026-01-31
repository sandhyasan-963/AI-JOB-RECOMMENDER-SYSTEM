# 🤖 AI Job Recommender System

An AI-powered web application that recommends job roles based on user skills using similarity matching.

---

## 🚀 Features
- User enters skills (space separated)
- AI model analyzes skill relevance
- Job roles ranked with match percentage
- Simple and clean UI
- Real-time recommendations

---

## 🛠️ Tech Stack
- Python
- Flask
- HTML
- CSS
- Basic Machine Learning (Similarity Matching)

---

## 📂 Project Structure
ai_job_recommender/ │ ├── app.py ├── recommender.py ├── data/ │   └── jobs.csv ├── templates/ │   └── index.html ├── static/ 
|── style.css └── README.md
---

## ⚙️ How It Works
1. User enters skills
2. Skills are processed by AI logic
3. Similarity score calculated for each job role
4. Jobs displayed with match percentage

---

## ▶️ How to Run the Project
```bash
pip install flask
python app.py
