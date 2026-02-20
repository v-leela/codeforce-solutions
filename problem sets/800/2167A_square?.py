"""
tags: math, sortings
"""

t=int(input())
for i in range(t):
    l=input()
    lengths=l.split()
    if lengths[0]==lengths[1]==lengths[2]==lengths[3]:
        print("yes")
    else:
        print("no")
