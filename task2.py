import random

def get_numbers_ticket(minimum: int, maximum: int, quantity: int) -> int:
    # Перевірка валідності вхідних даних
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        return []

    # Генерування набору унікальних чисел
    numbers = random.sample(range(minimum, maximum + 1), quantity)
    
    # Сортування та повернення списку чисел
    return sorted(numbers)

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
