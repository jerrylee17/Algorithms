n = int(input())
questions = []
for i in range(n):
    questions.append(input())

curr = questions[0]
count = 0
for n in questions[1:]:
    if n == curr:
        count += 1
    curr = n
print(count)
