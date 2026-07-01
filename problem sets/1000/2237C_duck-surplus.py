"""
tags: binary search, greedy
"""


def sort_first(a, idx):
    for i in range(idx, n - 1):
        if a[i] > a[i + 1]:
            oldright = a[i]
            a[i] = a[i + 1]
            a[i + 1] += oldright
            return 1, i

    return 0, idx


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    idx = 0
    notsorted = 1

    while notsorted == 1:
        notsorted, idx = sort_first(a, idx)

    print(a[-1])
