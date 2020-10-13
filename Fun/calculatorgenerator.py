def generateStatement(x, y, op):
    s = f'if op == \'{op}\':\n'
    if op == '+':
        s += f'    if x == {x} and y == {y}:\n'
        s += f'        print(f\'The sum is: {x+y}\')\n'
    elif op == '-':
        s += f'    if x == {x} and y == {y}:\n'
        s += f'        print(f\'The difference is: {x-y}\')\n'
    elif op == '*':
        s += f'    if x == {x} and y == {y}:\n'
        s += f'        print(f\'The product is: {x*y}\')\n'
    elif op == '/':
        s += f'    if x == {x} and y == {y}:\n'
        if y == 0:
            s += f'        print("Cannot divide by 0")\n'
        else:
            s += f'        print(f\'The quotient is {x/y}\')\n'
    return s


with open('calculator.py', 'w') as f:
    f.write("x, y, *_ = list(map(int, input('Welcome to calculator! Enter 2 integers please: ').split(' ')))\n")
    f.write("op = input('Please enter an operation: ')\n")
    for x in range(50):
        for y in range(50):
            s = generateStatement(x, y, '+')
            f.write(s)
            s = generateStatement(x, y, '-')
            f.write(s)
            s = generateStatement(x, y, '*')
            f.write(s)
            s = generateStatement(x, y, '/')
            f.write(s)
