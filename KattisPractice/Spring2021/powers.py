a, b = list(map(int, input().split()))
if a % 2 == 0:
    print((a//2)**b % a)
else:
    print(0)
