n = int(input())

count = [0, 0, 0, 0]

for i in range(n):
    value = int(input())
    if 0 <= value <= 3:
        count[value] += 1

for i in range(4):
    print(i, "occurred", count[i], "times")
