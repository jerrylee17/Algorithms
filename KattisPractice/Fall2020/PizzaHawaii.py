tc = int(input())
import functools

def translate(translations, ingredients1, ingredients2):
    # case 1: neither exists --> add
    # case 2: ingredients1 exists already but ingredients2 does not
    # case 3: ingredients2 exists but ingredients1 does not
    for i1 in ingredients1:
        for i2 in ingredients2:
            if i1 not in translations.keys() and (
                i2 not in functools.reduce(lambda x, y: x+y, translations.values())):
                translations[i1] = [i2]

for i in range(tc):
    n = int(input())
    translations = {}
    for j in range(n):
        name = input()
        ingredients1 = input().split(' ')[1:]
        ingredients2 = input().split(' ')[1:]
        translate(translations, ingredients1, ingredients2)

