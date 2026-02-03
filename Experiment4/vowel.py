st=input("Enter String ")
ct=0;
for i in range(len(st)):
    if st[i]=='a' or st[i]=='e' or st[i]=='i' or st[i]=='o'or st[i]=='u':
            ct=ct+1;

print(f"Number of vowels are {ct}")
