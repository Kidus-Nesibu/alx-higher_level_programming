#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = ['+', '-', '*', '/']

    if sys.argv[2] not in operator:
        print("Unkown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    print("{} {} {}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

