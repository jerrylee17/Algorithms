n, r, k = list(map(int, input().split()))

if n <= r and n <= k:
    print(max(r, k)*2)
else:
    d = max(n, k+abs(k-r))
    p = d+r
    if p % 2 == 1: 
        p += 1
    print(p)

'''
n highest:
r > k: n + r
k > r: 

r highest:
2*r

k highest:
2*k
'''
