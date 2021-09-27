# Write a wrapper class TableData for database table, that when initialized
# with database name and table acts as collection object (implements Collection protocol).
# Assume all data has unique values in 'name' column.
# So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')
# then
# len(presidents) will give current amount of rows in presidents table in database
# presidents['Yeltsin'] should return single data row for president with name Yeltsin
# 'Yeltsin' in presidents should return if president with same name exists in table
# object implements iteration protocol. i.e. you could use it in for loops::
# for president in presidents:
# print(president['name'])
# all above mentioned calls should reflect most recent data.
# If data in table changed after you created collection instance,
# your calls should return updated data.
# Avoid reading entire table into memory. When iterating through records,
# start reading the first record, then go to the next one, until records are exhausted.
# When writing tests, it's not always neccessary to mock database calls completely.
# Use supplied example.sqlite file as database fixture file.
import sqlite3
from pathlib import Path
from typing import Dict


class TableData:
    def __init__(self, db_name: Path, table_name: str):
        self.table_name = table_name
        self.c = sqlite3.connect(db_name).cursor()
        self._current_row = 0

    def get_data(self, row: int) -> sqlite3.Cursor:
        return self.c.execute(f"SELECT * FROM {self.table_name} LIMIT 1 OFFSET {row}")

    def __iter__(self):
        return self

    def __next__(self) -> Dict:
        next_row = self._current_row
        self._current_row += 1
        if self._current_row > self.__len__():
            self.current_row = 0
            raise StopIteration
        name, age, country = self.get_data(next_row).fetchone()
        return {'name': name, 'age': age, 'country': country}

    def __len__(self) -> int:
        len_ = self.c.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        return len_.fetchone()[0]

    def __getitem__(self, l_name: str) -> Dict:
        president = self.c.execute(f"SELECT * FROM {self.table_name} WHERE name LIKE '%{l_name}%'")
        return president.fetchone()
