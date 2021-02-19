tc = int(input())

words = set([])
for _ in range(tc):
    w = input()
    # Process this
    w = w.lower().replace(' ', '-')
    words.add(w)
print(len(words))
