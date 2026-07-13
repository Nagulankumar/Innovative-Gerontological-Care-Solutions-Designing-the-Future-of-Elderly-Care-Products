# 💊 MedRemind — Web Version

A browser-based version of the Medicine & Health Reminder System, built with **Flask**. Same core logic as the console app (Python + JSON storage), with a clean, elderly-friendly web interface — designed for a portfolio/demo, alongside the console version used for your actual submission.

---

## 🎨 Design Notes

- **Font:** Atkinson Hyperlegible — a typeface specifically designed for readers with low vision, chosen deliberately since this app is built for elderly users.
- **Large touch targets & big text** — buttons and cards are sized for users who may not be comfortable with small UI elements.
- **Color-coded status** — Due (amber), Upcoming (soft gold), Taken (green) — colour plus text label, never colour alone, for accessibility.
- **"Next Dose" hero card** — the single most important piece of information (what to take right now) is always the first thing visible, full-width, at the top.

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python app.py
```

Then open your browser to:
```
http://localhost:5000
```

---

## 📂 Project Structure

```
webapp/
├── app.py                 # Flask backend (routes + logic)
├── templates/
│   └── index.html         # Main dashboard page (Jinja2)
├── static/
│   └── style.css          # Design system + styling
├── medicines.json          # Data storage (auto-created/updated)
├── requirements.txt
└── README.md
```

---

## ✨ Features

| Feature | Description |
|---|---|
| Next Dose hero | Shows the most urgent medicine front and center |
| Add Medicine | Popup form to add a new reminder |
| Mark as Taken / Undo | One-click status toggle |
| Delete | Remove a medicine with confirmation |
| Reset Day | Clear all "taken" flags for a new day |
| Health Tip | Rotates daily, based on the day of the year |
| Fully responsive | Works on desktop, tablet, and mobile |

---

## 🔑 Notes for Your Viva

- This is the **portfolio/demo version** — your actual internal assessment submission is the **console version** (`medicine_reminder.py`), which is simpler and matches what was asked.
- Both versions share the same underlying logic: JSON-based storage, Due/Upcoming/Taken classification by comparing scheduled time to current time.
- Built using Flask (Python web framework) + Jinja2 templating — no JavaScript framework, no database — kept intentionally simple and dependency-light.
