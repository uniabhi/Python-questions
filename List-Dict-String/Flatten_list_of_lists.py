# def flatten(list_of_lists):
#     return [item for sublist in list_of_lists for item in sublist]


# data = [[1,2,3], [4,5,6], [7,8], [9]]

# print(flatten(data))


# ----M2------

def flatten_loop(lists_of_lists):
    result = []
    for sublist in lists_of_lists:
        for item in sublist:
            result.append(item)
    return result

data = [[1,2,3], [4,5,6], [7,8], [9]]

print(flatten_loop(data))