#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-24 17:27:00
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def fitness(x: int):
        return x * 2 * 5
    
    T = int(input())

    for _ in range(T):
        X = int(input())
        print(fitness(X))


if __name__ == "__main__":
    solve()

