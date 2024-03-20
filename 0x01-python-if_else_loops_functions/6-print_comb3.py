#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i != j and j > i:
            print("{}".format(i), end="")
            if j == 9 and i == 8:
                print("{}".format(j))
            else:
                print("{}".format(j), end=", ")
            j += 1
i += 1
