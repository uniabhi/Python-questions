# items = [1,2,3,4,5,6,7,8]

# n= 3

# chunks = [items[i: i+n] for i in range(0, len(items), n)]

# print(chunks)


# --- M2----

def chunk_list_loops(items, n):
    chunks = []
    for i in range(0, len(items), n):
        chunks.append(items[i:i+n])
    return chunks

nums = [1,2,4,5,6,6,8,8,9,4,5]
print(chunk_list_loops(nums, 4))