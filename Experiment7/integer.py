numbers = []

with open("/Users/pulkitsingh/Documents/B.Tech/upes-python/Experiment7/integer.txt", "r") as file:
    for line in file:
        num = int(line.strip())
        numbers.append(num)

maximum = max(numbers)

average = sum(numbers) / len(numbers)

count = 0
for num in numbers:
    if num > 20:
        count += 1

print("Maximum number:", maximum)
print("Average:", average)
print("Numbers greater than 20:", count)