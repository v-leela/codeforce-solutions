"""
tags: math
"""

def d3or6(n):
    if n%3==0 or n%6==0:
        return 1
    else:
        return 0
    
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x<2 or y>x/2 or x<(-4)*y:
        print("no")
    elif y<0:
        if d3or6(x+4*y):
            print("yes")
        else:
            print("no")
    elif y==0:
        if d3or6(x):
            print("yes")
        else:
            print("no")
    elif y>0:
        if d3or6(x-2*y):
            print("yes")
        else:
            print("no")
    else:
        print("no")