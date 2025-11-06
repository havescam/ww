def is_sorted_recursive(arr):
    # База: пустой список или один элемент — уже отсортирован
    if len(arr) <= 1:
        return True
    # Если найдено нарушение порядка, сразу False
    if arr[0] > arr[1]:
        return False
    # Рекурсивно проверяем «хвост» списка
    return is_sorted_recursive(arr[1:])

# Примеры:
print(is_sorted_recursive([]))                 # True
print(is_sorted_recursive([1]))                # True
print(is_sorted_recursive([1, 2, 2, 5]))       # True
print(is_sorted_recursive([1, 3, 2]))          # False

Результат работы: 
True
True
True
False
