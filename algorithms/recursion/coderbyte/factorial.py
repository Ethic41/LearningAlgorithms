#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-25 07:47:15
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    print(factorial(int(input("n: "))))


def factorial(n):
    """ principle:
    factorial(5) = 5 * 4 * 3 * 2 * 1
    factorial(4) = 4 * 3 * 2 * 1
    factorial(3) = 3 * 2 * 1
    factorial(2) = 2 * 1
    factorial(1) = 1

    therefore for we can define factorial(5) as
    factorial(5) = 5 * factorial(4), this follows that
    factorial(n) = n * factorial(n - 1) 
    """
    if n == 1: return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    solve()


