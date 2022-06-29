#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-29 16:51:15
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def apps_to_delete_count(S: int, X: int, Y: int, Z: int):
        if X + Y + Z <= S:
            return 0
        
        if S - X < Z and S - Y < Z:
            return 2
        
        return 1

    T = int(input())
    for _ in range(T):
        S, X, Y, Z = [*map(int, input().split())]
        print(apps_to_delete_count(S, X, Y, Z))


if __name__ == "__main__":
    solve()

