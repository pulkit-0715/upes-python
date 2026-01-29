nums=int(input("Enter Number"))

copy=nums
sums=0
while(copy):
    d=copy%10
    sums+=d
    copy//=10

print(f"Sum is: {sums}")