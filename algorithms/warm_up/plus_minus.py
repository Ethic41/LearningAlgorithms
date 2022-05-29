#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 06:28:40
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    n = int(input())

    array = list(map(int, input().split()))

    positives = 0
    negatives = 0
    zeroes = 0

    for item in array:
        if item > 0:
            positives += 1
        
        if item < 0:
            negatives += 1
        
        if item == 0:
            zeroes += 1
    
    print(f"{positives/n : .6f}")
    print(f"{negatives/n : .6f}")
    print(f"{zeroes/n : .6f}")


if __name__ == "__main__":
    main()

