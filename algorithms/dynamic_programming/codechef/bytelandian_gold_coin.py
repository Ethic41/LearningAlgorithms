#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-29 09:19:57
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def exchange_naive(n: int):
        if n <= 4: return n
        
        exchange = sum([exchange_naive(n // 2), exchange_naive(n // 3), exchange_naive(n // 4)])
        best = exchange if exchange > n else n
        return best
    

    def exchange_better(n: int, memo = {}):
        if n <= 4: return n
        if n in memo: return memo[n]

        exchange = sum([exchange_better(n // 2, memo), exchange_better(n // 3, memo), exchange_better(n // 4, memo)])
        best = exchange if exchange > n else n

        memo[n] = best
        return best


    while True:
        try:
            N = int(input())
            # print(exchange_naive(N))
            print(exchange_better(N, memo = {}))
        except EOFError:
            break
        except:
            break


if __name__ == "__main__":
    solve()

