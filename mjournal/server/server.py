import os

from flask import Flask
from flask import render_template


template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

server = Flask('mjournal', template_folder=template_dir)

@server.route("/")
def index():
    return render_template('index.html')

def run_server():
    global server

    server.run(port=8786)
