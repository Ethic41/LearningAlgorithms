#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-10 19:47:05
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : https://www.codechef.com/JULY221D/problems/LARSQR31
# @Version : 1.0.0


def solve():
    def get_green_square(N: int, garden: list, size: int, start: tuple = (0,0)):
        while True:
            current_x, current_y = start
            row = garden[current_x]
            



    def get_largest_square(N: int):
        garden = []
        for _ in range(N):
            case = [*map(int, input().split())]
            garden.append(case)
            


    while True:
        try:
            N = int(input())
            print(get_largest_square(N))
        except:
            break


if __name__ == "__main__":
    solve()

