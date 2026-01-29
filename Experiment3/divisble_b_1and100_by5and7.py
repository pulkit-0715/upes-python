count = 0

print("Numbers divisible by 5 or 7:")

for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        print(f"{i}\n")
        count += 1

print(f"\n\nTotal count: {count}")