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
        else:
            b += 1
    elif b > a:
        if b - a > a - b // x:
            b = b // x
        else:
            a += 1
    count += 1
print(count)
