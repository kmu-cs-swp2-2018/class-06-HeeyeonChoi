import time
import random


def seqsearch(nbrs, target):
    for idx in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return idx
    
    return -1


def recbinsearch(L, l, u, target):
    if u < l :
        return -1
    mid = (l + u) // 2

    if L[mid] == target:
        return mid
    elif L[mid] > target:
        u = mid - 1
    else:
        l = mid + 1

    return recbinsearch(L, l, u, target)



numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
count = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers)-1, target)
    if idx == -1:
        count += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, count, ts))

ts = time.time()

# sequential search
count = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        count += 1
ts = time.time() - ts

print("seqsearch %d: not found %d time %.6f" % (numoftargets, count, ts))
