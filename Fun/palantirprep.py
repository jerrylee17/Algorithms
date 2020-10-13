test_data = [
    ["jerry", "930"],
    ["jerry", "1030"],
    ["jerry", "1130"],
    ["jerry", "940"],
    ["jerry", "950"],
    ["jerry", "1020"],
    ["jerry", "1120"],
    ["habib", "1120"],
    ["habib", "1020"],
    ["habib", "920"],
    ["habib", "1220"],
]


def checkIfhourApart(t1, t2):
    # Given t2 > t1
    h1, m1 = t1[:-2], t1[-2:]
    h2, m2 = t2[:-2], t2[-2:]
    if int(h2) - int(h1) > 1:
        # not hour apart
        return False
    if int(h2) == int(h1):
        return True
    return False if int(m2) > int(m1) else True


def checkForThree(data):
    people = {}
    result = []
    for d in data:
        people[d[0]] = people.get(d[0], [])
        people[d[0]].append(d[1])
    for p in people.items():
        if len(p[1]) >= 3:
            result.append((p[0], p[1]))
    return result


def checkIfSus(test_data):
    if len(test_data) < 3:
        return
    data = sorted(test_data, key=lambda x: x[1])
    names = set([])
    result = []
    left = 0
    right = 0
    while right < len(data):
        if left == right:
            right += 1
            continue
        if left < right and data[left][0] in names:
            left += 1
            continue
        if data[right][0] in names:
            right += 1
            continue

        if checkIfhourApart(data[left][1], data[right][1]):
            result.extend(checkForThree(data[left:right]))
            try:
                names.add(result[-1][0])
            except:
                pass
            right += 1
        else:
            left += 1

    print(result)


checkIfSus(test_data)
print(checkIfhourApart('920', '1120'))
