#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-29 11:59:35
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : https://www.codechef.com/submit-v2/MIXTURES
# @Version : 1.0.0

from typing import List


def solve():
    def mix_naive(colors: List[int], pos: int = 0):
        if len(colors) == 1: return colors[0]
        if len(colors) == 2: return colors[0] * colors[1]

        first_part = colors[ : pos]
        last_part = colors[pos+2 : ]
        current_part = colors[pos : pos+2]

        mixture = (current_part[0] + current_part[1]) % 100
        smoke = current_part[0] * current_part[1]
        
        colors = first_part + [mixture] + last_part
        
        new_pos = len(first_part) + 1
        return smoke + mix_naive(colors, new_pos)
    

    def mix_better(colors: List[int], pos: int = 0):
        if len(colors) == 1: return colors[0]
        if len(colors) == 2: return colors[0] * colors[1]
        
        key = f"{colors[0]}_{colors[1]}"
        if key in memo: return memo[key]

        first_part = colors[ : pos]
        last_part = colors[pos+2 : ]
        current_part = colors[pos : pos+2]

        # print(f"first part: {first_part}")
        # print(f"last part: {last_part}")
        # print(f"current part: {current_part}")

        mixture = (current_part[0] + current_part[1]) % 100
        smoke = current_part[0] * current_part[1]
        
        colors = first_part + [mixture] + last_part
        
        new_pos = len(first_part)
        memo[key] = smoke + mix_better(colors, new_pos)
        return memo[key]


    while True:
        try:
            T = int(input())
            case = [*map(int, input().split())]
            colors = case
            smokes = []
            memo = {}
            for i in range(T - 1):
                # smokes.append(mix_naive(colors, i))
                smokes.append(mix_better(colors, i))
            print(min(smokes))
        except EOFError:
            break
        except:
            break


if __name__ == "__main__":
    solve()

