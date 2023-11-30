#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_elements_after_duplicate_pair(tup):
    if len(tup) < 2:
        return

    if tup[0] == tup[1]:
        print(tup[2:])
    else:
        print_elements_after_duplicate_pair(tup[1:])

if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 4, 5, 6, 7, 7, 8)
    print_elements_after_duplicate_pair(my_tuple)
