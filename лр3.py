# -*- coding: utf-8 -*-
# Все примеры собраны в одном файле

import heapq

print("=== 1) heapq (min-heap) ===")
some_numbers = [8, 3, 5, 1, 6, 2, 4, 7]
heapq.heapify(some_numbers)                  # O(n)
print("heapified:", some_numbers)
heapq.heappush(some_numbers, 0)              # O(log n)
print("after push 0:", some_numbers)
min_val = heapq.heappop(some_numbers)        # O(log n)
print("heappop ->", min_val)
print("after pop:", some_numbers)
print()

# ------------------------------------------------------------
# 2) Собственный класс бинарной кучи (min-heap)
# ------------------------------------------------------------

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return not self.heap

    def push(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def peek(self):
        return None if self.is_empty() else self.heap[0]

    def pop(self):
        if self.is_empty():
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root

    def _sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i] < self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

print("=== 2) BinaryHeap (custom min-heap) ===")
bh = BinaryHeap()
for x in [5, 3, 7, 1, 4]:
    bh.push(x)
print("peek:", bh.peek())
while not bh.is_empty():
    print("pop ->", bh.pop())
print()

# ------------------------------------------------------------
# 3) Фибоначчи: печать первых n и рекурсивный n-й
# ------------------------------------------------------------

def fibonacci_for_loop(n):
    a, b = 0, 1
    res = []
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("=== 3) Fibonacci ===")
print("first 10:", fibonacci_for_loop(10))
print("F(10):", fibonacci(10))
print()

# ------------------------------------------------------------
# 4) Хеш‑таблица: вариант с цепочками (separate chaining)
# ------------------------------------------------------------

class HashTableEntry:
    __slots__ = ("key", "value")
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"({self.key!r}, {self.value!r})"

class HashTableChaining:
    def __init__(self, capacity=8):
        self.capacity = max(4, capacity)
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _index(self, key):
        # Демонстрационная хеш-функция; в реальном коде лучше использовать встроенный hash(key)
        return (hash(key) & 0x7fffffff) % self.capacity

    def _load_factor(self):
        return self.size / self.capacity

    def _rehash(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for e in bucket:
                self.set(e.key, e.value)

    def set(self, key, value):
        i = self._index(key)
        bucket = self.buckets[i]
        for e in bucket:
            if e.key == key:
                e.value = value
                return
        bucket.append(HashTableEntry(key, value))
        self.size += 1
        if self._load_factor() > 0.75:
            self._rehash(self.capacity * 2)

    def get(self, key):
        i = self._index(key)
        bucket = self.buckets[i]
        for e in bucket:
            if e.key == key:
                return e.value
        raise KeyError(key)

    def remove(self, key):
        i = self._index(key)
        bucket = self.buckets[i]
        for idx, e in enumerate(bucket):
            if e.key == key:
                bucket.pop(idx)
                self.size -= 1
                return
        raise KeyError(key)

    def __repr__(self):
        return "{" + ", ".join(
            f"{e.key!r}:{e.value!r}"
            for bucket in self.buckets for e in bucket
        ) + "}"

print("=== 4) HashTable (separate chaining) ===")
ht = HashTableChaining(capacity=4)
ht.set("A", 10)
ht.set("B", 20)
ht.set("C", 30)
print("table:", ht)
print("get('B'):", ht.get("B"))
ht.remove("B")
print("after remove B:", ht)
print()

# ------------------------------------------------------------
# 5) Хеш‑таблица: открытая адресация (линейное пробирование)
# ------------------------------------------------------------

class OAEntry:
    __slots__ = ("key", "value", "deleted")
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.deleted = False

class HashTableOpenAddressing:
    def __init__(self, capacity=8):
        self.capacity = max(4, capacity)
        self.size = 0
        self.array = [None] * self.capacity

    def _index(self, key):
        return (hash(key) & 0x7fffffff) % self.capacity

    def _probe(self, start):
        i = start
        while True:
            yield i
            i = (i + 1) % self.capacity

    def _load_factor(self):
        return self.size / self.capacity

    def _rehash(self, new_capacity):
        old_array = self.array
        self.capacity = new_capacity
        self.array = [None] * self.capacity
        self.size = 0
        for slot in old_array:
            if slot is not None and not slot.deleted:
                self.set(slot.key, slot.value)

    def set(self, key, value):
        if self._load_factor() > 0.6:
            self._rehash(self.capacity * 2)
        idx0 = self._index(key)
        first_deleted = None
        for idx in self._probe(idx0):
            slot = self.array[idx]
            if slot is None:
                target = first_deleted if first_deleted is not None else idx
                self.array[target] = OAEntry(key, value)
                self.size += 1
                return
            if slot.deleted:
                if first_deleted is None:
                    first_deleted = idx
                continue
            if slot.key == key:
                slot.value = value
                return

    def get(self, key):
        idx0 = self._index(key)
        for idx in self._probe(idx0):
            slot = self.array[idx]
            if slot is None:
                break
            if not slot.deleted and slot.key == key:
                return slot.value
        raise KeyError(key)

    def remove(self, key):
        idx0 = self._index(key)
        for idx in self._probe(idx0):
            slot = self.array[idx]
            if slot is None:
                break
            if not slot.deleted and slot.key == key:
                slot.deleted = True
                self.size -= 1
                return
        raise KeyError(key)

    def __repr__(self):
        pairs = []
        for slot in self.array:
            if slot is not None and not slot.deleted:
                pairs.append(f"{slot.key!r}:{slot.value!r}")
        return "{" + ", ".join(pairs) + "}"

print("=== 5) HashTable (open addressing, linear probing) ===")
oa = HashTableOpenAddressing(capacity=5)
oa.set("A", 1)
oa.set("F", 2)  # возможная коллизия с "A"
oa.set("K", 3)  # ещё коллизии
print("table:", oa)
print("get('K'):", oa.get("K"))
oa.remove("F")
print("after remove F:", oa)
