#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-29 17:41:47
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def num_moves(Sx: int, Sy: int, Ex: int, Ey: int, count = 0):
        if Sx != Ex and Sy != Ey:
            return count + 1
        
        if Sx == Ex:
            if Sx + 1 <= 10:
                return num_moves(Sx + 1, Sy, Ex, Ey, count + 1)
            else:
                return num_moves(Sx - 1, Sy, Ex, Ey, count + 1)
        
        if Sy == Ey:
            if Sy + 1 <= 10:
                return num_moves(Sx, Sy + 1, Ex, Ey, count + 1)
            else:
                return num_moves(Sx, Sy - 1, Ex, Ey, count + 1)

    T = int(input())
    for i in range(T):
        Sx, Sy, Ex, Ey = [*map(int, input().split())]
        print(num_moves(Sx, Sy, Ex, Ey))


if __name__ == "__main__":
    solve()

