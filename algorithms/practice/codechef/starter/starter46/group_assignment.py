#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-06 15:48:31
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : https://www.codechef.com/START46D/problems/GRPASSN
# @Version : 1.0.0

from typing import Dict, List

def solve():
    def can_form_group(array_of_people: List[int], size: int):
        
        counter: Dict[int, int] = {}
        
        for person in array_of_people:
            if person not in counter:
                counter[person] = 1
            else:
                counter[person] += 1

        for person in counter:
            if counter[person] != person:
                return "NO"
        
        return "YES"


    T = int(input())
    for _ in range(T):
        N = int(input())
        P = [*map(int, input().split())]
        print(can_form_group(P, N))


if __name__ == "__main__":
    solve()

