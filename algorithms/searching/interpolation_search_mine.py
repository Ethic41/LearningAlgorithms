# Author: Dahir Muhammad Dahir
# Date: 18-June-2019 10:07 PM
# About: Interpolation search, is useful in a case of
# uniformly sorted array, unlike binary search where we
# jump to the middle of the array in this case we use the
# formula pos = start + [(x - array[start]) * (end - start) /
# array[end] - array[start] ], we use the value of pos to
# divide the array iteratively until we exhaust the array
# PS: once you can properly implement binary search this one
# is very easy


def main():
    uni_sorted_array = list(map(int, input().strip().split(",")))

    item = int(input())

    print(interpolation_search(uni_sorted_array, item))


def interpolation_search(uni_sorted_array, item):
    len_array = len(uni_sorted_array) - 1

    start = 0
    end = len_array

    pos = get_pos(start, end, uni_sorted_array, item)

    while start <= end:
        if item == uni_sorted_array[pos]:
            return pos

        elif item > uni_sorted_array[pos]:
            start = pos + 1
            pos = get_pos(start, end, uni_sorted_array, item)

        elif item < uni_sorted_array[pos]:
            end = pos - 1
            pos = get_pos(start, end, uni_sorted_array, item)


def get_pos(start, end, uni_sorted_array, item):
    return int(start + ((item - uni_sorted_array[start]) * (end - start) / (uni_sorted_array[end] - uni_sorted_array[start])))


if __name__ == "__main__":
    main()
