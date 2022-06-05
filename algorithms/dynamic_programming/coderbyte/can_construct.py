#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-05 10:31:12
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

""" 
    Problem Statement:
    Given a target string and a wordbank, 
    determine if you can construct the target string from the wordbank. 
    The wordbank will be an array of strings.
"""

def solve():
    def can_construct_naive(target_string: str):
        if target_string == "": return True

        for word in wordbank:
            if target_string.startswith(word):
                if can_construct_naive(target_string[len(word):]):
                    return True
        
        return False
    

    def can_construct_better(target_string: str, memo = {}):
        if target_string == "": return True
        if target_string in memo: return memo[target_string]

        for word in wordbank:
            if target_string.startswith(word):
                if can_construct_better(target_string[len(word):], memo):
                    memo[target_string] = True
                    return True
        
        memo[target_string] = False
        return False


    while True:
        try:
            target_string = input()
            wordbank = input().split()
            # print(can_construct_naive(target_string))
            print(can_construct_better(target_string, memo = {}))
        except EOFError:
            break
        except:
            break


if __name__ == "__main__":
    solve()

