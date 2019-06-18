# Author: Dahir Muhammad Dahir
# Date: 17-June-2019 7:39 PM
# About: binary search implementation; given a sorted array A
# find out if element x is in A, else print -1
# end of input is indicated by -1 as string
# note: this is a bad implementation of binary search that doesn't work
# my bad, this is included to remind myself and anyone reading this
# that i didn't just get it the first time i tried, am not that good


def main():
    while True:
        sorted_array = input().strip().split(',')

        if sorted_array == "-1":
            break

        item = input()

        len_array = len(sorted_array)
        mid_array = int(len_array / 2)

        for i in range(len_array):
            start = 0
            end = len_array - 1

            if sorted_array[mid_array] == item:
                print("{} is at {} index in array".format(item, mid_array))
                break

            elif sorted_array[mid_array] > item:
                end = mid_array
                mid_array = int(end / 2)

            elif sorted_array[mid_array] < item:
                start = mid_array
                mid_array = int(len(sorted_array[start:end]) / 2)

            elif len(sorted_array[start:end]) == 0:
                print("-1")


if __name__ == "__main__":
    main()
