# Author: Dahir Muhammad Dahir
# Date: 19-June-2019 1:09 AM
# About: Invented by Jon Bentley and Andrew Chi-Chih Yao,
# although this algorithm is called exponential
# search the complexity is actually O ( log(i) )
# this algorithms works by taking an index interval of
# 2^i (0 <= i <= inf), until we reach interval where
# target element is less than 2^i, we then perform binary
# search on then interval 2^i-1 to 2^i, this algorithm is
# useful for unbounded or infinite array, but can be used
# for bounded array as well
# PS: this implementation is for bounded or finite array

from binary_search_mine import binary_search # type: ignore


def main():
    sorted_array = list(map(int, input().strip().split(",")))
    item = int(input())

    print(exponential_search(sorted_array, item))


def exponential_search(sorted_array, item):
    index = 0

    len_array = len(sorted_array) - 1

    while (2 ** index < len_array) and (item > sorted_array[2 ** index]):
        index += 1

    if (2 ** index < len_array) and item == sorted_array[2 ** index]:
        return 2 ** index

    else:
        if 2 ** index < len_array:
            target_subarray = sorted_array[2 ** (index - 1): 2 ** index]
        else:
            target_subarray = sorted_array[2 ** (index - 1):]

        result = binary_search(target_subarray, item)

        if result == -1:
            return -1
        else:
            return 2 ** (index - 1) + result


if __name__ == "__main__":
    main()
