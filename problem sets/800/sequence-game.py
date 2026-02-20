t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    """ for j in range(min(a),max(a)+1):
        print(j) """
    if max(a)<x or min(a)>x:
        print("no")
    else:
        """ while len(a)==1:
            x=a[0]
            y=a[1] """
        """ z=max(a)
        y=min(a)
        while  """
        print("yes")
