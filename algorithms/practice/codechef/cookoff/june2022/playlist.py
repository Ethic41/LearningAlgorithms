#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-05 17:57:19
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def playlist(N, X):
        return N // (X * 3)


    T = int(input())
    for _ in range(T):
        N, X = [*map(int, input().split())]
        print(playlist(N, X))


if __name__ == "__main__":
    solve()

