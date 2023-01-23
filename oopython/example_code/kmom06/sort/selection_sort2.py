#!/usr/bin/python3
"""
Sorting algorithm Selction sort
Task on lecture kmom05
"""
def selection_sort(seq):
    """
    Sorts a list with integer values with the Selction sort algorithm. O(n*n)
    """
    c = 0
    for current, value1 in enumerate(seq):
        min_index = current
        for j, value2 in enumerate(seq, start=current+1):
            c += 1
            if seq[j] < seq[min_index]:
                min_index = j
        (seq[current], seq[min_index]) = (seq[min_index], seq[current])
    print(c)
    return seq


my_list = [7, 2, 11, 4, 1, 8]
my_list2 = [4, 21, 5, 6, 2 ,1]

print(selection_sort(my_list))
print(selection_sort(my_list2))
