from datetime import datetime

import os

import mjournal.Settings


class Entries:

    def split_id_to_date(entry_id):
        dt = datetime.strptime(entry_id, '%Y-%m-%d')

        return (dt.year, dt.month, dt.day)

    def create_paths(self, year, month, day):
        year_path = os.path.join(save_loc, year)
        month_path = os.path.join(year_path, month)
        day_path = os.path.join(month_path, day)

        if not os.path.exists(year_path):
            os.makedirs(year_path)

        if not os.path.exists(month_path):
            os.makedirs(month_path)

        if not os.path.exists(day_path):
            os.makedirs(day_path)

    def save_entry(self, entry_id, content):
        year, month, day = self.split_id_to_date(entry_id)

        save_loc = Settings.get_save_loc()


