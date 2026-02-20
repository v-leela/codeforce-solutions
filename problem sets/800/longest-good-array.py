t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    diff=1
    len=1
    a=l
    for i in range(r-l):
        if a+diff<=r:
            a+=diff
            len+=1
            diff+=1
        else:
            break
    print(len)