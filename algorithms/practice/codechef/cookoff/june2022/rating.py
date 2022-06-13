#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-05 17:45:20
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def rating(x, y):
        if y < x:
            print("NO")
            return
        
        if y > x + 200:
            print("NO")
            return
        
        print("YES")


    T = int(input())
    for _ in range(T):
        x, y = [*map(int, input().split())]
        rating(x, y)



if __name__ == "__main__":
    solve()


