#!/usr/bin/python3
"""
Sorting algorithm Bubble sort
"""
def bubble_sort(seq):
    """
    Sorts a list with integer values with the bubble sort algorithm. O(n*n)
    """
    for _ in range(len(seq)):
        for j in range(len(seq) - 1):
            if seq[j] > seq[j+1]:
                # temp_data = seq[j]
                # seq[j] = seq[j+1]
                # seq[j+1] = temp_data
                (seq[j], seq[j+1]) = (seq[j+1], seq[j])
    return seq

def bubble_sort_faster(seq):
    """
    Sorts a list with integer values with the bubble sort algorithm. O(n*n)
    """
    for i in range(len(seq)):
        already_sorted = True
        for j in range(len(seq) - 1 - i):
            if seq[j] > seq[j+1]:
                # temp_data = seq[j]
                # seq[j] = seq[j+1]
                # seq[j+1] = temp_data
                (seq[j], seq[j+1]) = (seq[j+1], seq[j])
                already_sorted = False
        if already_sorted:
            break
    return seq

my_list = [7, 2, 11, 4, 1, 8]

#print(bubble_sort(my_list))

print(bubble_sort_faster(my_list))
