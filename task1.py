from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        target_date = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримання поточної дати
        current_date = datetime.today()
        
        # Розрахунок різниці між поточною датою та заданою датою у днях
        difference = current_date - target_date
        
        # Повернення різниці у днях як ціле число
        return difference.days
    except ValueError:
        # Обробка неправильного формату вхідних даних
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."
    
print(f"Кількість днів між заданою датою і поточною датою: {get_days_from_today('2021.10.09')}")
print(f"Кількість днів між заданою датою і поточною датою: {get_days_from_today('2020-10-09 16:01:55')}")
