# -*- coding: utf-8 -*-
# Все примеры в одном файле

# --- Мультисписок (вложенный список) ---
# Разные длины вложенных списков удобно хранить как «рваный» список списков.
# Многомерные структуры и «рваные» списки — стандартная техника представления таблиц/матриц. 
multilist = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9],
]

print("=== Nested list ===")
for i, row in enumerate(multilist):
    row_sum = sum(row)
    print(f"row {i}: {row} | sum={row_sum}")
print()

# --- Очередь (queue.Queue) ---
# Потокобезопасная FIFO-очередь с методами put/get и qsize/empty.
from queue import Queue

q = Queue()
for v in (1, 2, 3):
    q.put(v)

print("=== queue.Queue (FIFO, thread-safe) ===")
print("size:", q.qsize())
print("empty:", q.empty())
while not q.empty():
    print("get:", q.get())
print("empty after drain:", q.empty())
print()

# --- Дек (двусторонняя очередь) ---
# deque обеспечивает O(1) добавление/удаление с обоих концов: append/appendleft, pop/popleft.
from collections import deque

tasks = deque()
tasks.append("task1")       # вправо
tasks.append("task2")
tasks.appendleft("urgent")  # влево (приоритет)

print("=== collections.deque ===")
print("initial:", list(tasks))
p = tasks.popleft()
print("popleft:", p)
print("after popleft:", list(tasks))
tasks.appendleft("now")
print("after appendleft:", list(tasks))
print()

# --- Приоритетная очередь через PriorityQueue ---
# PriorityQueue извлекает элементы в порядке возрастания ключа (минимальный приоритет первым).
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((2, "mid"))
pq.put((1, "high"))
pq.put((3, "low"))

print("=== queue.PriorityQueue (min-priority first) ===")
while not pq.empty():
    print(pq.get())
print()

# --- Приоритетная очередь через heapq (мин-куча) ---
# heapq работает со списком как с мин-кучей: heappush/heappop.
import heapq

customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))

print("=== heapq (min-heap) ===")
while customers:
    priority, name = heapq.heappop(customers)
    print(priority, name)

