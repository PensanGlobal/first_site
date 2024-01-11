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
    return render_template("rooms.html", rooms=rooms)


@app.route("/rooms/<id>", methods=['GET', 'POST'])
def room_page(id):
    room = db.get_room(id)
    if request.method == 'POST':
        session["room_id"] = room[0]
        if "petsitter_id" in session:
            return redirect(url_for('all_petsitters'))
        if "room_id" in session and "petsitter_id" in session:
            return redirect(url_for('booking'))
    return render_template("room.html", room=room)


@app.route("/petsitters", methods=['GET', 'POST'])
def all_petsitters():
    petsitters = db.get_all_pet_sitters()

    if request.method == 'POST':
        session["petsitter_id"] = request.form["petsitter_id"]
        if "room_id" not in session:
            return redirect(url_for('all_rooms'))
        if "room_id" in session and "petsitter_id" in session:
            return redirect(url_for('booking'))

    return render_template("petsitters.html", petsitters=petsitters)


@app.route("/booking", methods={'GET', 'POST'})
def booking():
    room = None
    petsitter = None
    if 'room_id' in session:
        room = db.get_room(session['room_id'])
    if "petsitter_id" in session:
        petsitter = db.get_petsitter(session["petsitter_id"])
    return render_template("booking.html", room=room, petsitter=petsitter)


app.run(debug=True)
