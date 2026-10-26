from collections import defaultdict

# items = ["apple", "banana", "apricot", "blueberry", "cherry"]

# grouped = defaultdict(list)

# for item in items:
#     key = item[0]
#     grouped[key].append(item)

# print(dict(grouped))

# ==== M2====

# from collections import defaultdict

# def group_by(items, key_func):
#     groups = defaultdict(list)

#     for item in items:
#         groups[key_func(item)].append(item)
#     return dict(groups)

# words = ["apple", "bat", "cat", "ant", "ball", "carrot"]

# print(group_by(words, lambda w: w[0]))



# from collections import defaultdict

# def group_by(items, key_func):
#     groups = defaultdict(list)

#     for item in items:
#         groups[key_func(item)].append(item)
#     return dict(groups)

# words = ["apple", "bat", "cat", "ant", "ball", "carrot"]

# print(group_by(words, len))

# ==========================================m3 ===== 
def group_by_manual(items, key_func):
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

words = ["apple", "bat", "cat", "ant", "ball", "carrot"]
print(dict(group_by_manual(words, lambda x: x[0])))