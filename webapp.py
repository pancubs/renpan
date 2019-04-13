#!/usr/bin/env python
import flask

app = flask.Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    return flask.render_template('index.html',front=True,title="a good news organizer")

@app.route('/css/<path:path>')
def serve_css(path):
    return flask.send_from_directory('css', path)

if __name__ == '__main__': app.run()
