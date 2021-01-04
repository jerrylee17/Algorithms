targetTime = 210

k = int(input())
n = int(input())

question = []
for _ in range(n):
    q = input().split(' ')
    question.append(q)

subtotal = 0
for q in question:
    subtotal += int(q[0])
    if subtotal >= targetTime:
        print(k)
        break
    if q[1] == 'T':
        k += 1
        if k == 9:
            k = 1
