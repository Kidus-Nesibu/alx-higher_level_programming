#!/usr/bin/python3
def safe_print_list_list(my_list=[], x=0):
    for i in my_list:
        try:
            print(i, end="")
            x -= 1
            if x == 0:
                break
        except Exception:
            pass
