m,a,b,c = list(map(int, input().split(' ')))

result = "possible" if a+b+c <= 2*m else "impossible"
print(result)

