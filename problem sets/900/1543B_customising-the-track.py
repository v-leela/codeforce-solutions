"""
tags: combinatorics, greedy, math
"""

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print((n-sum(a)%n)*(sum(a)%n))