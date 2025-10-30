from typing import List, Callable, Iterable

def insertion_sort(arr: List[float]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(
    data: Iterable[float],
    buckets_count: int | None = None,
    inner_sort: Callable[[List[float]], None] = insertion_sort
) -> List[float]:
    arr = list(data)
    n = len(arr)
    if n <= 1:
        return arr[:]
    k = buckets_count if (isinstance(buckets_count, int) and buckets_count > 0) else n
    lo = min(arr)
    hi = max(arr)
    if lo == hi:
        return arr[:]
    buckets: List[List[float]] = [[] for _ in range(k)]
    scale = hi - lo
    for x in arr:
        t = (x - lo) / scale
        bi = int(t * k)
        if bi == k:
            bi = k - 1
        buckets[bi].append(x)
    for b in buckets:
        inner_sort(b)
    result: List[float] = []
    for b in buckets:
        result.extend(b)
    return result

if __name__ == "__main__":
    data1 = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    data2 = [42, 32, 33, 52, 37, 47, 51, 42, 33, 100, -5, 0]
    data3 = [3.14, 2.71, 1.41, 1.73, 0.0, -1.0, 10.0, 9.99]

    sorted1 = bucket_sort(data1)
    sorted2 = bucket_sort(data2)
    sorted3 = bucket_sort(data3, buckets_count=16)

    print(sorted1)
    print(sorted2)
    print(sorted3)

Результат работы: 
Пример 1: исходный = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68] -> отсортированный = [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
Пример 2: исходный = [29, 25, 3, 49, 9, 37, 21, 43] -> отсортированный = [3, 9, 21, 25, 29, 37, 43, 49]
Пример 3: исходный = [5.0, -2.3, 7.1, 0.0, -2.3, 3.14, 2.71, 2.72] -> отсортированный = [-2.3, -2.3, 0.0, 2.71, 2.72, 3.14, 5.0, 7.1]
Пример 4: исходный = [1] -> отсортированный = [1]
Пример 5: исходный = [7, 7, 7, 7] -> отсортированный = [7, 7, 7, 7]

Шаги по строкам кода
n = len(a); if n <= 1: return a[:] — база: пустой/один элемент уже отсортирован.​

mn, mx = min(a), max(a); if mn == mx: return a[:] — все элементы равны, сортировать не нужно.​

buckets_count = max(2, int(math.sqrt(n))) — выбирается число корзин k для распределения диапазона значений.​

buckets = [[] for _ in range(buckets_count)] — создаются пустые корзины.​

idx = int((x - mn) / (mx - mn) * (buckets_count - 1)); buckets[idx].append(x) — вычисляется индекс корзины и элемент добавляется в неё (равномерная разбивка диапазона).​

для каждой корзины: insertion_sort(b); result.extend(b) — локальная сортировка корзин и конкатенация в итоговый массив

from typing import List, Tuple

def flip_prefix(a: List[int], k: int) -> None:
    """
    Переворачивает префикс массива a[0:k] (k элементов).
    Пример: a=[3,2,4,1], k=3 -> a станет [4,2,3,1].
    """
    a[:k] = reversed(a[:k])

def find_max_index(a: List[int], n: int) -> int:
    """
    Возвращает индекс максимального элемента в a[0:n].
    """
    max_i = 0
    for i in range(1, n):
        if a[i] > a[max_i]:
            max_i = i
    return max_i

def pancake_sort(a: List[int]) -> Tuple[List[int], List[int]]:
    """
    Блинная сортировка. Разрешённая операция — flip префикса длины k.
    Возвращает:
      - отсортированный массив (in-place) в виде копии,
      - список длин префиксов (k), которые переворачивались по порядку.
    Идея: для хвоста длины curr_n находим максимум, поднимаем его в начало (flip),
    затем переносим в конец хвоста (ещё один flip), уменьшаем хвост и повторяем.
    """
    arr = a[:]  # не портим исходные данные
    flips: List[int] = []
    n = len(arr)
    # последовательно "фиксируем" максимум в позиции curr_n-1
    for curr_n in range(n, 1, -1):
        max_i = find_max_index(arr, curr_n)
        # если максимум уже на месте, пропускаем
        if max_i == curr_n - 1:
            continue
        # если максимум не в нуле — поднимем его в начало
        if max_i != 0:
            flip_prefix(arr, max_i + 1)
            flips.append(max_i + 1)
        # перенесём максимум из начала в позицию curr_n-1
        flip_prefix(arr, curr_n)
        flips.append(curr_n)
    return arr, flips

if __name__ == "__main__":
    data = [3, 6, 1, 10, 2, 7]
    print("Исходный массив:", data)
    sorted_data, flip_seq = pancake_sort(data)
    print("Отсортированный:", sorted_data)
    print("Последовательность переворотов (k):", flip_seq)
    # Мини-демонстрация пошагово
    demo = data[:]
    print("\nПошаговая демонстрация переворотов:")
    for k in flip_seq:
        flip_prefix(demo, k)
        print(f"flip({k}) ->", demo)
Результат работы:
Исходный массив: [3, 6, 1, 10, 2, 7]
Отсортированный: [1, 2, 3, 6, 7, 10]
Последовательность переворотов (k): [4, 6, 5, 2, 4, 2, 3]

Пошаговая демонстрация переворотов:
flip(4) -> [10, 1, 6, 3, 2, 7]
flip(6) -> [7, 2, 3, 6, 1, 10]
flip(5) -> [1, 6, 3, 2, 7, 10]
flip(2) -> [6, 1, 3, 2, 7, 10]
flip(4) -> [2, 3, 1, 6, 7, 10]
flip(2) -> [3, 2, 1, 6, 7, 10]
flip(3) -> [1, 2, 3, 6, 7, 10]

from typing import List, Tuple

def bead_sort(arr: List[int]) -> List[int]:
    # Проверки
    if not arr:
        return []
    if any(x < 0 for x in arr):
        raise ValueError("Bead sort работает только с неотрицательными целыми")

    n = len(arr)
    max_val = max(arr)
    if max_val == 0:
        return arr[:]  # все нули уже "отсортированы"

    # Матрица бусин: rows = n, cols = max_val; 1 означает бусина
    beads = [[0] * max_val for _ in range(n)]
    for i, val in enumerate(arr):
        for j in range(val):
            beads[i][j] = 1

    # Гравитация по каждому столбцу: считаем бусины в столбце и "роняем" вниз
    for j in range(max_val):
        count = sum(beads[i][j] for i in range(n))
        # заполняем снизу вверх count единицами
        for i in range(n - 1, -1, -1):
            beads[i][j] = 1 if count > 0 else 0
            count -= 1

    # Считываем отсортированные значения как сумму по строке
    result = [sum(row) for row in beads]
    return result

if __name__ == "__main__":
    data = [5, 3, 0, 2, 4, 1, 1]
    print("Исходный массив:", data)
    try:
        sorted_data = bead_sort(data)
        print("Отсортированный:", sorted_data)
    except ValueError as e:
        print("Ошибка:", e)

    # Мини‑демо «шагов»: повторим гравитацию и выведем промежуточные состояния
    def gravity_demo(a: List[int]) -> None:
        if not a:
            print("Пусто"); return
        if any(x < 0 for x in a):
            print("Только неотрицательные целые"); return
        n = len(a)
        m = max(a)
        beads = [[0]*m for _ in range(n)]
        for i, val in enumerate(a):
            for j in range(val):
                beads[i][j] = 1
        print("\nМатрица до гравитации (1=бусина):")
        for row in beads:
            print(row)
        for j in range(m):
            count = sum(beads[i][j] for i in range(n))
            for i in range(n - 1, -1, -1):
                beads[i][j] = 1 if count > 0 else 0
                count -= 1
            print(f"\nПосле обработки столбца {j}:")
            for row in beads:
                print(row)
        print("\nСчитывание результата по строкам:")
        print([sum(row) for row in beads])

    gravity_demo(data)

Результат работы:
Исходный массив: [5, 3, 0, 2, 4, 1, 1]
Отсортированный: [0, 1, 1, 2, 3, 4, 5]

Матрица до гравитации (1=бусина):
[1, 1, 1, 1, 1]
[1, 1, 1, 0, 0]
[0, 0, 0, 0, 0]
[1, 1, 0, 0, 0]
[1, 1, 1, 1, 0]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]

После обработки столбца 0:
[0, 1, 1, 1, 1]
[1, 1, 1, 0, 0]
[1, 0, 0, 0, 0]
[1, 1, 0, 0, 0]
[1, 1, 1, 1, 0]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]

После обработки столбца 1:
[0, 0, 1, 1, 1]
[1, 0, 1, 0, 0]
[1, 0, 0, 0, 0]
[1, 1, 0, 0, 0]
[1, 1, 1, 1, 0]
[1, 1, 0, 0, 0]
[1, 1, 0, 0, 0]

После обработки столбца 2:
[0, 0, 0, 1, 1]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 1, 0, 0, 0]
[1, 1, 1, 1, 0]
[1, 1, 1, 0, 0]
[1, 1, 1, 0, 0]

После обработки столбца 3:
[0, 0, 0, 0, 1]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 1, 0, 0, 0]
[1, 1, 1, 0, 0]
[1, 1, 1, 1, 0]
[1, 1, 1, 1, 0]

После обработки столбца 4:
[0, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 1, 0, 0, 0]
[1, 1, 1, 0, 0]
[1, 1, 1, 1, 0]
[1, 1, 1, 1, 1]

Считывание результата по строкам:
[0, 1, 1, 2, 3, 4, 5]

from typing import List, Tuple

def binary_search(arr: List[int], left: int, right: int, target: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr: List[int], target: int) -> Tuple[int, Tuple[int, int]]:
    if not arr:
        return -1, (0, -1)
    if arr[0] == target:
        return 0, (0, 0)

    i = 1
    n = len(arr)
    # Расширяем диапазон степенями двойки: 1,2,4,8,...
    while i < n and arr[i] <= target:
        i *= 2

    left = i // 2
    right = min(i, n - 1)
    # Выполняем двоичный поиск в найденном диапазоне
    idx = binary_search(arr, left, right, target)
    return idx, (left, right)

if __name__ == "__main__":
    data = [1, 2, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 40, 60, 90]
    x = 15
    print("Массив:", data)
    print("Искомое:", x)
    idx, rng = exponential_search(data, x)
    print("Найденный диапазон для бинарного поиска:", rng)
    print("Результат: индекс =", idx)
    # Для демонстрации отсутствия элемента
    y = 13
    idx2, rng2 = exponential_search(data, y)
    print("\nПроверка отсутствующего элемента:", y)
    print("Найденный диапазон:", rng2)
    print("Результат: индекс =", idx2)
Результат работы:
Массив: [1, 2, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 40, 60, 90]
Искомое: 15
Найденный диапазон для бинарного поиска: (4, 8)
Результат: индекс = 7

Проверка отсутствующего элемента: 13
Найденный диапазон: (4, 8)
Результат: индекс = -1

from typing import List, Tuple

def binary_search(arr: List[int], left: int, right: int, target: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr: List[int], target: int) -> Tuple[int, Tuple[int, int]]:
    if not arr:
        return -1, (0, -1)
    if arr[0] == target:
        return 0, (0, 0)

    i = 1
    n = len(arr)
    # Увеличиваем границу экспоненциально: 1, 2, 4, 8, ...
    while i < n and arr[i] < target:
        i *= 2

    left = i // 2
    right = min(i, n - 1)
    idx = binary_search(arr, left, right, target)
    return idx, (left, right)

if __name__ == "__main__":
    data = [1, 2, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 40, 60, 90]
    print("Массив:", data)

    x = 15
    idx, rng = exponential_search(data, x)
    print("\nИскомое:", x)
    print("Диапазон для бинарного поиска:", rng)
    print("Результат: индекс =", idx)

    y = 13
    idx2, rng2 = exponential_search(data, y)
    print("\nИскомое:", y)
    print("Диапазон для бинарного поиска:", rng2)
    print("Результат: индекс =", idx2)

Результат работы:

Массив: [1, 2, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 40, 60, 90]

Искомое: 15
Диапазон для бинарного поиска: (4, 8)
Результат: индекс = 7

Искомое: 13
Диапазон для бинарного поиска: (4, 8)
Результат: индекс = -1
