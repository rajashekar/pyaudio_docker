from flask import Flask, render_template
import tensorflow as tf
import pyaudio

application = app = Flask(__name__, template_folder="static")


@app.route("/")
def index():
    """Return the client application."""
    return render_template("main.html", tf_version=tf.__version__, pyaudio_version=pyaudio.__version__)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
