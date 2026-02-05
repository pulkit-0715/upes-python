n = int(input("Enter Number to find if its Factorian number: "))
total_sum = 0
copy = n

while copy > 0:
    d = copy % 10
    
    fact = 1
    for i in range(1, d + 1):
        fact *= i
    
    total_sum += fact
    copy //= 10 

if n == total_sum:
    print(f"{n} is a Factorian number.")
else:
    print(f"{n} is not a Factorian number.")