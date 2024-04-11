#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
i = 0
names = dir(hidden_4)
while i < len(names):
    if names[i][:2] != '__':
        print("{}".format(names[i]))
    i += 1
