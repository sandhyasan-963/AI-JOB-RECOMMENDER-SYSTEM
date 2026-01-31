import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_jobs(user_skills):
    jobs = pd.read_csv("data/jobs.csv")

    job_texts = jobs["skills"].tolist()
    all_texts = job_texts + [user_skills]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    similarity_scores = cosine_similarity(
        tfidf_matrix[-1], tfidf_matrix[:-1]
    )[0]

    recommendations = []

    for idx, score in enumerate(similarity_scores):
        recommendations.append({
            "job": jobs.iloc[idx]["job_title"],
            "score": round(score * 100, 2)
        })

    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations