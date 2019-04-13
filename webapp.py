#!/usr/bin/env python
import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template('index.html',front=True,title="a good news organizer")

if __name__ == '__main__': app.run()
