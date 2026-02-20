n=int(input())
for i in range(n):
    b,k,a=map(int,input().split())
    st=a//(b+k)
    if (st)*(b+k)+b>=a+0.5:
        print("no")
    else:
        print("yes")