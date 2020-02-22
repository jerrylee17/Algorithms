def anagram(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

print(anagram("fsda","asdf"))
