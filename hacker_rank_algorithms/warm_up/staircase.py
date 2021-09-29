#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 06:38:55
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    n = int(input())
    case = "#"

    for i in range(1, n+1):
        space = (n - i) * " "
        cases = case * i
        print(f"{space}{cases}")


if __name__ == "__main__":
    main()

