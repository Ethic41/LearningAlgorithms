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
        self.last = None

    def push_node(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def add_node(self, new_node):
        if self.last is None:
            self.head = new_node
            self.last = self.head

        else:
            self.last.next = new_node
            self.last = self.last.next

    def pop_node(self):
        node_to_pop = self.head
        self.head = self.head.next
        return node_to_pop

    def length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            if current_node.data is not None:
                count += 1
            current_node = current_node.next

        return count

    def delete_node(self, key):
        current_node = self.head
        previous_node = None

        if current_node is not None and (current_node.data == key):
            self.head = current_node.next
        else:
            while (current_node is not None) and (current_node.data != key):
                previous_node = current_node
                current_node = current_node.next

            if (previous_node is not None) and (current_node is not None):
                previous_node.next = current_node.next

    def delete_node_at_position(self, pos):
        index = 1
        current_node = self.head
        if pos == 0 and (current_node is not None):
            self.head = self.head.next
        else:
            while (index < pos) and (current_node is not None):
                current_node = current_node.next
                index += 1

            if (current_node is not None) and (current_node.next is not None):
                current_node.next = current_node.next.next

    def delete(self):
        current_node = self.head

        while current_node is not None:
            next_node = None
            if current_node.next is not None:
                next_node = current_node.next
                current_node.next = None

            del current_node.data
            current_node = next_node

    def search(self, key):
        current_node = self.head

        while current_node is not None:
            if current_node.data == key:
                return True

            if current_node.next is None:
                return False

            current_node = current_node.next

    def get_node(self, pos):
        current_node = self.head
        count = 0

        while current_node is not None:
            if count == pos:
                if current_node.data is not None:
                    return current_node.data

            current_node = current_node.next
            count += 1

        return None

    def get_node_from_end(self, pos):
        len_list = self.length()  # getting the length of linked list
        real_index = len_list - pos  # this is the position of the node counting from ltr, zero indexed
        return self.get_node(real_index)   # we can just obtain the node with real index

    def get_middle_element(self):
        len_list = self.length()
        middle_index = int(len_list / 2)
        if middle_index == 0:
            return None
        else:
            return self.get_node(middle_index)

    def count(self, item):
        item_count = 0
        current_node = self.head

        while current_node is not None:
            if current_node.data == item:
                item_count += 1

            current_node = current_node.next

        return item_count

    def has_loop(self):
        current_node = self.head
        traversed = []

        while current_node is not None:
            if current_node.next is None:
                return False

            if current_node.next in traversed:
                return True

            traversed.append(current_node.next)
            current_node = current_node.next

        return False

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
