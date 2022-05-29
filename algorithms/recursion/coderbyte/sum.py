#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-25 09:11:32
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

from typing import List

def solve():
    print(naive_sum([*map(int, input().split())]))
    print(better_sum([*map(int, input().split())]))


def naive_sum(list: List[int]):
    """ principle:
    sum([]) = 0
    sum([1]) = 1
    sum([1, 2]) = 3
    sum([1, 2, 3]) = 6, this follows that:
    
    sum([]) = 0 
    sum([i]) = i
    sum([i1, i2]) = i + sum([i2])
    sum([i1, i2, i3]) = i + sum(i2, i3) """

    if list == []: return 0
    return list[0] + naive_sum(list[1:])


def better_sum(list: List[int]):
    def sum(list, index: int = 0):
        if index == len(list): return 0
        
        return list[index] + sum(list, index+1)

    return sum(list)


if __name__ == "__main__":
    solve()

