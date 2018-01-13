import thread

from mjournal.server import Server
from mjournal.app import *


class MJournal:

    def run_server(self):
        thread.start_new_thread(Server.run, ())

    def run(self):
        self.run_server()
        self.run_app()
