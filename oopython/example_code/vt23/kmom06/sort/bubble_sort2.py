#!/usr/bin/python3
"""
Sorting algorithm Bubble sort
"""
def bubble_sort(seq):
    """
    Sorts a list with integer values with the bubble sort algorithm. O(n*n)
    """
    for i in range(len(seq)):
        for j in range(len(seq) - 1):
            if seq[j] > seq[j+1]:
                temp_data = seq[j]
                seq[j] = seq[j+1]
                seq[j+1] = temp_data
    return seq


my_list = [7, 2, 11, 4, 1, 8]

print(bubble_sort(my_list))
