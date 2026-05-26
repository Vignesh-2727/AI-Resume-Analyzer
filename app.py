from flask import Flask, render_template, request

app = Flask(__name__)

skills = [
    "python",
    "sql",
    "html",
    "css",
    "machine learning",
    "java",
    "communication",
    "teamwork"
]

skill_recommendations = {
    "python": "Learn Python basics and practice mini projects.",
    "sql": "Practice SQL queries and database basics.",
    "html": "Improve frontend basics with HTML forms and layouts.",
    "css": "Learn styling to improve UI design.",
    "machine learning": "Start with basic ML concepts and models.",
    "java": "Practice OOP concepts in Java.",
    "communication": "Work on speaking and presentation skills.",
    "teamwork": "Participate in collaborative projects."
}


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        resume_text = request.form["resume"].lower()

        found_skills = []
        missing_skills = []
        recommendations = []

        for skill in skills:

            if skill in resume_text:
                found_skills.append(skill)

            else:
                missing_skills.append(skill)
                recommendations.append(
                    skill_recommendations[skill]
                )

        score = min(len(found_skills) * 15, 100)

        job_role = "General Software Intern"

        if "python" in found_skills and "sql" in found_skills:
            job_role = "Data Analyst Intern"

        elif "html" in found_skills and "css" in found_skills:
            job_role = "Web Developer Intern"

        elif "machine learning" in found_skills and "python" in found_skills:
            job_role = "AIML Intern"

        score_color = "red"

        if score >= 70:
            score_color = "green"

        elif score >= 40:
            score_color = "orange"

        result = {
            "score": score,
            "found": found_skills,
            "missing": missing_skills,
            "recommendations": recommendations,
            "job_role": job_role,
            "score_color": score_color
        }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)