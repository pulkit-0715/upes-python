count = 0
vowel_count = 0
longest = ""

with open("/Users/pulkitsingh/Documents/B.Tech/upes-python/Experiment7/name.txt", "r") as file:
    for line in file:
        name = line.strip()
        if name == "":
            continue

        count += 1

        if name[0].lower() in "aeiou":
            print(name)
            vowel_count += 1

        if len(name) > len(longest):
            longest = name

print("Total names:", count)
print("Names starting with vowel:", vowel_count)
print("Longest name:", longest)