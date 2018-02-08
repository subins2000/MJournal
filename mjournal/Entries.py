from datetime import datetime

import os

import mjournal.Settings


class Entries:

    def split_id_to_date(entry_id):
        dt = datetime.strptime(entry_id, '%Y-%m-%d')

        return (dt.year, dt.month, dt.day)

    def save_entry(self, entry_id, content):
        year, month, day = self.split_id_to_date(entry_id)

        save_loc = Settings.get_save_loc()
