#!/usr/bin/python3
"""
Sorting algorithm Bubble sort faster
"""

import time

def bubble_sort_faster(seq):
    """
    Sorts a list with integer values with the bubble sort algorithm. O(n*n)
    """
    for i in range(len(seq)): 
        for j in range(len(seq) - 1 - i):
            if seq[j] > seq[j+1]:
                (seq[j], seq[j+1]) = (seq[j+1], seq[j])
    return seq

my_list = [7, 2, 11, 4, 1, 8]

start_time = time.time()
print(bubble_sort_faster(my_list))
print("--- %s seconds ---" % (time.time() - start_time))
