#!/usr/bin/python3
a = 'z'
i = 1
while ord('a') <= ord(a):
    if i % 2 == 0:
        print("{}".format(a).upper(), end="")
    else:
        print("{}".format(a), end="")
    a = chr(ord(a)-1)
    i += 1
