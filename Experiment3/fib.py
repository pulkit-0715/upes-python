a=0
b=1
c=0
num = int(input("Enter value of n: "))
print(f"{a}\n{b}")
for i in range(num,1):
    a=b
    b=c
    c=a+b
    print(f"{c}")