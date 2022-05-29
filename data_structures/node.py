#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-11-29 05:58:10
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


class Node:
    def __init__(self, info) -> None:
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self) -> str:
        return self.info

