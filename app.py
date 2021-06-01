import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("home.j2")

@app.route("/li")
def li():
    return flask.redirect("https://www.linkedin.com/in/martin-meneval/")

@app.route("/resume")
def resume():
    return flask.render_template("resume.j2")
