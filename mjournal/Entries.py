import mjournal.Settings


class Entries:

    def __init__(self):
        self.save_loc = Settings.get_save_loc()

    def save_entry(self, id, content):
        self.save_loc()
