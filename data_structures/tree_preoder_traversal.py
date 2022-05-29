#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-11-29 05:04:07
# @Author  : Dahir Muhammad Dahir
# @Description : something cool

from typing import List, Optional
from node import Node


def pre_order_recursive(root: Optional[Node]):
    if root:
        print(root.info, end=' ')

        if root.left:
            pre_order_recursive(root.left)
        if root.right:
            pre_order_recursive(root.right)


def pre_order_iterative(root: Optional[Node]):
    to_visit: List[Optional[Node]] = [root]
    while to_visit:
        node = to_visit.pop()
        if node:
            print(node.info, end=' ')
            if node.right:
                to_visit.append(node.right)
            if node.left:
                to_visit.append(node.left)

