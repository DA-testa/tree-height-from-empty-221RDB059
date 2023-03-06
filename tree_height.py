# python3

import sys
import threading
import numpy
import os


def compute_height(n: int, parents: list, root=-1):
    # Write this function

    # Your code here
    children = {i: [] for i in range(n)}
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    max_height = 1
    queue = [root]
    while queue:
        next_level = []
        for node in queue:
            next_level += children[node]
        if next_level:
            max_height += 1
        queue = next_level

    return max_height


def main():
    # implement input form keyboard and from files
    test_type = input().lower()
    if test_type.find("f") != -1:
        file_name = input()
        with open(f"test/{file_name}") as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split(" ")))
            print(compute_height(n, parents))
    elif test_type.find("i") != -1:
        n = int(input())
        parents = list(map(int, input().split(" ")))
        print(compute_height(n, parents))
    else:
        print("bruh")

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
