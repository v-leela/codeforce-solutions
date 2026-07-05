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

a = random.randint(1, 100)
b = random.randint(1, 100)
x = random.randint(2, 10)
# a, b, x =
print(a, b, x)

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
    print(a, b, "count :", count)

print(a, b, count)
