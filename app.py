from flask import Flask, render_template, request
from model.recommender import recommend_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = None

    if request.method == "POST":
        skills = request.form["skills"]
        recommendations = recommend_jobs(skills)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)