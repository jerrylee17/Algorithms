n, h, l = list(map(int, input().split(' ')))

horrorList = list(map(int, input().split(' ')))
similarities = []

for i in range(l):
    x = list(map(int, input().split(' ')))
    similarities.append(x)

movies = [n+1 for i in range(n)]
for elem in horrorList:
    movies[elem] = 0

queue = []
for i, similar in enumerate(similarities):
    m1, m2 = similar
    # Both infinity can't do anything
    if movies[m1] == n+1 and movies[m2] == n+1:
        queue.append(similar)
        continue
    # Modify the one that's infinity
    elif movies[m1] == n+1:
        movies[m1] = movies[m2] + 1
    elif movies[m2] == n+1:
        movies[m2] = movies[m1] + 1
    # Change the movie values
    else:
        movies[m1], movies[m2] = min(
            movies[m1], movies[m2] + 1), min(movies[m2], movies[m1] + 1)
    # Check all the elements that weren't working before
    for j, elem in enumerate(queue):
        e1, e2 = elem
        # Still not working
        if movies[e1] == n+1 and movies[e2] == n+1:
            continue
        # One works
        elif movies[e1] == n+1:
            movies[e1] = movies[e2] + 1
        elif movies[e2] == n+1:
            movies[e2] = movies[e1] + 1
        # Both works
        else:
            movies[e1], movies[e2] = min(
                movies[e1], movies[e2] + 1), min(movies[e2], movies[e1] + 1)
        queue.pop(j)

# Final scan
for j, elem in enumerate(queue):
    e1, e2 = elem
    # Still not working
    if movies[e1] == n+1 and movies[e2] == n+1:
        continue
    # One works
    elif movies[e1] == n+1:
        movies[e1] = movies[e2] + 1
    elif movies[e2] == n+1:
        movies[e2] = movies[e1] + 1
    # Both works
    else:
        movies[e1], movies[e2] = min(
            movies[e1], movies[e2] + 1), min(movies[e2], movies[e1] + 1)

print(movies.index(max(movies)))
