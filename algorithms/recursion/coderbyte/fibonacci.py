#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-25 10:04:02
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    print(fib(int(input("n: "))))


def fib(n: int):
    """ principle:
    the first two numbers of fibonacci sequence are 1 and 1,
    the next number of the sequence can be calculated by
    taking the sum of the previous two. this follows that, 
    fib(1) = 1
    fib(2) = 1
    fib(3) = 2
    fib(4) = 3
    fib(5) = 5, this follows that
    fib(n) = fib(n-1) + fib(n-2) """

    if n <= 2: return 1   # guarding against 0 and negative people
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    solve()


