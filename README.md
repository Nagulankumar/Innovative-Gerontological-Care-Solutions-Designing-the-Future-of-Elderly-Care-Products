# 💊 Medicine & Health Reminder System
### Innovative Gerontological Care Solutions — Designing the Future of Elderly Care Products

A Python-based **Medicine & Health Reminder System** designed specifically for elderly people. This application helps elderly individuals track their medicines, set reminders, and follow daily health tips.

---

## 🎯 Purpose

Elderly people often forget to take their medicines on time. This system solves that problem by:
- Storing all medicine details in one place
- Reminding which medicines are due at what time
- Tracking which medicines have been taken
- Providing daily health tips for a healthy lifestyle

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ➕ Add Medicine | Add medicine name, dosage, time, and notes |
| 📋 View All | See all medicines in a clear table format |
| ✅ Mark Taken | Mark a medicine as taken for the day |
| 🗑️ Delete | Remove a medicine from the list |
| ⏰ Check Reminders | See due, upcoming, and taken medicines |
| 🔄 Reset Daily | Reset all medicines for a new day |
| 🌟 Health Tips | 10 daily health tips for elderly care |
| 💾 Auto Save | All data saved automatically to JSON file |

---

## 🚀 How to Run

```bash
python medicine_reminder.py
```

No extra libraries needed — uses Python built-in modules only!

---

## 📋 Sample Output

```
=======================================================
     💊 MEDICINE & HEALTH REMINDER SYSTEM 💊
        Designed for Elderly Care Support
=======================================================

--- MAIN MENU ---
  1. ➕ Add Medicine Reminder
  2. 📋 View All Medicines
  3. ✅ Mark Medicine as Taken
  4. 🗑️  Delete Medicine
  5. ⏰ Check Today's Reminders
  6. 🔄 Reset Daily Status
  7. 🌟 Health Tips
  8. 🚪 Exit

--- ⏰ Checking Reminders ---
🚨 DUE NOW — Take these medicines immediately!
   💊 Metformin — 1 tablet | Note: Take after food

⏳ UPCOMING Medicines:
   🕐 20:00 → Vitamin D — 1 capsule
```

---

## 💾 Data Storage

All medicine data is saved in `medicines.json` automatically. Data is preserved even after closing the program.

---

## 🧠 Key Concepts Used

- **Functions** — Modular code structure
- **Lists & Dictionaries** — Data storage
- **JSON** — Saving and loading data
- **datetime module** — Real-time clock and date
- **File Handling** — Read/write JSON file
- **Loops & Conditions** — Menu and logic flow

---

## 👨‍💻 Author

**Nagulan**
AIML Engineering Student
Project: Innovative Gerontological Care Solutions

---

## 📄 License

Open source under [MIT License](LICENSE).
