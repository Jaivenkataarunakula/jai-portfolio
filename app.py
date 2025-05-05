from flask import Flask, render_template

app = Flask(__name__)

# Maintenance mode toggle
under_construction = True  # Set to False when site is ready

home_content = {
    "name": "Jai Venkata Arun",
    "title": "Hi, I'm Jai Venkata Arun 👋",
    "tagline": "Crafting digital systems, solving real problems.",
    "bio": "I'm a Computer Science grad student and Python backend developer passionate about automation, cloud, and innovation.",
    "resume_link": "jai_resume.pdf",
    "linkedin": "https://www.linkedin.com/in/jaivenkataarunakula",
}


@app.route("/")
def home():
    if under_construction:
        return render_template("coming_soon.html")
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
