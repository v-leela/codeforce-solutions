n=int(input())
for i in range(n):
    s=input()
    n,a,b=map(int,s.split())
    """ print(n,a,b) """
    if n%2:
        p1=int(((n-1)/2)*b+a)
        p2=n*a
    else:
        p1=int((n/2)*b)
        p2=n*a
    print(min(p1,p2))