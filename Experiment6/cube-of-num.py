def cube_sum(n):
    a = n - 1
    sum = a * a * ((a + 1) ** 2) // 4
    return sum

print(cube_sum(5))