n=int(input("Enter number of fruits"))

s1=set()
s2=set()
for i in range(n):
    s1.add(input("Enter fruits for s1: "))

for i in range(n):
    s2.add(input("Enter fruits for s2: "))

print("Common ",s1&s2)
print("Only in s1 ",s1-s2)
print("Only in s2 ",s2-s1)
print("Total fruits count: ",len(s1|s2))