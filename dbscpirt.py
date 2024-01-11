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
    
    def get_room(self,room_id):
        self.connect()
        self.cursor.execute(''' SELECT * FROM rooms WHERE id=(?)''', [room_id])
        data = self.cursor.fetchone()
        self.close()
        return data
    
    def get_all_pet_sitters(self):
        self.connect()
        self.cursor.execute(''' SELECT * FROM pet_sitters ''')
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_petsitter(self,petsitter_id):
        self.connect()
        self.cursor.execute(''' SELECT * FROM pet_sitters WHERE id=(?)''', [petsitter_id])
        data = self.cursor.fetchone()
        self.close()
        return data
    
    def new_booking(self):
        self.connect()
        self.cursor.execute(''' INSERT INTO bookings() VALUES() ''')
        self.conn.commit()
        self.close()