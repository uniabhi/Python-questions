import copy
numbers = [1,2,3,4,5,6,7,8,9,10]

nums_kept = copy.deepcopy(numbers)

for num in nums_kept:
    if num%2==0:
        numbers.remove(num)

print(numbers)
print(f"backup number which copied{nums_kept}")