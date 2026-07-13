from flask import Flask, render_template, request, redirect, url_for
import json
import os
import datetime

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "medicines.json")

HEALTH_TIPS = [
    "Drink at least 8 glasses of water daily.",
    "Take a 15-minute walk every morning.",
    "Eat fresh fruits and vegetables every day.",
    "Sleep at least 7-8 hours per night.",
    "Never skip your prescribed medicines.",
    "Keep your mind active — read books or solve puzzles.",
    "Visit your doctor for regular check-ups.",
    "Practice deep breathing to reduce stress.",
    "Brush your teeth twice daily for good oral health.",
    "Get some sunlight every day for Vitamin D.",
]


def load_medicines():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_medicines(medicines):
    with open(DATA_FILE, "w") as f:
        json.dump(medicines, f, indent=4)


def next_id(medicines):
    return (max([m["id"] for m in medicines]) + 1) if medicines else 1


def classify(medicines, current_time):
    due, upcoming, taken = [], [], []
    for m in medicines:
        if m["taken"]:
            taken.append(m)
        elif m["time"] <= current_time:
            due.append(m)
        else:
            upcoming.append(m)
    upcoming.sort(key=lambda m: m["time"])
    return due, upcoming, taken


@app.route("/")
def dashboard():
    medicines = load_medicines()
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    due, upcoming, taken = classify(medicines, current_time)

    if due:
        next_dose = due[0]
        next_status = "due"
    elif upcoming:
        next_dose = upcoming[0]
        next_status = "upcoming"
    else:
        next_dose = None
        next_status = "done"

    tip = HEALTH_TIPS[now.timetuple().tm_yday % len(HEALTH_TIPS)]

    return render_template(
        "index.html",
        medicines=medicines,
        due=due,
        upcoming=upcoming,
        taken=taken,
        next_dose=next_dose,
        next_status=next_status,
        current_date=now.strftime("%A, %d %B %Y"),
        current_time=now.strftime("%I:%M %p"),
        tip=tip,
        total=len(medicines),
        taken_count=len(taken),
    )


@app.route("/add", methods=["POST"])
def add_medicine():
    medicines = load_medicines()
    name = request.form.get("name", "").strip()
    dosage = request.form.get("dosage", "").strip()
    time_str = request.form.get("time", "").strip()
    note = request.form.get("note", "").strip()

    if name and dosage and time_str:
        medicines.append({
            "id": next_id(medicines),
            "name": name,
            "dosage": dosage,
            "time": time_str,
            "note": note if note else "No special note",
            "taken": False,
        })
        save_medicines(medicines)

    return redirect(url_for("dashboard"))


@app.route("/take/<int:med_id>", methods=["POST"])
def mark_taken(med_id):
    medicines = load_medicines()
    for m in medicines:
        if m["id"] == med_id:
            m["taken"] = True
    save_medicines(medicines)
    return redirect(url_for("dashboard"))


@app.route("/undo/<int:med_id>", methods=["POST"])
def undo_taken(med_id):
    medicines = load_medicines()
    for m in medicines:
        if m["id"] == med_id:
            m["taken"] = False
    save_medicines(medicines)
    return redirect(url_for("dashboard"))


@app.route("/delete/<int:med_id>", methods=["POST"])
def delete_medicine(med_id):
    medicines = load_medicines()
    medicines = [m for m in medicines if m["id"] != med_id]
    save_medicines(medicines)
    return redirect(url_for("dashboard"))


@app.route("/reset", methods=["POST"])
def reset_daily():
    medicines = load_medicines()
    for m in medicines:
        m["taken"] = False
    save_medicines(medicines)
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
