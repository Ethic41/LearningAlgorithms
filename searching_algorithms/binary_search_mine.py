# Author: Dahir Muhammad Dahir
# Date: 17-June-2019 8:25 PM
# About: binary search implementation; given a sorted array A
# find out if element x is in A, else print -1
# end of input is indicated by -1 as string
# take-away: binary search implementation without proper thought is
# easy, mistakes like '(start - end) / 2' instead of '(start - end) / 2'
# when computing the middle of array, can be fatal
# also forgetting to check for searched value when 'start == end' is
# another common error


def main():
    sorted_array = input().strip().split(",")  # comma separated array expected

    if sorted_array == "-1":  # if end of input is reached
        return

    item = input()  # this is the item that will be searched for

    binary_search(sorted_array, item)  # searched for the item


def binary_search(sorted_array, item):
    len_array = len(sorted_array)  # getting the length of array

    start = 0  # start of array
    end = len_array - 1  # end of array
    mid = int(len_array / 2)  # middle of array

    while start != end:  # if we haven't converged
        if sorted_array[mid] == item:  # item has been found at the mid of array
            print("{} found at {}".format(item, mid))
            return

        if item > sorted_array[mid]:  # discarding the lower part of array
            start = mid + 1
            mid = int((start + end) / 2)

        if item < sorted_array[mid]:  # discarding the upper part of array
            end = mid - 1
            mid = int((start + end) / 2)

    if sorted_array[start] == item:  # we could have as well check with end, both are equal, True when we converge
        print("{} found at {}".format(item, start))
        return

    else:   # item doesn't exist in array, GTFO, lol
        print("-1")


if __name__ == "__main__":
    main()
