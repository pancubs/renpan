#!/usr/bin/env python
import flask
import utils as _utils
import platform as _platform

from settings import production_mode,db

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template('index.html',pyversion=_utils.pyversion(),distro=_platform.linux_distribution())

if __name__ == '__main__': app.run(debug=not(production_mode))
