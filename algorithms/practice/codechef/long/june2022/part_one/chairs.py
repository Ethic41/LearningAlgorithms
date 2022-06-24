#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-13 01:37:04
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def solve():
    def chairs(X, Y):
        if Y >= X:
            return 0
        
        return X - Y
    

    T = int(input())
    for _ in range(T):
        X, Y = [*map(int, input().split())] # type: ignore
        print(chairs(X, Y))
    

if __name__ == "__main__":
    solve()

