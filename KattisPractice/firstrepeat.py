def firstRepeat(s):
    if len(s) == 0:
        return ""
    d = set()
    for i in range(len(s)):
        if s[i] in d and s[i] != " ":
            return s[i]
        d.add(s[i])
    return ""

print(firstRepeat("habib is noob"))
