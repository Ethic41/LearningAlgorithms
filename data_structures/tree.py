# Author: Dahir Muhammad Dahir
# Date: 6/22/2020
# About: Base class for most trees


from collections import deque


class Tree:
    def __init__(self):
        self.root = None
        # self.last = None  TODO: implementing last is not practical

    def bf_print_tree(self):
        que = deque()

        if self.root is not None:
            que.append(self.root)

        while len(que) > 0:
            current_node = que.popleft()
            print("{}=>".format(current_node.data), end="")

            if current_node.left is not None:
                que.append(current_node.left)

            if current_node.right is not None:
                que.append(current_node.right)
        print(None)

    def depth_first_traverse(self):
        current_node = self.root
        previous_node = None

        while current_node is not None:
            if previous_node == current_node.parent:
                # this means we are in a new node
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
