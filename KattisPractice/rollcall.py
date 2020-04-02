import sys

arr = []

for line in sys.stdin:
    if not line.strip():
        break
    arr.append(line.strip().split(' '))

arr.sort(key=lambda x:(x[1], x[0]))


for i,a in enumerate(arr):
    if a[0] in [x[0] for x in (arr[:i]+arr[i+1:])]:
        print(a[0], a[1])
    else:
        print(a[0])
