#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-07-14 07:39:21
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    array = sorted(list(map(int, input().split())))

    min = sum(array[:-1])
    max = sum(array[1:])

    print(f"{min} {max}")


if __name__ == "__main__":
    main()

