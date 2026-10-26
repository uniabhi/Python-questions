# from collections import Counter

# def freq_n_items(items, n):   ## method 1: Counter.most_common
#     counts = Counter(items)
#     return counts.most_common(n)


# fruits = ["apple", "banana", "apple", "orange", "banana", "apple", "mango", "banana", "apple"]

# print(freq_n_items(fruits,2))

##method 2:  sorted with a key

# def freq_n_items(items, n):
#     counts = {}
#     for item in items:
#         counts[item] = counts.get(item, 0) +1 

#     sorted_items = sorted(counts.items(), key = lambda pair: pair[1] , reverse= True)
#     return sorted_items[:n]

# fruits = ["apple", "banana", "apple", "orange", "banana", "orange", "apple", "mango", "banana", "apple"]
# print(freq_n_items(fruits,3))


#  sorted with a key - M3
items = ["apple", "banana", "apple", "orange", "banana", "apple", "mango"]
n = 4

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] = frequency[item]+1
    else:
        frequency[item] = 1

sorted_items = sorted(
    frequency.items(),
    key = lambda pair: pair[1],
    reverse=True
)

top_items = sorted_items[:n]
print(top_items)