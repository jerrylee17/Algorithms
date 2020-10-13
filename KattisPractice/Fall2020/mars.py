n, m = list(map(int, input().split(' ')))
acre = {}

for i in range(1, n + 1):
    ph = float(input())
    acre[ph] = acre.get(ph, []) + [i]


# def checkMajority(phList):
#     freqList = {}
#     for elem in phList:
#         freqList[elem] = freqList.get(elem, 0) + 1
#     if max(freqList.values()) >= (len(phList) // 2 + 1):
#         print('usable')
#     else:
#         print('unusable')
def bin_search(arr, target, high=False):
    l = 0
    h = len(arr)
    while l < h:
        mid = (l + h) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    if high:
        return mid - 1
    return mid + 1


# print(acre)
# print()
for _ in range(m):
    a, b = list(map(int, input().split(' ')))
    # checkMajority(acre[a-1:b])
    # print('a, b', a, b)
    for s, position in acre.items():
        aPos = bin_search(position, a, False)
        bPos = bin_search(position, b, True)
        # print('ap, bp', aPos, bPos)
        if (bPos - aPos + 1) >= ((b - a + 1) // 2 + 1):
            print('usable')
            break
    else:
        print('unusable')
