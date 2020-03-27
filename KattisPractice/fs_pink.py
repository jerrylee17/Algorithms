testcases = int(input())

counter = 0
for i in range(testcases):
    s = input().lower()
    if 'rose' in s or 'pink' in s:
        counter += 1
if counter == 0:
    print('I must watch Star Wars with my daughter')
else:
    print(counter)