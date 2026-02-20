"""
tags: implementation, math
"""

import math
t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(1)
    else:
        x=int(math.log2(n))
        print(2**x)
