from flask import Flask, render_template, request, session, redirect, url_for

from dbscpirt import PetHotelDB

app = Flask(__name__)
app.config["SECRET_KEY"] = "kasidjasjfpwjpesmdaoskdw"
db = PetHotelDB()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rooms")
def all_rooms():
    rooms = db.get_all_rooms()
    return render_template("rooms.html", rooms = rooms)

@app.route("/rooms/<id>", methods=['GET', 'POST'])
def room_page(id):
    room = db.get_room(id)
    if request.method == 'POST':
        session["room_id"] = room[0]
        return redirect(url_for('all_petsitters'))
        print(room[0])
    return render_template("room.html", room = room)

@app.route("/petsitters", methods=['GET', 'POST'])
def all_petsitters():
    petsitters = db.get_all_pet_sitters()
    if request.method == 'POST':
        session["petsitter_id"] = request.form["petsitter_id"]
        # return redirect(url_for('all_petsitters'))

    return render_template("petsitters.html", petsitters = petsitters)

app.run(debug=True)