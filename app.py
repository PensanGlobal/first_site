from flask import Flask, render_template

from dbscpirt import PetHotelDB

app = Flask(__name__)
db = PetHotelDB()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rooms")
def all_rooms():
    rooms = db.get_all_rooms()
    return render_template("rooms.html", rooms = rooms)

@app.route("/rooms/<id>")
def room_page(id):
    room = db.get_room(id)
    return render_template("room.html", room = room)

@app.route("/petsitters")
def all_petsitters():
    petsitters = db.get_all_pet_sitters()
    return render_template("petsitters.html", petsitters = petsitters)

app.run(debug=True)