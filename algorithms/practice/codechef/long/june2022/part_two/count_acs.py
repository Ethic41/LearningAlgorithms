#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-24 18:03:28
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def count_acs(score: int, count: int = 0):
        count = count

        if count > 10: return -1
        if score == 0: return count

        if score >= 100:
            return count_acs(score % 100, count + score // 100)
        
        return count_acs(0, count + score // 1)


    T = int(input())

    for i in range(T):
        P = int(input())
        print(count_acs(P))


if __name__ == "__main__":
    solve()

