nums=int(input("Enter Number"))

copy=nums
nums2=0
while(copy):
    d=copy%10
    nums2=nums2*10+d
    copy//=10

if (nums2==nums):
    print(f"Palindrome")
    exit()
print(f"Not palindrome")