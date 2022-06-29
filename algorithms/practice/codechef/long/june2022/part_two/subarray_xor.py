#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-25 09:45:15
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

""" 
the subarray of the array [1,2,3,4] 
[1], [1,2], [1,2,3], [1,2,3,4], [2], [2,3],
[2,3,4], [3], [3,4], [4]
"""

def solve():
    def gen_subarrays(array: list):
        subarrays = []
        for i, _ in enumerate(array):
            for j, _ in enumerate(array[i:]):
                subarrays.append(array[i:j+i+1])
    
        return subarrays
    
    def subarray_xor(array: list, K: int):
        subarrays = gen_subarrays(array)
        good_subarrays = []

        for subarray in subarrays:
            pass


if __name__ == "__main__":
    solve()

