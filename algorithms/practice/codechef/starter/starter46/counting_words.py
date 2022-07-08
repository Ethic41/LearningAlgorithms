#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-06 15:32:35
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : https://www.codechef.com/START46D/problems/CNTWRD
# @Version : 1.0.0


def solve():
    def count_words(N: int, M: int):
        return N * M

    T = int(input())

    for _ in range(T):
        N, M = [*map(int, input().split())]
        print(count_words(N, M))


if __name__ == "__main__":
    solve()

