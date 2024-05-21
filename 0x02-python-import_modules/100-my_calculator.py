#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = ['+', '-', '*', '/']

    if sys.argv[2] not in operator:
        print("Unknown operator. Only: +, -, * and / available")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            print("Error: Division by Zero")
            sys.exit(1)
        else:
            result = a // b

    print("{} {} {} = {}".format(a, op, b, result))
