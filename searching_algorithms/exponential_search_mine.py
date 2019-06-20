# Author: Dahir Muhammad Dahir
# Date: 18-June-2019 11:49 PM
# About: Invented by Jon Bentley and Andrew Chi-Chih Yao,
# although this algorithm is called exponential
# search the complexity is actually O ( log(i) )
# this algorithms works by taking an index interval of
# 2^i (0 <= i <= inf), until we reach interval where
# target element is less than 2^i, we then perform binary
# search on then interval 2^i-1 to 2^i, this algorithm is
# useful for unbounded or infinite array, but can be used
# for bounded array as well
# PS: this implementation assumes array is infinite or
# unbounded

from binary_search_mine import binary_search


def main():
    sorted_array = list(map(int, input().strip().split(",")))
    item = int(input())

    print(exponential_search(sorted_array, item))


def exponential_search(sorted_array, item):
    index = 0

    while item > sorted_array[2 ** index]:
        index += 1

    if item == sorted_array[2 ** index]:
        return 2 ** index

    else:
        target_subarray = sorted_array[2 ** (index - 1): 2 ** index]
        result = binary_search(target_subarray, item)

        if result == -1:
            return -1
        else:
            return 2 ** (index - 1) + result


if __name__ == "__main__":
    main()
