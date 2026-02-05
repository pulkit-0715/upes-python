n=int(input("Enter Number to find if its automorphic number"))

nsq=n*n;
copy=n;
ct=0
while(copy!=0):
    copy=copy//10;
    ct=ct+1;

rem=nsq%(10**ct)

if(rem==n):
    print(f"{n} is an autopmorphic number")
else:
    print(f"{n} is NOT an autopmorphic number")