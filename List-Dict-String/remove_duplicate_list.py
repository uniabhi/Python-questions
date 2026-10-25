def remove_duplicates(my_list):
    seen = set()
    result = []
    for item in my_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

my_list = [1,1,2,3,4,4,5,5,6]
print(remove_duplicates(my_list))