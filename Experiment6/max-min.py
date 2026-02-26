def find_max_min(numbers):
    
    if len(numbers) == 0:
        return None, None
    
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum

nums = [10, 5, 25, 2, 8, 15]
max_value, min_value = find_max_min(nums)

print("Maximum:", max_value)
print("Minimum:", min_value)