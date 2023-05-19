from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from flask.globals import request
from datetime import timedelta
import os

from api.forms import URLForm

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=5)
app.config["SESSION_FILE_THRESHOLD"] = 100

sess = Session()
sess.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():
    form = URLForm()

    if form.validate_on_submit():
        session.clear()

        session["url"] = form.url.data
        if form.checkbox.data:  # Custom introspection from file
            session["introspection"] = request.files[form.file.name].read()

        return redirect(url_for("graphiql"))

    return render_template("index.html", form=form)


@app.route("/graphiql")
def graphiql():
    url = session.get("url")
    custom_introspection = bool(session.get("introspection"))

    if url:
        return render_template("graphiql.html", url=url, custom_introspection=custom_introspection)
    else:
        return redirect(url_for("index"))


@app.route("/introspection", methods=["POST"])
def introspection():
    return session.get("introspection")


@app.route("/help/1")
def help1():
    url = f"https://{request.host}/"

    return render_template("help1.html", url=url)


@app.route("/help/2")
def help2():
    return render_template("help2.html")
