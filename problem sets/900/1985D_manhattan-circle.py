"""
tags: implementation, math
"""

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        row=list(input())
        grid.append(row)
    grid.append(list("." for i in range(m)))
    list_hash=[0]
    count=0
    i=0
    while i<n+1:
        count=grid[i].count("#")
        if count<max(list_hash):
            ind=grid[i-1].index("#")
            j=ind+max(list_hash)//2+1
            print(i,j)
            break
        else:
            i+=1
            list_hash.append(count)
    