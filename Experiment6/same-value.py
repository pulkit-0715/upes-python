data = {'a': 10, 'b': 10, 'c': 10}
check = lambda d: len(set(d.values())) == 1
if check(data):
    print("All values are same")
else:
    print("Values are not same")