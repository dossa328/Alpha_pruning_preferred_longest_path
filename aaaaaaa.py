import random

outputlist = []
tlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while (1):
    out = random.sample(tlist, 3)
    outputlist.append(out)

    if len(outputlist) >= 9000000:
        break

remove = list(set(map(tuple, outputlist)))
print(remove)
print(len(remove))
