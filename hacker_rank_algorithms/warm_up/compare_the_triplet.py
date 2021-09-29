#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-07-12 06:32:44
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    alice_list = list(map(int, input().split()))
    bob_list = list(map(int, input().split()))

    n = len(alice_list)

    alice_score = 0
    bob_score = 0

    for i in range(n):
        if alice_list[i] > bob_list[i]:
            alice_score += 1
        
        if alice_list[i] < bob_list[i]:
            bob_score += 1
    
    print(alice_score, bob_score)


if __name__ == "__main__":
    main()

