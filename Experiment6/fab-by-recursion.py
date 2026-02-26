def fibonacci(n):
    if n <= 0:
        return
    elif n == 1:
        print(0, end=" ")
    elif n == 2:
        print(0, 1, end=" ")
    else:
        fibonacci(n - 1)
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        print(b, end=" ")

fibonacci(7)