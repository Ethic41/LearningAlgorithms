#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-13 02:17:36
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def solve():
    def altadd(A, B):
        if A + 1 == B:
            return "YES"
        
        diff = B - A
        is_odd = diff % 2 == 1
        if not is_odd:
            num_past = (2 * diff // 2) + (1 * diff // 2)
        else:
            num_past = (2 * diff // 2) + (1 * diff // 2) + 1
        
        target = B
        for index, num in enumerate(range(B, num_past)):
            if index + 1 % 2 == 0:
                target += 2
            else:
                target += 1
            if target == num_past:
                return "YES"
        
        return "NO"



    T = int(input())
    for _ in range(T):
        A, B = [*map(int, input().split())] # type: ignore
        print(altadd(A, B))


if __name__ == "__main__":
    solve()

