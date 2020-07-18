def mergeSort(a):
    curr_size = 1
    while curr_size < len(a) - 1:
        left = 0
        while left < len(a) - 1:
            mid = left + curr_size
            right = mid + curr_size
            sortedList = mergeLists(a[left: mid], a[mid: right])
            a[left: right] = sortedList
            left += 2*curr_size
        curr_size *= 2
    return a
    

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

test = [5, 4, 7, 9, 15, 2, 17]
result = mergeSort(test)

print(result)
