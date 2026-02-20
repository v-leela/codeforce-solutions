t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    result=a[0]
    if n==1:
        print(a[0])
    else:
        """ s.append(a[0])
        result="".join(s)
        for j in range(1,n):
            lst=[a[j],result]
            result="".join(sorted(lst))
            print(result) """
        for j in range(1,n):
            if a[j]+result>result+a[j]:
                result+=a[j]
            else:
                result=a[j]+result
        print(result)
