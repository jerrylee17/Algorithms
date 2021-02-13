n = int(input())

characters = []
for _ in range(n):
    c = list(input().split(' '))
    characters.append(c)


def solve(characters):
    done = set([])
    largestGroup = 0
    for i, c in enumerate(characters):
        # Already in group
        if c[0] in done:
            continue
        group = set([c[0]])
        speaking = set([c[1]])
        hearing = set(c[1:])
        for j, d in enumerate(characters[i+1:]):
            # Can converse
            # 1. They can understand someone speaking
            # 2. Them speaking can be understood by someone else
            if (speaking & set(d[1:])) and (d[1] in hearing):
                # Add them to group
                group.add(d[0])
                # Add their language to group since they speak it
                speaking.add(d[1])
                # Add the hearing to the things the group can hear
                hearing = hearing | set(d[1:])
        largestGroup = max(len(group), largestGroup)
        done = done | group
    print(len(characters) - largestGroup)
    return

solve(characters)
            

