"""
tags: brute force, sortings
"""

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    if max(a)<x or min(a)>x:
        print("no")
    else:
        print("yes")
