import os

from flask import Flask
from flask import render_template, send_from_directory


server_loc = os.path.dirname(os.path.abspath(__file__))

template_loc = os.path.join(server_loc, 'templates')
server = Flask('mjournal', template_folder=template_loc)

def get_template_content(filename):
    global server_loc

    path = os.path.join(server_loc, 'templates', filename)

    with open(path, 'r') as myfile:
        data = myfile.read().replace('\n', '')

    return data

@server.route("/")
def index():
    return render_template('index.html',
        home_template=get_template_content('home.html'),
        write_template=get_template_content('write.html'),
        settings_template=get_template_content('settings.html')
    )

@server.route('/js/<path:path>')
def send_js(path):
    global server_loc

    js_loc = os.path.join(server_loc, 'static', 'js')

    return send_from_directory(js_loc, path)

@server.route('/css/<path:path>')
def send_css(path):
    global server_loc

    css_loc = os.path.join(server_loc, 'static', 'css')

    return send_from_directory(css_loc, path)

def run_server():
    global server

    '''
    UPDATE templates on change
    '''
    server.config['TEMPLATES_AUTO_RELOAD'] = 'true'

    server.run(port=8786)
