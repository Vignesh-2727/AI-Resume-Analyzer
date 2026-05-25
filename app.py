from flask import Flask, render_template, request

app = Flask(__name__)

skills = ["python", "sql", "html", "css", "machine learning"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        resume_text = request.form["resume"].lower()

        found_skills = []
        missing_skills = []

        for skill in skills:
            if skill in resume_text:
                found_skills.append(skill)
            else:
                missing_skills.append(skill)

        score = min(len(found_skills) * 15, 100)

        result = {
            "score": score,
            "found": found_skills,
            "missing": missing_skills
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)