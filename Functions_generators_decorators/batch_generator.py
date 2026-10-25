##method 1

def make_batches(items,n):
    batch = []

    for item in items:
        batch.append(item)

        if len(batch) ==n:
            yield batch
            batch = []

    if len(batch) >0:
            yield batch

numbers = [1,2,3,4,5,6,7,8]

for group in make_batches(numbers, 3):
    print(group)


##method 2::::
def batch_generator(items,n):
    for i in range(0,len(items), 3):
        batch = items[i:i+n]
        yield batch 

gen = batch_generator([1,2,3,4,5,6,7,8], 3)
for batch in gen:
    print(batch)