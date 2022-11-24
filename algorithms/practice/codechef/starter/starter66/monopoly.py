#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-11-23 16:27:28
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    T = int(input())

    for _ in range(T):
        R1, R2, R3 = [*map(int, input().split())]
        if R1 > sum([R2, R3]) or R2 > sum([R1, R3]) or R3 > sum([R1, R2]):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()


