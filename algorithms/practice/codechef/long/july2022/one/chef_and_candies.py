#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-08 10:45:00
# @Author  : Dahir Muhammad Dahir
# @Link : https://www.codechef.com/JULY221D/problems/CHEFCAND


def solve():
    def candies_to_buy(N: int, X: int):
        if X >= N:
            return 0
        
        deficit = N - X
        if deficit % 4: return (deficit // 4) + 1
        return deficit // 4


    T = int(input())
    for i in range(T):
        N, X = [*map(int, input().split())]
        print(candies_to_buy(N, X))


if __name__ == "__main__":
    solve()
