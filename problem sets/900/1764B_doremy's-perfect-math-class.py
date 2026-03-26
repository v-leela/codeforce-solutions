"""
tags: math, number theory
"""

import math

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    div=a[0]
    for e in a:
        div=math.gcd(div,e)
        if div==1:
            break
    print(max(a)//div)