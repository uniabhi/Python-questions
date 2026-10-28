# functions = [lambda: i for i in range(3)]  ##late binding

# for func in functions:
#     print(func())

##correct method
functions = [lambda i = i:i for i in range(3)]

for func in functions:
    print(func())

