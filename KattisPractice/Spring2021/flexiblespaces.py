w, p = map(int, input().split())
partitions = list(map(int, input().split()))
partitions.append(w)

output = set()

for par in partitions:
    output.add(par)
    for o_par in partitions:
        if par == o_par:
            break
        output.add(abs(par - o_par))

print(" ".join(str(part) for part in sorted(output)))