"""
tags: constructive algorithms, games, greedy, math
"""

t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    if n!=2 and (a-b)%2==0:
        print("yes")
    else:
        print("no")
