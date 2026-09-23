"""ЕГЭ информатика — Python-шаблоны 1–27."""

# 1 — графы
# Степень вершины: len(graph[v])

# 2 — таблица истинности
from itertools import product
def task_2():
    for a, b, c in product([0, 1], repeat=3):
        F = ...
        print(a, b, c, F)

# 3 — базы данных
def task_3(rows):
    total = 0
    for row in rows:
        if ...:
            total += row[...]
    return total

# 4 — Фано
# Проверяй отсутствие ситуации code_a.startswith(code_b).

# 5 — системы счисления
def task_5():
    n = int('101101', 2)
    print(bin(n), oct(n), hex(n))

# 6 — Черепаха
def task_6():
    from turtle import *
    for _ in range(...):
        forward(...)
        right(...)

# 7 — объём информации
# I = k * i * f * t
# I = X * Y * i
# I = v * t

# 8 — комбинаторика
def task_8(alphabet, length):
    count = 0
    for word in product(alphabet, repeat=length):
        s = ''.join(word)
        if ...:
            count += 1
    return count

# 9 — электронные таблицы
# Учитывай абсолютные и относительные ссылки.

# 10 — IP
def task_10():
    import ipaddress
    net = ipaddress.ip_network('192.168.1.0/24')
    ip = ipaddress.ip_address('192.168.1.10')
    return ip in net

# 11 — информация/пароли
# i = log2(N), I = K * log2(N), варианты = N ** K

# 12 — редактор
def task_12(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
    return s

# 13 — вычислительные цепочки
from functools import lru_cache
@lru_cache(None)
def task_13(x):
    if x == ...:
        return 1
    if x > ...:
        return 0
    return task_13(x + 1) + task_13(x * 2)

# 14 — неизвестная цифра
def task_14(base):
    for x in range(base):
        # собрать число с x и проверить условие
        pass

# 15 — логика/отрезки
def task_15(a, b):
    return bool(a & b)

# 16 — оптимизация рекурсии
import sys
sys.setrecursionlimit(1_000_000)

# 17 — последовательности
def task_17(a):
    count = 0
    for i in range(len(a) - 1):
        if ...:
            count += 1
    return count

# 18 — робот/таблица
def task_18(n, m):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i: dp[i][j] += dp[i-1][j]
            if j: dp[i][j] += dp[i][j-1]
    return dp[-1][-1]

# 19–21 — теория игр
def game(x, target, moves):
    if x >= target:
        return True
    return any(not game(x + m, target, moves) for m in moves)

# 22 — многопроцессорные системы
# Учитывай зависимости и время окончания процессов.

# 23 — графы / BFS
from collections import deque
def bfs(graph, start):
    dist = [-1] * len(graph)
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for u in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)
    return dist

# 24 — максимальная серия
def max_series(s):
    best = cur = 0
    for ch in s:
        if ...:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best

# 25 — маски
def task_25():
    from fnmatch import fnmatch
    for n in range(1, 10**7):
        if fnmatch(str(n), '12*34'):
            print(n)

# 26 — файлы
def task_26(filename):
    with open(filename) as f:
        data = list(map(int, f))
    data.sort()
    ans = 0
    for x in data:
        if ...:
            ans += x
    return ans

# 27 — большие данные
def task_27(data):
    best = ...
    for x in data:
        # O(N)
        ...
    return best