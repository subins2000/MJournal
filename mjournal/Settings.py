import os

from PyQt5.QtCore import QSettings


class Settings:

    def get_value(self, key):
        settings = QSettings('mjournal', 'mjournal')
        return settings.value(key)

    def get_save_loc(self):
        save_loc = self.get_value('save_loc')

        if save_loc:
            return save_loc
        else:
            return os.path.join(root_loc, 'data', 'entries')
