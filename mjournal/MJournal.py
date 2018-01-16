import _thread

from mjournal.server.server import run_server
from mjournal.app.App import App


class MJournal:

    app = None

    def run_server(self):
        _thread.start_new_thread(run_server, ())

    def run_app(self):
        self.app = App()
        self.app.run()

    def run(self):
        self.run_server()
        self.run_app()
