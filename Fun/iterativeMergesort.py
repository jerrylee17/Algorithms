import numpy as np
import time
import sys


def generateRandomArray():
    arr = np.random.random_integers(1, 10_000_000, 200_000)
    arr = arr.tolist()
    return arr


def mergeLists(a, b):
    res = []
    while a and b:
        if a[0] > b[0]:
            res.append(b.pop(0))
        else:
            res.append(a.pop(0))
    res.extend(a)
    res.extend(b)
    return res


def iterativeMergeSort(a):
    curr_size = 1
    while curr_size < len(a) - 1:
        left = 0
        while left < len(a) - 1:
            mid = left + curr_size
            right = mid + curr_size
            a[left:right] = mergeLists(a[left: mid], a[mid: right])
            left += 2*curr_size
        curr_size *= 2
    return a


def recurseMergeSort(a):
    if len(a) == 1:
        return a
    mid = len(a)//2
    return mergeLists(recurseMergeSort(a[:mid]), recurseMergeSort(a[mid:]))


a = generateRandomArray()
# print("Initial array: ", a)
iterativeArray = a.copy()
recursiveArray = a.copy()
sortArray = a.copy()
sortedArray = a.copy()
numpyArray = np.array(a)
timestaken = []

# Iterative merge sort
start_time = time.time()
iterativeMergeSort(iterativeArray)
timetaken = time.time() - start_time
timestaken.append(("iterative", timetaken))
print("Iterative sort:", timetaken)
sys.stdout.flush()
# print(iterativeArray)

# Recursive sort
start_time = time.time()
newArr = recurseMergeSort(recursiveArray)
timetaken = time.time() - start_time
timestaken.append(("recursive", timetaken))
print("Recursive sort:", timetaken)
sys.stdout.flush()
# print(newArr)

# Built in sort function sort
start_time = time.time()
sortArray.sort()
timetaken = time.time() - start_time
timestaken.append(("Built in sort", timetaken))
print("Built in sort function:", timetaken)
sys.stdout.flush()
# print(sortArray)

# Built in sorted function sort
start_time = time.time()
newArr = sorted(sortedArray)
timetaken = time.time() - start_time
timestaken.append(("Built in sorted", timetaken))
print("Built in sorted functions sort:", timetaken)
sys.stdout.flush()
# print(newArr)

# Numpy sort
start_time = time.time()
np.sort(numpyArray)
timetaken = time.time() - start_time
timestaken.append(("Numpy sort", timetaken))
print("Numpy sort:", timetaken)
sys.stdout.flush()

timestaken.sort(key=lambda x: x[1])
timestaken = [t[0] for t in timestaken]
print(timestaken)
