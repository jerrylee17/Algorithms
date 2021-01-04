from collections import Counter
sequence = input()

c = Counter(sequence)

result = c['T']**2 + c['C']**2 + c['G']**2 + min([c['T'], c['C'], c['G']])*7
print(result)
