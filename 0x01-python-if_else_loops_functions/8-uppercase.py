#!/usr/bin/python3
def uppercase(str):
    result = ""
    i = 0
    j = len(str)
    while i < j:
        if 'a' <= str[i] <= 'z':
            cap = ord(str[i]) - 32
            result += chr(cap)
        else:
            result += str[i]
        i += 1
    print(result)
