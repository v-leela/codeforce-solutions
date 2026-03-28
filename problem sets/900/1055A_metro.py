n,s=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

if a[0]==0 or (a[s-1]==0 and b[s-1]==0):
    print("NO")
elif a[s-1]==1:
    print("YES")
elif a[s-1]==0:
    i=s
    while i<n:
        if a[i]&b[i]:
            print("YES")
            break
        else:
            i+=1
    if i==n:
        print("NO")