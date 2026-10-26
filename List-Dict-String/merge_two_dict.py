a = {"name": "Abhi", "color": "blue", "shape": "round"}
b = {"name": "aman", "color": "blue", "length" : 3}

# merged = {**a, **b}
# print(f"original", a)
# print(f"original", b)
# print("Merged:", merged)

def merge_dicts(a,b):
    return {**a, **b}

result = merge_dicts(a,b)
print(result)


print(a)
print(b)