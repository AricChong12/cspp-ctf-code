program = """
92 7 + . 108 7 + . 105 7 + . 105 7 + . 116 7 + .
107 7 + . 105 7 + . 103 7 + . 88 7 + . 92 7 + .
45 7 + . 101 7 + . 92 7 + . 110 7 + . 101 7 + .
90 7 + . 109 7 + . 104 7 + . 107 7 + . 118 7 + .
"""

stack = []
output = []

for token in program.split():
    if token.isdigit():
        stack.append(int(token))

    elif token == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)

    elif token == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)

    elif token == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)

    elif token == '.':
        output.append(chr(stack.pop()))

print(''.join(output))