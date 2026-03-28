t=int(input())
for _ in range(t):
    n,m,h=map(int,input().split())
    a=list(map(int,input().split()))
    rep=a
    for k in range(m):
        b,c=map(int,input().split())
        if rep[b-1]+c>h:
            rep=a
            print(rep[b-1]+c)
        else:
            rep[b-1]+=c
    print(a)