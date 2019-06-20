# Author: Dahir Muhammad Dahir
# Date: 19-June-2019 8:29 PM
# About: this file is used to test the implementation of
# the various data structures found in this module


from linked_list import LinkedList, Node


def main():
    arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    linked_list1 = LinkedList()

    linked_list1.array_to_linked_list(arrays)

    linked_list1.print_list()


if __name__ == "__main__":
    main()
