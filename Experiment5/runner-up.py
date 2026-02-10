n = int(input("Enter number of students: "))

score = []

print("Enter score of each student")

for i in range(n):
    score.append(int(input()))

score.sort()

value = score[n - 1]

i = n - 1
while i >= 0:
    if score[i] < value:
        value = score[i]
        break
    i -= 1

print("Runner up is", value)
