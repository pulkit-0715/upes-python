n=int(input("Enter a numbr to check if its perfect or not "))
sum=0
for i in range(1,((n//2)+1)):
    if(n%i==0):
        sum=sum+i

if(sum==n):
    print(f"The Number {n} is perfect number")
else:
    print(f"he Number {n} is NOT A perfect number")