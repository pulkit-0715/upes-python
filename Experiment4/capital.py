st = input("Enter String: ")
ct = 0
for i in range(len(st)):
    if st[i].isupper():
        ct = ct + 1

print(f"Number of capitals is {ct}")