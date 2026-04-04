#wrong answer on test 2
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for x in a:
        res^=x
    print(res)
    """ for i in range(n-1):
        mx=min(a)
        a.remove(mx)
        for j in range(len(a)):
            a[j]=a[j]^mx
        print(a)
    print(a[0]) """