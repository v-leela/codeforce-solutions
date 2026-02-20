"""
tags: bitmasks, brute force, greedy, implementation, math
"""

t=int(input())
for i in range(t):
    n=int(input())
    M=[]
    row=[0 for _ in range(n+2)]
    M.append(row)
    for j in range(n):
        row=[0]
        for k in range(1,n+1):
            ele=j*n+k
            row.append(ele)
        row.append(0)
        M.append(row)
    row=[0 for _ in range(n+2)]
    M.append(row)
    def Max(A):
        value=[]
        for a in range(1,n+1):
            for b in range(1,n+1):
                sum=A[a][b]+A[a][b-1]+A[a][b+1]+A[a-1][b]+A[a+1][b]
                value.append(sum)
        return max(value)
    print(Max(M))
