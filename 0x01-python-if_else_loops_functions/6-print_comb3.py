#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i != j and j > i:
            print(i, end="")
            if j == 9 and i == 8:
                print(j)
            else:
                print(j, end=", ")
            j += 1
i += 1
