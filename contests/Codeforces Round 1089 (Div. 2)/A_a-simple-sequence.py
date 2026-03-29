t=int(input())
for _ in range(t):
    n=int(input())
    if n==2:
        print("2 1")
    else:
        result=[n-1,n,n-2]
        i=n-3
        while i>0:
            result.append(i)
            i-=1
        print(" ".join(list(map(str,result))))
