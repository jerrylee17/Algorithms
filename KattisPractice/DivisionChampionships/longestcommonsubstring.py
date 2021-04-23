n = int(input())
s, min_len, smallest  = set(), 1000, ''
for i in range(n):
    curr = input()
    if len(curr) < min_len:
        smallest = curr
        min_len = len(curr)
    if curr not in s:
        s.add(curr)

if n == 1:
    print(min_len)
else:
    largest = 0
    inside = True
    for i in range(min_len):
        for j in range(i+1, min_len+1):
            for k in s:
                if k.find(smallest[i:j]) < 0:
                    inside = False
                    break
            if inside and largest < (j - i):               
                largest = j - i
            inside = True
    print(largest)