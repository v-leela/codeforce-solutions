"""
tags: greedy
"""

t=int(input())
while t!=0:
    n=int(input())
    a=list(map(int,input().split()))
    max_val=max(a)
    print(max_val*n)
    t-=1
