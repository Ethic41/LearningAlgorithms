# Author: Dahir Muhammad Dahir
# Date: 19-June-2019 8:19 PM
# About: a simple python linked list implementation
# a linked list is a data structure in which each
# node contain it's data and a reference or
# pointer to another node
# PS: this may not be the best implementation jst
# try to learn


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, new_node):
        head = self.head

        if head is None:
            head = new_node
        else:
            current_node = head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

        self.head = head

    def array_to_linked_list(self, array):
        len_array = len(array)

        for index in range(len_array):
            self.add_node(Node(array[index]))

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def has_next(self):  # TODO: remove this method if no significant use is found
        if self.next:
            return True
        else:
            return False
