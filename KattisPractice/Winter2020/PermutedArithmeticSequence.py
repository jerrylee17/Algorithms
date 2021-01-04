tc = int(input())


def determineArithmetic(arr):
    diff = arr[1]-arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != diff:
            return False
    return True


for _ in range(tc):
    k, *nums = list(map(int, input().split(' ')))
    if determineArithmetic(nums):
        print("arithmetic")
    else:
        if determineArithmetic(sorted(nums)):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")
