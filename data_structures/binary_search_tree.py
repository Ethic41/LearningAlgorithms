# Author: Dahir Muhammad Dahir
# Date: 13-July-2019 8:44 AM
# About: Binary Search Tree is a special kind
# of binary tree in which each node u, store
# an additional data u.x, the binary search
# tree obeys the binary search tree property
# that is for a given node u, u.left.x < u.x
# and u.right.x > u.x
from collections import deque
from tree import Tree


class BinarySearchTree(Tree):
    def __init__(self):
        super().__init__()

    def breadth_first_traverse(self):
        que = deque([self.root])

        while len(que) > 0:
            current_node = que.popleft()
            if current_node.left is not None:
                que.append(current_node.left)
            elif current_node.right is not None:
                que.append(current_node.right)

    def find_leaf_bfs(self):
        que = deque()
        current_node = self.root
        if current_node is not None:
            que.append(current_node)

        while len(que) > 0:
            current_node = que.popleft()
            if current_node.left is None:
                return current_node
            else:
                que.append(current_node.left)

            if current_node.right is None:
                return current_node
            else:
                que.append(current_node.right)

        return current_node

    def add_node_bf(self, node):
        if self.root is None:
            self.root = node
            return

        current_node = self.find_leaf_bfs()
        if current_node.left is None:
            current_node.left = node
            current_node.left.parent = current_node
            return

        if current_node.right is None:
            current_node.right = node
            current_node.right.parent = current_node
            return

    def add_node(self, node):
        """the addition is based on the binary search tree
        property, to add a value x to the binary tree
        node u, if u.value < x; add to u.left else if u.value
        > x; add to u.right; if equal no need to add"""
        value = node.data
        current_node = self.find_last(value)

        if current_node is None:
            self.root = node
            return

        elif value == current_node.data:
            return

        if value < current_node.data:
            current_node.left = node
            current_node.left.parent = current_node

        if value > current_node.data:
            current_node.right = node
            current_node.right.parent = current_node

    def find_last(self, value):
        current_node = self.root
        last_node = None

        while current_node is not None:
            if current_node.data == value:
                return current_node

            elif value < current_node.data:
                last_node = current_node
                current_node = current_node.left

            else:
                last_node = current_node
                current_node = current_node.right

        return last_node

    def find(self, value):
        current_node = self.root

        while current_node is not None:
            if value == current_node.data:
                return current_node

            elif value < current_node.data:
                current_node = current_node.left

            else:
                current_node = current_node.right
        return None

    def find_geq(self, value):
        current_node = self.root
        smallest_greater_node = None

        while current_node is not None:
            if value == current_node.data:
                return current_node
            elif value < current_node.data:
                smallest_greater_node = current_node
                current_node = current_node.left
            else:
                current_node = current_node.right

        return smallest_greater_node

    def print_tree(self):
        que = deque()
        power = 0
        count = 0

        if self.root is not None:
            que.append(self.root)

        while len(que) > 0:
            while count < 2 ** power:
                if len(que) < 1:
                    break
                current_node = que.popleft()
                print("{} ".format(current_node.data), end="")

                if current_node.left is not None:
                    que.append(current_node.left)

                if current_node.right is not None:
                    que.append(current_node.right)

                count += 1
            power += 1
            count = 0
            print()
