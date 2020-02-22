def oct_to_bin(x):
    s = ''
    for digit in x:
        tmp = str(bin(int(digit))[2:])
        s += ('0'*(3-len(tmp)))+tmp
    return s

def bin_to_hex(x):
    s = ''
    for i in range(int(len(x)/4)):
        sub = str(x[i*4: i*4+4])
        b10 = int(sub[3]) + 2*int(sub[2]) + 4*int(sub[1]) + 8*int(sub[0])
        b16 = hex(b10)[2:]
        s += str(b16)
    return s

x = input()
try:
    if int(x) == 0:
        print('0')
except:
    pass

res = ''
if len(x) % 4 != 0:
    x = ('0'* (4 - (len(x)%4))) + x
for i in range(int(len(x)/4)):
    ind = i*4
    sub = x[ind:ind+4]
    sub = oct_to_bin(sub)
    sub = bin_to_hex(sub)
    res += sub
z = 0
for d in res:
    if d == '0':
        z += 1
    else:
        break
print(res[z:].upper())
