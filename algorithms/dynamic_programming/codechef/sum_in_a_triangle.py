#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-24 13:20:55
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

from typing import List

def solve():
    def largest_sum_better(size: int, x: int = 0, y: int = 0, memo = {}):
        if x > size - 1: return 0
        
        key = f"{x}-{y}"
        if key in memo: return memo[key]
        
        path_sum = case[x][y] + max(largest_sum_better(size, x=x+1, y=y, memo=memo), largest_sum_better(size, x=x+1, y=y+1, memo=memo))
        
        memo[key] = path_sum
        return path_sum
    

    def largest_sum_naive(case: List[List[int]], size: int, x: int = 0, y: int = 0):
        if x > size - 1: return 0
        return case[x][y] + max(largest_sum_naive(case, size, x=x+1, y=y), largest_sum_naive(case, size, x=x+1, y=y+1))
    

    T = int(input())
    
    for _ in range(T):
        N = int(input())

        case: List[List[int]] = []
        
        for i in range(N):
            line = [*map(int, input().split())]
            case.append(line)
        
        print(largest_sum_better(N, x=0, y=0, memo={}))


if __name__ == "__main__":
    solve()

