"""
tags: brute force, implementation, math, number theory
"""

import math
from functools import reduce

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=2
    while i<10**8:
        gcd=reduce(math.gcd,a+[nth_prime(i)])
        if gcd==1:
            print(nth_prime(i))
            break
        i+=1
    if i==10**8:
        print(-1)
