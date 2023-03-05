# python3

import sys
import threading
import numpy
import os


def compute_height(n: int, parents: list):
    # Write this function
    max_height = 2
    # Your code here
    parents.sort()

    i = 0
    nodes_available_after = 0
    nodes_available = 1
    last_num = 0  # The first number after sort should always be -1
    while i < n:
        curr_num = parents[i]
        if last_num == curr_num:
            nodes_available_after += 1
        elif nodes_available > 0:
            nodes_available_after += 1
            nodes_available -= 1

        else:
            nodes_available = nodes_available_after
            nodes_available_after = 0
            max_height += 1
        last_num = parents[i]
        i += 1
    return max_height


def main():
    # implement input form keyboard and from files
    test_type = input().lower()
    if test_type.find("f") != -1:
        file_name = input()
        with open(f"tests\{file_name}") as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split(" ")))
            print(compute_height(n, parents))
    else:
        n = int(input())
        parents = list(map(int, input().split(" ")))
        print(compute_height(n, parents))

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
