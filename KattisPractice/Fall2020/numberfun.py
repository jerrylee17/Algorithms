tc = int(input())

for _ in range(tc):
    a, b, c = list(map(int, input().split(' ')))
    if (a+b == c) or (a-b == c) or (b-a == c) or (a*b == c) or (b != 0 and a/b == c) or (a != 0 and b/a == c):
        print("Possible")
    else:
        print("Impossible")
