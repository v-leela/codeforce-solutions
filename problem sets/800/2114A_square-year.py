"""
tags: binary search, brute force, math
"""

import math
t=int(input())
for i in range(t):
    year=int(input())
    r=math.isqrt(year)
    if r*r==year:
        print(0,r)
    else:
        print(-1)
