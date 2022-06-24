#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-13 01:50:18
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def solve():
    def subscribe(N, X):
        rem = 0 if N % 6 == 0 else 1
        count = N // 6 + rem
        return count * X


    T = int(input())
    for _ in range(T):
        N, X = [*map(int, input().split())] # type: ignore
        print(subscribe(N, X))


if __name__ == "__main__":
    solve()

