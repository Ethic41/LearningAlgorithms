#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-08 10:35:00
# @Author  : Dahir Muhammad Dahir
# @Link : https://www.codechef.com/JULY221D/problems/PASSTHEEXAM


def solve():
    def is_exam_passed(A: int, B: int, C: int):
        if sum([A,B,C]) >= 100 and min(A, B, C) >= 10:
            return "PASS"
        return "FAIL"
    

    T = int(input())
    for i in range(T):
        A, B, C = [*map(int, input().split())]
        print(is_exam_passed(A, B, C))


if __name__ == "__main__":
    solve()
