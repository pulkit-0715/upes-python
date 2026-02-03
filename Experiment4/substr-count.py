st = input("Enter String: ")
subst = input("Enter Substring: ")

sub_len = len(subst)
ct = 0

for i in range(len(st) - sub_len + 1):
    wd = st[i : i + sub_len]
    if wd == subst:
        ct = ct + 1

print(f"Number of occurrences: {ct}")