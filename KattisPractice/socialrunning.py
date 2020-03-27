testcases = int(input())

arr = []
for i in range(testcases):
    arr.append(int(input()))

sums = [arr[i]+arr[(i+2)%len(arr)] for i in range(len(arr))]

print(min(sums))
