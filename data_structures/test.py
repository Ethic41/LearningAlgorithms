# Author: Dahir Muhammad Dahir
# Date: 19-June-2019 8:29 PM
# About: this file is used to test the implementation of
# the various data structures found in this module


from binary_search_tree import BinarySearchTree
from node import Node
from random import choice


def main():
    tree = BinarySearchTree()
    for i in range(1, 128):
        i = choice(list(range(1, 3000)))
        print("{} ".format(i), end="")
        tree.add_node(Node(i))

    print()

    tree.print_tree()


if __name__ == "__main__":
    main()
