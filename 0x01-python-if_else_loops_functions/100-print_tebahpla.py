#!/usr/bin/python3
a = 'z'

while ord('a') <= ord(a):
    print(a)
    a = chr(ord(a)-1)
