# data/reminders.py

reminders = []

def add_reminder(medicine, hours, telegram_id):
    reminder = {
        "medicine": medicine,
        "hours": hours,
        "telegram_id": telegram_id
    }
    reminders.append(reminder)
    return reminder

def get_reminders():
    return reminders
