"""t = int(input())
for _ in range(t):
    a, b, x = list(map(int, input().split()))
    count = 0
    while a != b:
        if b > a * x:
            b = b // x
        elif a > b * x:
            a = a // x
        elif a > b:
            if a - b > b - a // x:
                a = a // x
            elif a - b > 1 and a - b > a // x - b // x:
                a = a // x
                b = b // x
                count += 1
            else:
                b += 1
        elif b > a:
            if b - a > a - b // x:
                b = b // x
            elif b - a > 1 and b - a > b // x - a // x:
                a = a // x
                b = b // x
                count += 1
            else:
                a += 1
        count += 1
    # print(a, b, "count :", count)

    print(count)"""

import random
from collections import deque


def brute(A, B, X):
    LIMIT = 100  # >= maximum value you want to test

    q = deque([(A, B, 0)])
    vis = {(A, B)}

    while q:
        A, B, d = q.popleft()

        if A == B:
            return d

        nxt = [
            (A + 1, B),
            (A, B + 1),
            (A // X, B),
            (A, B // X),
        ]

        for na, nb in nxt:
            if 0 <= na <= LIMIT and 0 <= nb <= LIMIT and (na, nb) not in vis:
                vis.add((na, nb))
                q.append((na, nb, d + 1))


a = random.randint(1, 100)
b = random.randint(1, 100)
x = random.randint(2, 10)
# a, b, x = 100, 97, 6
print(a, b, x)


def ncount(a, b, x):
    cnt = 0
    while a != b:
        a = a // x
        b = b // x
        cnt += 1
    return cnt


print("bruteforce :", brute(a, b, x))


def greedy(a, b, x):
    count = 0
    i = 1
    while a != b:
        if b > a * x:
            b = b // x
        elif a > b * x:
            a = a // x
        elif a > b:
            """ if a - b <= b - a // x and a - b <= a // x - b // x:
                b += 1 """
            if a - b > b - a // x:
                a = a // x
            elif (a - b) - (a // x - b // x) > 2 and a - b > a // x - b // x:
                a = a // x
                b = b // x
                count += 1
                i += 1
            else:
                b += 1
        elif b > a:
            if b - a > a - b // x:
                b = b // x
            elif (b - a) - (b // x - a // x) > 2 and b - a > b // x - a // x:
                a = a // x
                b = b // x
                count += 1
                i += 1
            else:
                a += 1
        count += 1
        # print(a, b, "count :", count, ncount(a, b, x))
    return count


print("greedy :", greedy(a, b, x))

for a in range(1, 101):
    for b in range(1, 101):
        for x in range(2, 11):
            g = greedy(a, b, x)
            r = brute(a, b, x)
            if g != r:
                print(a, b, x, g, r)
                break

print("No mismatch!")
