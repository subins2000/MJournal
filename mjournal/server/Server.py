from flask import Flask
from flask import render_template


class Server:

    def __init__(self):

        self.app = Flask(__name__)

        self.routes()

    def routes(self):

        @self.app.route("/")
        def index():
            return render_template('index.html')

    def run(self):
        self.app.run()

