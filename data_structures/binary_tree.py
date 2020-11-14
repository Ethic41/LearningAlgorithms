# Author: Dahir Muhammad Dahir
# Date: 04-July-2019 10:14 PM
# About: Binary Tree is a non-linear, finite,
# connected, undirected graph with vertex
# or node of degree !> 3, data structure.
# this is my first implementation of a
# binary tree, note that due to it's varying
# nature, this is not the only possible implementation
from collections import deque
from tree import Tree


class BinaryTree(Tree):
    def __init__(self):
        super().__init__()

    def add_node(self, node):
        """Add node to the first found leaf"""
        if self.root is None:
            current_node = self.root
        else:
            current_node = self.find_leaf()

        if current_node is None:
            self.root = node

        elif current_node.left is None:
            current_node.left = node
            current_node.left.parent = current_node

        elif current_node.right is None:
            current_node.right = node
            current_node.right.parent = current_node

    def find_leaf(self):
        que = deque()
        que.append(self.root)
        current_node = None

        while len(que) > 0:
            current_node = que.popleft()
            if current_node.left is not None:
                que.append(current_node.left)
            else:
                return current_node

            if current_node.right is not None:
                que.append(current_node.right)
            else:
                return current_node

        return current_node

    def get_size_dft(self):
        current_node = self.root
        previous_node = None

        node_count = 0

        while current_node is not None:
            if previous_node == current_node.parent:  # we are at a new node
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

    def breadth_first_traverse(self):
        que = deque()

        if self.root is not None:
            que.append(self.root)

        while len(que) > 0:
            current_node = que.popleft()
            if current_node.left is not None:
                que.append(current_node.left)
            if current_node.right is not None:
                que.append(current_node.right)

    def add_internal_node(self, internal_node, node):
        pass

    def print_tree_dfs(self):
        current_node = self.root
        previous_node = None

        while current_node is not None:
            if previous_node == current_node.parent:
                print("{}=>".format(current_node.data), end="")
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
        print(None)
