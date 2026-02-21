"""
tags: greedy, math
"""

t=int(input())
for _ in range(t):
    l,r,k=map(int,input().split())
    if r//k>=l:
        last_num=int(r//k)
        print(last_num-l+1)
    else:
        print(0)