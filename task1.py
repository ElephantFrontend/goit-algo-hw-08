# Імпортуємо лібу для роботи з купами.
import heapq

# Створюємо функцію яка буде обробляти мінімальну вартість зʼднання та повертати інфу.
def min_connection_cost(cables):
    # Ініціалізуємо мін-купу з довжинами кабелів.
    heapq.heapify(cables)
    total_cost = 0

    # Поки є більше ніж один кабель у купі.
    while len(cables) > 1:
        # Дістаємо два найкоротші кабелі.
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість об'єднання.
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад до купи.
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання.y
cables = [4, 3, 2, 6]
print("Мінімальна вартість з'єднання:", min_connection_cost(cables))
