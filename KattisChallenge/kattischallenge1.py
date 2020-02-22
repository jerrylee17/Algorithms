c = input()

c = c.split(' ')
if len(set(c)) == len(c):
    print("yes")
else:
    print("no")
