#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-11-23 16:45:52
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def battle(N, A, B, time=0):
        if N == 1:
            return time - B
        
        return battle(N // 2, A, B, time + A + B)
    
    T = int(input())

    for _ in range(T):
        N, A, B = [*map(int, input().split())]
        print(battle(N, A, B))


if __name__ == "__main__":
    solve()


