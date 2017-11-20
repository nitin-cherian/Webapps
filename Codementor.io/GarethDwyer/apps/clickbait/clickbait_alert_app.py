# clickbait_alert_app.py


# Import libraries
from flask import Flask, render_template, request
from clickbait_classifier import is_clicbait

# Create a Flask instance
app = Flask(__name__)


# View function
@app.route("/", methods=["GET", "POST"])
def alert():

    if request.form:
        headline = request.form.get('headline')
        clickbait = is_clicbait(headline)
        return render_template("headline.html", clickbait=clickbait)

    return render_template("headline.html")


if __name__ == '__main__':
    app.run(debug=True)
