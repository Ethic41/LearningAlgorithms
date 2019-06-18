# Author: Dahir Muhammad Dahir
# Date: 17-June-2019 11:10 PM
# About: jump search implementation, jump search works by jumping a certain
# block (best sqrt(n)) of the given array, until we reach a block
# where previous_block_index < x < current_block_index
# take-away: be very careful when stepping with range
# it could get dirty

from math import sqrt
from linear_search_mine import linear_search


def main():
    while True:
        sorted_array = list(map(int, input().strip().split(",")))

        if sorted_array == "-1":
            break

        item = int(input())

        print(jump_search(sorted_array, item))


def jump_search(sorted_array, item):
    size = len(sorted_array)

    block = int(sqrt(size))

    last_index = 0

    for i in range(0, size, block):
        if sorted_array[i] > item:
            target_block = sorted_array[last_index:]
            result = linear_search(target_block, item)
            return result + last_index

        last_index = i

    if last_index < size:
        target_block = sorted_array[last_index:]
        result = linear_search(target_block, item)
        return result + last_index

    return -1


if __name__ == "__main__":
    main()
