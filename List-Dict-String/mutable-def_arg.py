# def f(x, acc=[]):
#     acc.append(x)
#     return acc


# print(f(10))
# print(f(20))
# print(f(30))

##correct one

def f(x, acc= None):
    if acc is None:
        acc = []

    acc.append(x)
    return acc

# print(f(10))
# print(f(10))
# print(f(10))

lst1 = [10,20]

print(f(225, lst1))