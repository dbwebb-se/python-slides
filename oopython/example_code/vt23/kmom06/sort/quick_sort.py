#!/usr/bin/python3
"""
Sorting algorithm Quick sort
"""
def quick_sort(seq):
    """
    Sorts a list with integer values with the Quick sort algorithm. O(n*n)
    """
    for i in range(1, len(seq)):
        current = seq[i]
        j = i # Sort current into the sorted part
        while j > 0 and seq[j-1] > current:
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = current
    return seq


my_list = [7, 2, 11, 4, 1, 8]

print(quick_sort(my_list))
