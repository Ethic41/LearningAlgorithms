#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-09-29 07:24:42
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    n = int(input())
    candles = list(map(int, input().split()))
    print(candles.count(max(candles)))


if __name__ == "__main__":
    main()

