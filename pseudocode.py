def f(n):
    if n<=10:
        return
    print(n-1)
    f(n-1)
    print(n-1)
f(13)
