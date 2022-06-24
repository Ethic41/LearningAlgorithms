#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-24 19:27:06
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

from collections import Counter

def solve():
    def make_equal(num_array: list):
        counter = Counter(num_array)
        mode = counter.most_common()[0][0]

        operations = 0
        for element in num_array:
            if element != mode:
                operations += 1
        
        return operations

    T = int(input())

    for i in range(T):
        N = int(input())
        num_array = [*map(int, input().split())]
        print(make_equal(num_array))


if __name__ == "__main__":
    solve()

