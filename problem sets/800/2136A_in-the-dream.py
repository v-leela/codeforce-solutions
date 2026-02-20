""""
tags: greedy, math
""""

t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    """ print(a) """
    max1,min1=max(a,b),min(a,b)
    max2,min2=max(c-a,d-b),min(c-a,d-b)
    if max1%2:
        num2_1=(max1//2)+1
    else:
        num2_1=max1/2
    if max2%2:
        num2_2=(max2//2)+1
    else:
        num2_2=max2/2
    if min1>=num2_1-1 and min2>=num2_2-1:
        print("yes")
    else:
        print("no")
