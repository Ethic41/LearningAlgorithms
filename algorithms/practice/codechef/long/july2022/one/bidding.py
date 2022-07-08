#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-08 10:22:00
# @Author  : Dahir Muhammad Dahir
# @Link : https://www.codechef.com/JULY221D/problems/AUCTION


def solve():
    def bid(alice: int, bob: int, charlie: int):
        winner = max(alice, bob, charlie)
        if winner == alice:
            return "ALICE"
        if winner == bob:
            return "BOB"
        return "CHARLIE"
    
    T = int(input())
    for i in range(T):
        alice, bob, charlie = [*map(int, input().split())]
        print(bid(alice, bob, charlie))


if __name__ == "__main__":
    solve()
