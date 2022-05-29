# Author: Dahir Muhammad Dahir
# Date: 17-June-2019 7:10 PM
# About: this is my implementation of linear search algorithm
# that is given an array 'Array' find item 'item' in the array
# print out it's index else print -1, if it does not exist
# end of file is indicated by -1 as string


def main():
    while True:
        array = input().strip().split(',')

        if array == "-1":
            break

        item = input()

        print(linear_search(array, item))


def linear_search(array, item):
    len_array = len(array)

    for i in range(len_array):
        if array[i] == item:
            return i

    return -1


if __name__ == "__main__":
    main()
