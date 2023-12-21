import sqlite3
class PetHotelDB:
    def __init__(self):
        self.name = 'pethotel.db'
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()