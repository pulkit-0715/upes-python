st=input("Enter String ")
st=st+" "
wd=""
for i in range(len(st)):
    if(st[i]!=' '):
        wd=wd+st[i]
    else:
        print(f"{wd}")
        wd=""

        