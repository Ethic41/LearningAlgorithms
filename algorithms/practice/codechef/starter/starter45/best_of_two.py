#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-29 16:40:59
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def best_of_two(X: int, Y: int):
        return max(X, Y)
    
    T = int(input())

    for _ in range(T):
        X, Y = [*map(int, input().split())]
        print(best_of_two(X, Y))


if __name__ == "__main__":
    solve()

    