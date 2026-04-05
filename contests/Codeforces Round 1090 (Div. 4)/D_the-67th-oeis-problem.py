def nth_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

t=int(input())
for _ in range(t):
    n=int(input())
    list1=[1]*n
    for i in range(1,n):
        list1[i-1]=list1[i-1]*nth_prime(i)
        list1[i]=list1[i]*nth_prime(i)
    print(" ".join(list(map(str,list1))))