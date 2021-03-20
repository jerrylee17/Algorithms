from collections import Counter
n, d = list(map(int, input().split()))
nums = list(map(lambda x: int(x) // d, input().split()))
occurs = Counter(nums)
tot = 0
for k, v in occurs.items():
    tot += v * (v-1) // 2

print(tot)

