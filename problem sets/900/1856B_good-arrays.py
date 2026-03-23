"""
tags: implementation, math
"""

import numpy as np

t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    a=np.array(a)
    if n==1:
        print("no")
    else:
        if n%2==0:
            b=np.array([1]*(int(n/2))+[-1]*(int(n/2)))
        else:
            b=np.array([2]+[1]*(int((n-3)/2))+[-1]*(int((n+1)/2)))
        c=a+b
        if 0 in c:
            print("no")
        elif 0 not in c:
            print("yes")