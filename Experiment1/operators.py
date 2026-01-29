'''Truth table for different operators'''

print(f"{'a':<5} {'b':<5} {'a&b':<5} {'a|b':<5} {'a^b':<5} {'not a':<7} {'not b':<7} {'not(a&b)':<10} {'not(a^b)':<10}")

for i in range(4):
    a = i // 2
    b = i % 2
    print(f"{a:<5} {b:<5} {a & b:<5} {a | b:<5} {a ^ b:<5} {int(not a):<7} {int(not b):<7} {int(not (a & b)):<10} {not(a^b):<10}")
