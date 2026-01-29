'''
Factorial using while
'''
num=int(input("Enter value of n "))
fact=1
while(num>0):
    fact*=num
    num-=1

print(f"Factorial is {fact}")