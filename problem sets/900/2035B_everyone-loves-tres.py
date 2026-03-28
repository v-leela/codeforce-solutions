"""
tags: constructive algorithms, greedy, math, number theory
"""

t=int(input())
for _ in range(t):
    n=int(input())

    if n==1 or n==3:
        print(-1)
    else:
        if n%2:
            a=[3]*(n-4)+[6,3]+[6,6]
            print("".join(list(map(str,a))))
        else:
            a=[3]*(n-2)+[6,6]
            print("".join(list(map(str,a))))