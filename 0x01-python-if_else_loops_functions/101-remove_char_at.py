#!/usr/bin/python3i
def remove_char_at(str, n):
    tmp = ""
    length = len(str)
    i = 0
    while i < length:
        if i != n:
            tmp += str[i]
        i += 1
    return tmp
