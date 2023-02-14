#!/usr/bin/python3
"""
Sorting algorithm Selection sort
Task on lecture kmom06
"""

# Outer loop for current

    # Save index of the lowest value
    
    # Inner loop, find the lowest value and put it in current
    
        # If the value is lower, save the index for that value

    # Update the value on current position with the lowest number


















def selection_sort(seq):
    """
    Sorts a list with integer values with the Selction sort algorithm. O(n*n)
    """
    # Outer loop for current
    for current in range(len(seq)):
        # Save index of the lowest value
        min_index = current
        # Inner loop, find the lowest value and put it in current
        for j in range(current+1, len(seq)):
            # If the value is lower, save the index for that value
            if seq[j] < seq[min_index]:
                min_index = j
        # Update the value on current position with the lowest number
        (seq[current], seq[min_index]) = (seq[min_index], seq[current])
    return seq


my_list = [7, 2, 11, 4, 1, 8]

print(selection_sort(my_list))
