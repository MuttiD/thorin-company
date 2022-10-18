import os
from flask import Flask, render_template


app = Flask(__name__)

# routing to the index "/"
@app.route("/")
def index():
    return render_template("index.html")


# routing to the about page "/about"
@app.route("/about")
def about():
    return render_template("about.html")


# routing to the contact page "/contact"
@app.route("/contact")
def contact():
    return render_template("contact.html")


# routing to the careers page "/careers"
@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)