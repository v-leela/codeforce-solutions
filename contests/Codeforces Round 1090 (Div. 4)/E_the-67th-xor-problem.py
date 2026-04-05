t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mx=0
    for i in range(n):
        b=a[:i]+a[i+1:]
        for j in range(n-1):
            xor=b[j]^a[i]
            if xor>mx:
                mx=xor
    print(mx)