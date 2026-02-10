n = int(input())

values = []

for _ in range(n):
    num = float(input())
    values.append(num)

t = tuple(values)

average = sum(t) / n

print("Tuple:", t)
print("Average:", average)
