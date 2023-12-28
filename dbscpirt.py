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
    
    def get_all_rooms(self):
        self.connect()
        self.cursor.execute(''' SELECT * FROM rooms ''')
        data = self.cursor.fetchall()
        self.close()
        return data