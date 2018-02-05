import os

from mjournal.MJournal import MJournal

dir_path = os.path.dirname(os.path.realpath(__file__))

MJournal().run()
