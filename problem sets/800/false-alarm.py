t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    o=0
    while o<n:
        if a[o]==0:
            o+=1
        elif a[o]==1 and x!=-1:
            o+=x
            x=-1
        else:
            break
    if o<n:
        print("no")
    else:
        print("yes")
