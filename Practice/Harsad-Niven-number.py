num=int(input("Enter Number\n"))
sum=0;
copy=num;
while (copy!=0):
    n=copy%10;
    sum=sum+n;
    copy=copy//10

if(num%sum==0):
    print("Number {num} is Harsad Niven Number")
else:
    print("Number {num} is NOT Harsad Niven Number")
