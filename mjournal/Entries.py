from datetime import datetime

import json
import os

from mjournal.Settings import Settings


class Entries:

    def __init__(self, root_loc):
        self.entries_save_loc = Settings(root_loc).get_entries_save_loc()

    def split_id_to_date(self, entry_id):
        dt = datetime.strptime(entry_id, '%Y-%m-%d')

        return (str(dt.year), str(dt.month).zfill(2), str(dt.day).zfill(2))

    def create_paths(self, year, month, day):
        year_path = os.path.join(self.entries_save_loc, year)
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

        entry_loc = os.path.join(self.entries_save_loc, year, month, day, 'entry.md')

        entry_file = open(entry_loc, 'w')
        entry_file.write(entry_content)
        entry_file.close()

        entry_info = {
            'date': '%s-%s-%s' % (year, month, day)
        }
        entry_info = json.dumps(entry_info)

        entry_info_loc = os.path.join(self.entries_save_loc, year, month, day, 'entry.json')

        entry_info_file = open(entry_info_loc, 'w')
        entry_info_file.write(entry_info)
        entry_info_file.close()

    def update_index_cache(self):
        i = 0
        entries = {}

        for location, folders, files in os.walk(self.entries_save_loc):
            for file in files:
                if file == 'entry.md':
                    try:
                        entry_info_f = open(os.path.join(location, 'entry.json'), 'r')
                        entry_info = json.load(entry_info_f)
                        entry_info_f.close()

                        entries[entry_info['date']] = {
                            'date': entry_info['date'],
                            'path': location
                        }

                        i += 1

                    except Exception as e:
                        pass

        index_f = open(os.path.join(self.entries_save_loc, 'index.json'), 'w')
        index_f.write(json.dumps(entries))
        index_f.close()

    def get_all_entries(self):
        index_f = open(os.path.join(self.entries_save_loc, 'index.json'), 'r')
        index = json.load(index_f)
        index_f.close()

        return index
