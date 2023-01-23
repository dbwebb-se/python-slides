#!/usr/bin/python3
"""
Sorting algorithm Bubble sort
"""

# Outer loop, all elements

    # Inner loop with comparison
    
        # Change place, bubble larger element to the right

























def bubble_sort(seq):
    """
    Sorts a list with integer values with the bubble sort algorithm. O(n*n)
    """
    # Outer loop, all elements
    for _ in range(len(seq)):
        # Inner loop with comparison
        for j in range(len(seq)): # run without minus 1 first
            value1 = seq[j]
            value2 = seq[j+1]
            # Change place, bubble larger element to the right
            if value1 > value2:
                seq[j] = value2
                seq[j+1] = value1
    return seq


my_list = [7, 2, 11, 4, 1, 8]

print(bubble_sort(my_list))
