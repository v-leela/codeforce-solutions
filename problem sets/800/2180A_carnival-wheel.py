"""
tags: number theory, brute force
"""

t=int(input())
for i in range(t):
    l,a,b=map(int,input().split())
    prize_list=[]
    for j in range(l):
        prize_list.append((a+(j*b))%l)
    print(max(prize_list))
