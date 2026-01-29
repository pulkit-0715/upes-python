text = input("Enter a string: ")
result = ""

for char in text:
    if 'a' <= char <= 'z':
        result += char.upper()
    else:
        
        result += char

print(f"Manual Result: {result}")