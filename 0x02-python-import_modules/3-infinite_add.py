#!/usr/bin/python3
if __name__ == "__main__":
    import sys
length = len(sys.argv) - 1
i = 1
args = 0
while i <= length:
    args += int(sys.argv[i])
    i += 1
print("{}".format(args))
