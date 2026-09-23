"""ЕГЭ информатика 1–27 — простые полные Python-шаблоны.
Шаблоны рассчитаны на учебное использование: меняй только части с "...".
"""

# ==================== 1. ГРАФЫ ====================
# Степень вершины — количество рёбер.
# Для небольшого графа можно перебрать готовые пути.
best = 10**9
for path in paths:
    length = sum(weight[e] for e in path)
    best = min(best, length)
print(best)

# ==================== 2. ТАБЛИЦЫ ИСТИННОСТИ ====================
from itertools import product
for x, y, w, z in product([0, 1], repeat=4):
    F = ...
    print(x, y, w, z, int(F))
# Импликация A -> B: (not A) or B

# ==================== 3. БАЗЫ ДАННЫХ ====================
answer = 0
for row in rows:
    if ...:
        answer += row[...]
print(answer)

# ==================== 4. ФАНО ====================
codes = ['00', '01', '10']
new = '11'
ok = all(not (new.startswith(c) or c.startswith(new)) for c in codes)
print(ok)

# ==================== 5. СИСТЕМЫ СЧИСЛЕНИЯ ====================
def to_base(n, base):
    s = ''
    while n:
        s = str(n % base) + s
        n //= base
    return s or '0'

# Вариант: троичная
for N in range(1, 1000):
    s = to_base(N, 3)
    if N % 3 == 0:
        s += s[-2:]
    else:
        s += to_base((s.count('1') + s.count('2')) * 3, 3)
    R = int(s, 3)
    if 900 < R < 1000:
        print(R)

# Вариант: двоичная + чётность единиц
for N in range(1, 1000):
    s = to_base(N, 2)
    s = ('10' if s.count('1') % 2 == 0 else '11') + s
    R = int(s, 2)
    if R > 50:
        print(R)
        break

# Вариант: четырёхричная
for N in range(1, 1000):
    s = to_base(N, 4)
    if N % 4 == 0:
        s += s[-1]
    else:
        s += to_base((N % 4) * 2, 4)
    R = int(s, 4)
    if R < 200:
        print(R)

# ==================== 6. ЧЕРЕПАХА ====================
from turtle import *
m = 20
left(90)
down()
for i in range(7):
    forward(10*m)
    right(120)
up()

# Точки на плоскости:
for x in range(-10, 11):
    for y in range(-10, 11):
        setpos(x*m, y*m)
        dot(3)

# ==================== 7. ИНФОРМАЦИЯ ====================
# Звук: I = k * i * f * t
channels = 2
depth = 16
frequency = 44100
seconds = 10
I = channels * depth * frequency * seconds
MB = I / 8 / 1024 / 1024
print(MB)

# Графика:
from math import log2
colors = 256
i = int(log2(colors))
I = width * height * i

# Передача:
I = speed * seconds

# ==================== 8. КОМБИНАТОРИКА ====================
# Ровно K символов:
count = 0
for x1 in '1234':
    for x2 in '1234':
        for x3 in '1234':
            for x4 in '1234':
                for x5 in '1234':
                    s = x1+x2+x3+x4+x5
                    if s.count('1') == 2:
                        count += 1
print(count)

# Product:
count = 0
for p in product('АКЦЕНТ', repeat=5):
    word = ''.join(p)
    if word.count('Т') >= 1 and not word.startswith(('А','Е','К')):
        count += 1
print(count)

# Без повторений:
from itertools import permutations
for p in permutations('ABCDE', 4):
    word = ''.join(p)
    if ...:
        print(word)

# Номер слова:
count = 0
for a in 'АОУ':
    for b in 'АОУ':
        for c in 'АОУ':
            for d in 'АОУ':
                for e in 'АОУ':
                    count += 1
                    if count == 210:
                        print(a+b+c+d+e)

# ==================== 9. ТАБЛИЦЫ ====================
# В задачах на Excel внимательно проверяй A1, $A$1, $A1, A$1.

# ==================== 10. IP ====================
import ipaddress
net = ipaddress.ip_network('192.168.159.86/255.255.252.0', 0)
print(net.network_address)
ip = net.network_address
print(sum(map(int, str(ip).split('.'))))

# ==================== 11. ИНФОРМАЦИОННЫЙ ОБЪЁМ ====================
from math import log2
N = 256
K = 20
I = K * log2(N)
variants = N ** K
print(I, variants)

# ==================== 12. РЕДАКТОР ====================
s = '>' + '0'*10 + '1'*20 + '2'*15
while '>1' in s or '>2' in s or '>0' in s:
    s = s.replace('>1', '22>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>0', '1>', 1)
print(s)

# Перебор N:
for n in range(1, 100):
    s = '0' + '1'*n + '2'*n
    while '01' in s or '02' in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3', 1)
    if sum(map(int, s)) == 75:
        print(n)

# ==================== 13. ЦЕПОЧКИ ====================
def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x+1, end) + f(x+2, end)

# Через обязательную точку M:
# answer = f(start, M) * f(M, finish)

# Запрещённая точка:
def f_bad(x, end, bad):
    if x > end or x == bad:
        return 0
    if x == end:
        return 1
    return f_bad(x+1,end,bad) + f_bad(x+2,end,bad)

# ==================== 14. НЕИЗВЕСТНАЯ ЦИФРА ====================
for x in range(2, 8):
    n = int(f'1{x}25', 8)
    if n % 7 == 0:
        print(x, n)

# Несколько чисел:
for x in range(2, 8):
    A = int(f'12{x}3', 8)
    B = int(f'4{x}5', 8)
    if (A+B) % 9 == 0:
        print(x)

# ==================== 15. ЛОГИКА ====================
for A in range(1000):
    ok = True
    for x in range(1000):
        F = ...
        if not F:
            ok = False
            break
    if ok:
        print(A)
        break

# Поразрядная конъюнкция:
# (x & 29) != 0
# (x & 17) == 0
# (x & A) != 0

# ==================== 16. РЕКУРСИЯ ====================
# Метод 1: увеличить лимит
import sys
sys.setrecursionlimit(1000000)

# Метод 2: кэш
from functools import lru_cache
@lru_cache(None)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# Метод 3: цикл вместо рекурсии
ans = 1
for i in range(1, n+1):
    ans *= i
print(ans)

# ==================== 17. ПОСЛЕДОВАТЕЛЬНОСТИ ====================
with open('17.txt') as f:
    a = [int(x) for x in f]

# Пары:
ans = []
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if ...:
        ans.append(x+y)
print(len(ans), max(ans))

# Тройки:
for i in range(len(a)-2):
    x, y, z = a[i:i+3]
    if ...:
        ...

# Четвёрки:
for i in range(len(a)-3):
    x1,x2,x3,x4 = a[i:i+4]
    if ...:
        ...

# ==================== 18. РОБОТ ====================
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i:
            dp[i][j] += dp[i-1][j]
        if j:
            dp[i][j] += dp[i][j-1]
print(dp[-1][-1])

# Запрещённая клетка:
# if blocked[i][j]: dp[i][j] = 0

# ==================== 19–21. ИГРЫ ====================
def win(s):
    if s >= target:
        return True
    return any(not win(s+m) for m in moves)

# Две кучи:
def win2(a,b):
    if a+b >= target:
        return True
    states = [(a+1,b),(a,b+1),(a*2,b),(a,b*2)]
    return any(not win2(x,y) for x,y in states)

# ==================== 22. ПРОЦЕССЫ ====================
# start = max(end predecessors)
# end = start + duration

# ==================== 23. ГРАФЫ ====================
from collections import deque
def bfs(graph, start):
    dist = [-1]*len(graph)
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for u in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)
    return dist

# Количество путей в DAG:
dp = [0]*n
dp[start] = 1
for v in order:
    for u in graph[v]:
        dp[u] += dp[v]
print(dp[target])

# Длиннейший путь в DAG:
dp = [-10**18]*n
dp[start] = 0
for v in order:
    for u,w in graph[v]:
        dp[u] = max(dp[u], dp[v]+w)

# ==================== 24. СТРОКИ ====================
best = cur = 0
for ch in s:
    if ch == 'A':
        cur += 1
        best = max(best, cur)
    else:
        cur = 0
print(best)

# ==================== 25. МАСКИ ====================
from fnmatch import fnmatch
for x in range(0, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x//1917)

# Делители:
def divisors(n):
    d = 1
    while d*d <= n:
        if n % d == 0:
            yield d
            if d*d != n:
                yield n//d
        d += 1

# ==================== 26. ФАЙЛЫ ====================
with open('26.txt') as f:
    a = [int(x) for x in f]
a.sort()
total = 0
count = 0
for x in a:
    if total + x <= limit:
        total += x
        count += 1
print(count, total)

# ==================== 27. БОЛЬШИЕ ДАННЫЕ ====================
best = -10**18
for x in data:
    best = max(best, x)
print(best)

# Два ответа в одной строке:
print(answer1, answer2)