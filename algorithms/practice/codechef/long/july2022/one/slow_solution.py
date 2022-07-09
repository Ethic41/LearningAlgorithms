#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-09 00:10:31
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : https://www.codechef.com/JULY221D/problems/SLOWSOLN
# @Version : 1.0.0


def solve():
    def get_slowest_iteration(maxT: int, maxN: int, sumN: int):
        test_cases = []
        
        count = sumN // maxN
        remainder = sumN % maxN
        
        for _ in range(count):
            if len(test_cases) < maxT:
                test_cases.append(maxN)
            else:
                break
        
        if len(test_cases) < maxT:
            test_cases.append(remainder)
        
        return sum(map(lambda x: x*x, test_cases))


    T = int(input())

    for _ in range(T):
        maxT, maxN, sumN = [*map(int, input().split())]
        print(get_slowest_iteration(maxT, maxN, sumN))


if __name__ == "__main__":
    solve()

