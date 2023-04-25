def fib_sum(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        first,second=0,1
        result=first+second
        for i in range(2,n+1):
            next=first+second
            result+=next
            first=second
            second=next
        print(result)
fib_sum(4)