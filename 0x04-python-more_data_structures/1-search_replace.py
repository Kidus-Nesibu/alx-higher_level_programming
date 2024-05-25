#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy_list = []
    for item in my_list:
        if search in my_list and search is item:
            cpy_list.append(replace)
        else:
            cpy_list.append(item)
    return cpy_list
