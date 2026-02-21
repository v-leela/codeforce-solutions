"""
tags: greedy, math
"""

def multiples(int,k):
    multi=[]
    for i in range(k):
        multi.append((i+1)*int)
    return multi

t=int(input())
for _ in range(t):
    l,r,k=map(int,input().split())
    s=list(range(l,r+1))
    """ print(s) """
    count=0
    for j in s:
        if set(multiples(j,k))<=set(s):
            count+=1
    print(count)    
    