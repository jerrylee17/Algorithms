tc = int(input())

for _ in range(tc):
    p = input()
    if p[:10].lower() == 'simon says':
        print(p[11:])