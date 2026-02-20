"""
tags: implementation, greedy
"""

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    gold=0
    people=0
    for j in range(n):
        if a[j]>=k:
            gold+=a[j]
        if a[j]==0 and gold:
            gold-=1
            people+=1
        else:
            continue          
    print(people)
