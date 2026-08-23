program = bytes.fromhex(
    "0139015a04020129015a0402012a015a0402012a015a04020121015a0402"
    "0129015a0402012e015a0402016e015a04020139015a04020131015a0402"
    "0105015a04020137015a0402013b015a04020139015a04020132015a0402"
    "016b015a04020134015a0402013f015a04020105015a0402012e015a0402"
    "0128015a0402013b015a04020139015a0402013f015a04020127015a0402"
)

stack = []
output = []

i = 0

while i < len(program):
    opcode = program[i]
    i += 1

    if opcode == 0x01:          # PUSH
        value = program[i]
        i += 1
        stack.append(value)

    elif opcode == 0x02:        # OUT
        output.append(chr(stack.pop()))

    elif opcode == 0x03:        # ADD
        a = stack.pop()
        b = stack.pop()
        stack.append((a + b) & 0xff)

    elif opcode == 0x04:        # XOR
        a = stack.pop()
        b = stack.pop()
        stack.append(a ^ b)

    else:
        raise ValueError(f"Unknown opcode: {opcode:02x}")

print("".join(output))