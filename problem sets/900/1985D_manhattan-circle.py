"""
tags: implementation, math
"""

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    count_hash=-1
    a=1
    for i in range(n):
        row=input()
        if i==n-1 and count_hash<row.count("#"):
            print(n,row.index("#")+1)
            break
        if "#" in row and count_hash<row.count("#"):
            ind=row.index("#")
        if count_hash>row.count("#") and a:
            print(i,ind+(count_hash//2)+1)
            a=0
        if count_hash<row.count("#"):
            count_hash=row.count("#")
        else:
            continue