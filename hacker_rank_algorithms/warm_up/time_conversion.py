#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-09-29 07:50:52
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


def main():
    t = input()
    if t.endswith("AM"):
        if t[:2] == "12":
            print("00" + t[2:-2])
        else:
            print(t[:-2])
    
    if t.endswith("PM"):
        if t[:2] == "12":
            print(t[:-2])
        else:
            print(str(int(t[:2]) + 12) + t[2:-2])


if __name__ == "__main__":
    main()

