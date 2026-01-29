n=int(input("Enter number"))
sums=0
for i in range(1,n+1,1):
    sums=sums+(1/i)

print(f"Sum is {sums}")