# Author: Dahir Muhammad Dahir
# Date: 29-June-2019 10:26 AM
# About: given two linked list 'A' and 'B'
# find out if the first list is present in
# the second list, the list is going to be
# a linked list

from data_structures.linked_list import LinkedList


def main():
    array_a = list(map(int, input().strip().split(',')))
    array_b = list(map(int, input().strip().split(',')))
    list_a = LinkedList()
    list_b = LinkedList()

    list_a.array_to_linked_list(array_a)
    list_b.array_to_linked_list(array_b)

    print(sublist_search(list_a, list_b))


def sublist_search(list_a, list_b):
    inList = False
    current_a_node = list_a.head
    current_b_node = list_b.head

    while current_b_node is not None:
        if current_a_node is not None:
            if current_b_node.data == current_a_node.data:
                inList = True
                current_a_node = current_a_node.next
                current_b_node = current_b_node.next
            else:
                current_a_node = list_a.head
                if current_a_node.data == current_b_node.data:
                    inList = True
                    current_a_node = current_a_node.next
                    current_b_node = current_b_node.next
                else:
                    inList = False
                    current_a_node = current_a_node.next
                    current_b_node = current_b_node.next
        else:
            break

    if inList and current_a_node is None:
        return "List Found"
    else:
        return "List Not Found"


if __name__ == "__main__":
    main()
