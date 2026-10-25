# def process_list():
#     numbers = [x *2 for x in range(1_000_000)]

#     for num in numbers:
#         print(num)


# def process_with_generator():
#     def number_generator():
#         for i in range(0, 1_000_000):
#             yield i *2

#     for num in number_generator():
#         print(num)

# process_list()
# process_with_generator()



##full_code


import sys
# print("=" * 50)
# print("LIST COMPREHENSION vs GENERATOR")
# print("=" * 50)

# print("\n small data (10 items)")
# print("-" * 50)

# list_small = [x *2 for x in range(10)]
# gen_small = [ x * 2 for x in range(10)]

# print(f"list: {list_small}")
# print(f"Generator: {gen_small}")
# print(f"List size: {sys.getsizeof(list_small)} bytes")
# print(f"Generator size: {sys.getsizeof(gen_small)} bytes")

list_mill = [x* 2 for x in range(1_000_000)]
gen_big = (x* 2 for x in range(1_000_000))

list_mem = sys.getsizeof(list_mill)
gen_mem = sys.getsizeof(gen_big)
print(list_mem)
print(gen_mem)




