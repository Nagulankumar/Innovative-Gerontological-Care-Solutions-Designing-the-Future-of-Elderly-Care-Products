# ============================================================
# 💊 Medicine & Health Reminder System
# Author      : Nagulan
# Description : A Python-based medicine reminder system for
#               elderly care — tracks medicines, schedules,
#               and daily health tips.
# ============================================================

import time
import datetime
import json
import os

# ============================================================
# STEP 1: Medicine Database (stored as a list)
# ============================================================

medicines = []

# ============================================================
# STEP 2: Helper Functions
# ============================================================

def display_banner():
    print("\n" + "=" * 55)
    print("     💊 MEDICINE & HEALTH REMINDER SYSTEM 💊")
    print("        Designed for Elderly Care Support")
    print("=" * 55)

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M")

def get_current_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")

def save_medicines():
    with open("medicines.json", "w") as f:
        json.dump(medicines, f, indent=4)
    print("✅ Medicine data saved successfully!")

def load_medicines():
    global medicines
    if os.path.exists("medicines.json"):
        with open("medicines.json", "r") as f:
            medicines = json.load(f)
        print(f"✅ Loaded {len(medicines)} medicine(s) from saved data.")
    else:
        medicines = []

# ============================================================
# STEP 3: Add Medicine
# ============================================================

def add_medicine():
    print("\n--- ➕ Add New Medicine ---")
    name     = input("Medicine Name       : ").strip()
    dosage   = input("Dosage (e.g. 1 tab) : ").strip()
    time_str = input("Reminder Time (HH:MM): ").strip()
    note     = input("Special Note (optional, press Enter to skip): ").strip()

    medicine = {
        "id"      : len(medicines) + 1,
        "name"    : name,
        "dosage"  : dosage,
        "time"    : time_str,
        "note"    : note if note else "No special note",
        "taken"   : False
    }

    medicines.append(medicine)
    save_medicines()
    print(f"\n✅ '{name}' reminder added for {time_str}!")

# ============================================================
# STEP 4: View All Medicines
# ============================================================

def view_medicines():
    print("\n--- 📋 All Medicine Reminders ---")
    if not medicines:
        print("⚠️  No medicines added yet!")
        return

    print(f"\n{'ID':<5} {'Medicine':<20} {'Dosage':<15} {'Time':<10} {'Taken':<8} {'Note'}")
    print("-" * 75)
    for m in medicines:
        status = "✅ Yes" if m["taken"] else "❌ No"
        print(f"{m['id']:<5} {m['name']:<20} {m['dosage']:<15} {m['time']:<10} {status:<8} {m['note']}")

# ============================================================
# STEP 5: Mark Medicine as Taken
# ============================================================

def mark_taken():
    view_medicines()
    if not medicines:
        return
    try:
        med_id = int(input("\nEnter Medicine ID to mark as taken: "))
        for m in medicines:
            if m["id"] == med_id:
                m["taken"] = True
                save_medicines()
                print(f"✅ '{m['name']}' marked as taken! Great job! 💪")
                return
        print("❌ Medicine ID not found!")
    except ValueError:
        print("❌ Please enter a valid number!")

# ============================================================
# STEP 6: Delete Medicine
# ============================================================

def delete_medicine():
    view_medicines()
    if not medicines:
        return
    try:
        med_id = int(input("\nEnter Medicine ID to delete: "))
        for m in medicines:
            if m["id"] == med_id:
                medicines.remove(m)
                save_medicines()
                print(f"🗑️  '{m['name']}' removed successfully!")
                return
        print("❌ Medicine ID not found!")
    except ValueError:
        print("❌ Please enter a valid number!")

# ============================================================
# STEP 7: Check Today's Reminders
# ============================================================

def check_reminders():
    print("\n--- ⏰ Checking Reminders ---")
    current_time = get_current_time()
    print(f"Current Time : {current_time}")
    print(f"Current Date : {get_current_date()}\n")

    if not medicines:
        print("⚠️  No medicines added yet!")
        return

    due = [m for m in medicines if m["time"] == current_time and not m["taken"]]
    upcoming = [m for m in medicines if m["time"] > current_time and not m["taken"]]
    taken = [m for m in medicines if m["taken"]]

    if due:
        print("🚨 DUE NOW — Take these medicines immediately!")
        for m in due:
            print(f"   💊 {m['name']} — {m['dosage']} | Note: {m['note']}")

    if upcoming:
        print("\n⏳ UPCOMING Medicines:")
        for m in upcoming:
            print(f"   🕐 {m['time']} → {m['name']} — {m['dosage']}")

    if taken:
        print("\n✅ Already Taken Today:")
        for m in taken:
            print(f"   ✔️  {m['name']} — {m['dosage']}")

    if not due and not upcoming:
        print("🎉 All medicines taken for today! Well done!")

# ============================================================
# STEP 8: Reset Daily Status
# ============================================================

def reset_daily():
    for m in medicines:
        m["taken"] = False
    save_medicines()
    print("✅ Daily medicine status has been reset for a new day!")

# ============================================================
# STEP 9: Health Tips for Elderly
# ============================================================

def health_tips():
    tips = [
        "💧 Drink at least 8 glasses of water daily.",
        "🚶 Take a 15-minute walk every morning.",
        "🥗 Eat fresh fruits and vegetables every day.",
        "😴 Sleep at least 7-8 hours per night.",
        "💊 Never skip your prescribed medicines.",
        "🧠 Keep your mind active — read books or solve puzzles.",
        "👨‍⚕️ Visit your doctor for regular check-ups.",
        "🧘 Practice deep breathing or meditation to reduce stress.",
        "🦷 Brush your teeth twice daily for good oral health.",
        "☀️  Get some sunlight every day for Vitamin D.",
    ]
    print("\n--- 🌟 Daily Health Tips for Elderly ---")
    for i, tip in enumerate(tips, 1):
        print(f"  {i:>2}. {tip}")

# ============================================================
# STEP 10: Main Menu
# ============================================================

def main():
    load_medicines()
    display_banner()

    while True:
        print(f"\n📅 Date : {get_current_date()}  |  🕐 Time : {get_current_time()}")
        print("\n--- MAIN MENU ---")
        print("  1. ➕ Add Medicine Reminder")
        print("  2. 📋 View All Medicines")
        print("  3. ✅ Mark Medicine as Taken")
        print("  4. 🗑️  Delete Medicine")
        print("  5. ⏰ Check Today's Reminders")
        print("  6. 🔄 Reset Daily Status")
        print("  7. 🌟 Health Tips")
        print("  8. 🚪 Exit")

        choice = input("\nEnter your choice (1-8): ").strip()

        if   choice == "1": add_medicine()
        elif choice == "2": view_medicines()
        elif choice == "3": mark_taken()
        elif choice == "4": delete_medicine()
        elif choice == "5": check_reminders()
        elif choice == "6": reset_daily()
        elif choice == "7": health_tips()
        elif choice == "8":
            print("\n👋 Take care! Stay healthy! Goodbye! 💊\n")
            break
        else:
            print("❌ Invalid choice! Please enter 1 to 8.")

if __name__ == "__main__":
    main()
