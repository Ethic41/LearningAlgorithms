# Author: Dahir Muhammad Dahir
# Date: 04-July-2019 10:14 PM
# About: Binary Tree is a non-linear, finite,
# connected, undirected graph with vertex
# or node of degree !> 3, data structure.
# this is my first implementation of a
# binary tree, note that due to it's varying
# nature, this is not the only possible implementation


class BinaryTree:
    def __init__(self):
        self.root = None
        # self.last = None  TODO: implementing last is not practical

    def add_node(self, node):
        """Add node to the first found leaf"""
        current_node = self.root

        if current_node is None:
            self.root = node
            return

        if current_node.left is None:
            current_node.left = node
            current_node.left.parent = current_node
            return

        if current_node.right is None:
            current_node.right = node

    def find_leaf(self):
        pass

    def get_size_dft(self):
        current_node = self.root
        previous_node = None

        node_count = 0

        while current_node is not None:
            if previous_node == current_node.parent:
                node_count += 1
                if current_node.left is not None:
                    next_node = current_node.left

                elif current_node.right is not None:
                    next_node = current_node.right

                else:
                    next_node = current_node.parent

            elif previous_node == current_node.left:
                if current_node.right is not None:
                    next_node = current_node.right

                else:
                    next_node = current_node.parent

            else:
                next_node = current_node.parent

            previous_node = current_node
            current_node = next_node

        return node_count

    def depth_first_traverse(self):
        current_node = self.root
        previous_node = None

        while current_node is not None:
            if previous_node == current_node.parent:
                if current_node.left is not None:
                    next_node = current_node.left
                elif current_node.right is not None:
                    next_node = current_node.right
                else:
                    next_node = current_node.parent

            elif previous_node == current_node.left:
                if current_node.right is not None:
                    next_node = current_node.right
                else:
                    next_node = current_node.parent

            else:
                next_node = current_node.parent

            previous_node = current_node
            current_node = next_node

    def breadth_first_traverse(self):
        pass

    def add_internal_node(self, internal_node, node):
        pass


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
