#status: not accepted (time limit exceeded)
"""
tags:data structures, implementation, math, two pointers
"""

t=int(input())
for _ in range(t):
    n,m,h=map(int,input().split())
    a=list(map(int,input().split()))
    rep=a.copy()
    for k in range(m):
        b,c=map(int,input().split())
        if a[b-1]+c>h:
            a=rep
        else:
            a[b-1]+=c
    print(" ".join(list(map(str,a))))