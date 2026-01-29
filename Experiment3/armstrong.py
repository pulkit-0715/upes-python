num = int(input("Enter value of n: "))
copy = num
power = 0

temp_copy = num
while temp_copy > 0:
    temp_copy //= 10
    power += 1

is_arm = 0
temp_copy = num

while temp_copy > 0:
    d = temp_copy % 10
    is_arm += d ** power
    temp_copy //= 10

if is_arm == num:
    print("Is armstrong")   
else:
    print("Is not armstrong")