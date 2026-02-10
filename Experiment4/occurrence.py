st = input("Enter String: ").upper()
unique_chars = set(st)

for char in unique_chars:
    count = st.count(char)
    print(f"{count}{char}")
