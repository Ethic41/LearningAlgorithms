# Author: Dahir Muhammad Dahir
# Date: 02-July-2019 4:49 PM
# About: this is a rough file to test my ideas
# do not expect my best here


def main():
    input_array = list(map(int, input().strip().split()))
    target_element = int(input().strip())
    print(binary_floor_search(input_array, target_element))


def binary_search(array, target):
    len_array = len(array)
    start = 0
    end = len_array - 1
    mid = int((start + end) / 2)

    while start <= end:
        if array[mid] == target:
            return mid

        if array[mid] < target:
            start = mid + 1
            mid = int((start + end) / 2)

        if array[mid] > target:
            end = mid - 1
            mid = int((start + end) / 2)

    return -1


def binary_floor_search(array, key):
    len_array = len(array)
    start = 0
    end = len_array - 1
    mid = int((start + end) / 2)

    while start <= end:
        if array[mid] == key and mid > 0:
            return array[mid - 1]
        elif array[mid] > key:
            if array[mid - 1] < key:
                return array[mid - 1]
            end = mid - 1
            mid = int((start + end) / 2)
        else:
            start = mid + 1
            mid = int((start + end) / 2)

    return -1


if __name__ == "__main__":
    main()
