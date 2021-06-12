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

@app.route("/dl_resume")
def dl_resume():
    return flask.send_file("static/resume.pdf",
                     mimetype='application/pdf',
                     attachment_filename='Resume_Martin_Meneval.pdf',
                     as_attachment=True)
