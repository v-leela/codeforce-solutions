n=int(input())
P=0
for _ in range(n):
    event=input().split()
    event[1]=int(event[1])
    """ print(event[1]) """
    if event[0]=="P":
        P+=event[1]
    else:
        B=event[1]
        if B-P>=1:
            print("yes")
            P=0
        else:
            print("no")
            P-=B