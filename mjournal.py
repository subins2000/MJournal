import os

from mjournal_app.MJournal import MJournal

dir_path = os.path.dirname(os.path.realpath(__file__))

MJournal(dir_path).run()
