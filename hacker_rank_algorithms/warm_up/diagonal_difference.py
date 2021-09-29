#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-07-12 07:13:14
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    n = int(input())
    arrays = []

    for i in range(n):
        ith_array = list(map(int, input().split()))
        arrays.append(ith_array)
    
    print(absolute_difference(n, arrays))


def absolute_difference(n, arrays):
    l_counter = 0
    r_counter = -1
    left_diag = 0
    right_diag = 0

    for array in arrays:
        left_diag += array[l_counter]
        right_diag += array[r_counter]
        l_counter += 1
        r_counter -= 1
    
    return abs(left_diag - right_diag)



if __name__ == "__main__":
    main()

