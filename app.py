from flask import Flask, render_template

from dbscpirt import PetHotelDB

app = Flask(__name__)
db = PetHotelDB()

@app.route("/")
def index():
    return render_template("index.html")
    # івіфалхфлввзпзф

@app.route("/rooms")
def all_rooms():
    rooms = db.get_all_rooms()
    return render_template("rooms.html", rooms = rooms)

@app.route("/rooms/{id}")
def room_page(id):
    room = db.get_room(id)
    return render_template("room.html", room = room)

app.run(debug=True)