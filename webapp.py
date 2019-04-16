#!/usr/bin/env python
import flask
import utils

app = flask.Flask(__name__)
_pyversion = utils.pyversion()

@app.route("/")
def hello():
    #return flask.render_template('index.html',front=True,title="a good news organizer")
    return flask.render_template('index.html',pyversion=_pyversion)

if __name__ == '__main__': app.run()
