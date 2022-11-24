#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-11-23 17:19:26
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def is_mob_day(N: int, M: int, K: int, X: int):
        current_day = 0
        current_year = 0
        is_mob = False

        while current_day < X:
            if current_year % K == 0:
                current_day += N + M
                current_year += 1
                is_mob = True
            else:
                current_day += N
                current_year += 1
                is_mob = False
        
        if current_day == X:
            return "YES" if is_mob else "NO"
        
        if current_day > X:
            diff = current_day - X
            if diff <= M:
                return "NO" if is_mob else "YES"
            else:
                return "NO"

    T = int(input())

    for _ in range(T):
        N, M, K, X = [*map(int, input().split())]
        print(is_mob_day(N, M, K, X))



if __name__ == "__main__":
    solve()


