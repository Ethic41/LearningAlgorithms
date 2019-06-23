# Author: Dahir Muhammad Dahir
# Date: 19-June-2019 8:29 PM
# About: this file is used to test the implementation of
# the various data structures found in this module


from linked_list import LinkedList, Node


def main():
    arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 1]
    linked_list1 = LinkedList()
    a = Node(15)
    b = Node(16)
    c = Node(17)

    a.next = b
    b.next = c
    c.next = a
    linked_list1.add_node(a)
    linked_list1.add_node(b)
    linked_list1.add_node(c)
    print(linked_list1.has_loop())

    # linked_list1.array_to_linked_list(arrays)
    # print(linked_list1.has_loop())
    linked_list1.print_list()


if __name__ == "__main__":
    main()
