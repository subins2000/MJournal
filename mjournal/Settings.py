import os

from PyQt5.QtCore import QSettings


class Settings:

    root_loc = None

    def __init__(self, root_loc):
        self.root_loc = root_loc

    def get_value(self, key):
        settings = QSettings('mjournal', 'mjournal')
        return settings.value(key)

    '''
    Get path to data folder
    '''
    def get_save_loc(self):
        save_loc = self.get_value('save_loc')

        if save_loc:
            return save_loc
        else:
            data_path = os.path.join(self.root_loc, 'data')

            if not os.path.exists(data_path):
                os.makedirs(data_path)

            return data_path

    '''
    Get path to data/entries
    '''
    def get_entries_save_loc(self):
        enties_path = os.path.join(self.get_save_loc(), 'data')

        if not os.path.exists(enties_path):
            os.makedirs(enties_path)

        return enties_path
