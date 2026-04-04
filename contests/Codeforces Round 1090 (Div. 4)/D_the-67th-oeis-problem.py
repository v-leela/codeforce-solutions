#wrong answer on test 2
t=int(input())
for _ in range(t):
    n=int(input())
    l="1 2"
    app=2
    if n==1:
        print("1")
    elif n==2:
        print(l)
    else:
        for i in range(2,n):
            app=app*2
            l=l+" "+str(app)
        print(l)
