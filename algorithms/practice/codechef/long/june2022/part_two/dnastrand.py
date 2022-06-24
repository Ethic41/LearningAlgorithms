#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-24 17:37:43
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


def solve():
    def complement_dna(dna_strand: str)-> str:
        complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}

        complementary_strand = ""

        for nucleotide in dna_strand:
            complementary_strand += complement_map[nucleotide]
        
        return complementary_strand

    T = int(input())

    for i in range(T):
        N = int(input())
        dna_strand = input()
        print(complement_dna(dna_strand))


if __name__ == "__main__":
    solve()


