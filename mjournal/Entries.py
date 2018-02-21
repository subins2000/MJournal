from datetime import datetime

import os

from mjournal.Settings import Settings


class Entries:

    def __init__(self, root_loc):
        self.save_loc = Settings(root_loc).get_save_loc()

    def split_id_to_date(self, entry_id):
        dt = datetime.strptime(entry_id, '%Y-%m-%d')

        return (str(dt.year), str(dt.month).zfill(2), str(dt.day).zfill(2))

    def create_paths(self, year, month, day):
        year_path = os.path.join(self.save_loc, year)
        month_path = os.path.join(year_path, month)
        day_path = os.path.join(month_path, day)

        if not os.path.exists(year_path):
            os.makedirs(year_path)

        if not os.path.exists(month_path):
            os.makedirs(month_path)

        if not os.path.exists(day_path):
            os.makedirs(day_path)

    def save_entry(self, entry_id, entry_content):
        year, month, day = self.split_id_to_date(entry_id)

        self.create_paths(year, month, day)

        entry_loc = os.path.join(self.save_loc, year, month, day, 'index.md')

        entry_file = open(entry_loc, 'w')
        entry_file.write(entry_content)
        entry_file.close()

