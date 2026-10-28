import copy

num = [[1,2], [3,4]]

shallow_copy = num.copy()
deep_copy = copy.deepcopy(num)

shallow_copy[0][1] = 55
deep_copy[1][0] = 100

print(f"original:{num}")
print(f"shallow:{shallow_copy}")
print(f"deep :{deep_copy}")

shallow_copy[0].append(54)

print(f"shallow new {shallow_copy}")

