# Author: Dahir Muhammad Dahir
# Date: 6/22/2020
# About: Base class for a node


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
