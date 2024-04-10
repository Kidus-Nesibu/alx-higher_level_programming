#!/usr/bin/python3
if __name__ == "__main__":
    import sys
num_arg = len(sys.argv)
args = sys.argv
i = 1
if num_arg - 1 == 0:
    print("{} arguments.".format(num_arg - 1))
elif num_arg - 1 == 1:
    print("{} argument:".format(i))
else:
    print("{} arguments:".format(num_arg - 1))
while i < num_arg:
    print("{}: {}".format(i, args[i]))
    i += 1
