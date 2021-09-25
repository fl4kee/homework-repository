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
