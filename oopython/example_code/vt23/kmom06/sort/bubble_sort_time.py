#!/usr/bin/python3
"""
Sorting algorithm Bubble sort
"""

import time

def bubble_sort(seq):
    """
    Sorts a list with integer values with the bubble sort algorithm. O(n*n)
    """
    for _ in range(len(seq)):
        for j in range(len(seq) - 1):
            if seq[j] > seq[j+1]:
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
                (seq[j], seq[j+1]) = (seq[j+1], seq[j])
                already_sorted = False
        if already_sorted:
            break
    return seq

def bubble_sort_recursive(seq):
    """
    Sorts a list with integer values with the bubble sort algorithm. O(n*n)
    """
    def bubble_sort_rec(_seq, len):
        for i in range(len - 1):
            if _seq[i] > _seq[i + 1]:
                (seq[i], seq[i+1]) = (seq[i+1], seq[i])
        if len - 1 > 1:
            bubble_sort_rec(_seq, len - 1)
    
    bubble_sort_rec(seq, len(seq))
    return seq

my_list = [7, 77, 2, 11, 4, 1, 13, -2, 8, 5, 33, 3, 11, 0, 22, 6, 1]

print('\n Bubblesort ')
print(bubble_sort(my_list))

# get the start time
st = time.time()
# run the function
bubble_sort(my_list)
# get the end time
et = time.time()

# get execution time
res = (et - st) * 1000
print('Execution time:', res, 'milliseconds or ', round(1000*res, 2), 'ns')

print('\n Bubblesort faster')
print(bubble_sort_faster(my_list))

st = time.time()
bubble_sort_faster(my_list)
et = time.time()
res = (et - st) * 1000
print('Execution time:', res, 'milliseconds or ', round(1000*res, 2), 'ns')

print('\n Bubblesort recursive')
print(bubble_sort_recursive(my_list))

st = time.time()
bubble_sort_faster(my_list)
et = time.time()
res = (et - st) * 1000
print('Execution time:', res, 'milliseconds or ', round(1000*res, 2), 'ns')