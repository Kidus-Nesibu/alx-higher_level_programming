#!/usr/bin/python3
import sys
num_arg = len(sys.argv)
args = sys.argv
i = 1

print("{} argument:".format(num_arg - 1))
while i < num_arg:
    print("{}: {}".format(i, args[i]))
    i += 1
if __name__ == "__main__":
    sys.print_arguments()
