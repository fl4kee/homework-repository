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


class TableData:
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.c = sqlite3.connect(db_name).cursor()

    def get_data(self):
        return self.c.execute(f"SELECT * FROM {self.table_name}")

    def __iter__(self):
        return self.get_data()

    def __next__(self):
        data = self.get_data()
        return data.fetchone()

    def __len__(self):
        return sum(1 for _ in self.get_data())

    def __getitem__(self, l_name):
        for president in self.get_data():
            if l_name in president:
                return president
