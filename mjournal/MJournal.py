import _thread

from mjournal.server.server import run_server
from mjournal.app.App import App


class MJournal:

    app = None

    root_loc = None

    '''
    root_loc - Root location of MJournal
    '''
    def __init__(self, root_loc = None):
        self.root_loc = root_loc

    def run_server(self):
        _thread.start_new_thread(run_server, (self.root_loc,))

    def run_app(self):
        self.app = App()
        self.app.run()

    def run(self):
        self.run_server()
        self.run_app()
