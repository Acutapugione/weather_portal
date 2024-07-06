from flask import render_template, redirect, url_for

from .. import app

@app.get('/')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('weather'))

    return redirect(url_for('index'))