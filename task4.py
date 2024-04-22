from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)
        
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        
        days_until_birthday = (birthday - today).days
        
        if 0 <= days_until_birthday <= 7:
            if birthday.weekday() >= 5:  # Якщо день народження припадає на вихідний
                # Переносимо дату привітання на наступний понеділок
                days_until_birthday += (7 - birthday.weekday())
            congratulation_date = today + timedelta(days=days_until_birthday)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    
    return upcoming_birthdays

# Приклад використання функції
users = [
    {"name": "John Doe", "birthday": "1985.04.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
