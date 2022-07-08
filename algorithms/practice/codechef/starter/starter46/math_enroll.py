#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-06 15:39:40
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : https://www.codechef.com/START46D/problems/M1ENROL
# @Version : 1.0.0


def solve():
    def get_seats(X: int, Y: int):
        if Y > X:
            return Y - X
        
        return 0

    T = int(input())

    for _ in range(T):
        X, Y = [*map(int, input().split())]
        print(get_seats(X, Y))


if __name__ == "__main__":
    solve()


