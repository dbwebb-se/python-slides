#!/usr/bin/python3
"""
Sorting algorithm Insertion sort
"""
# Start: sorterad del <=> listan[0], osorterad del <=> resten av listan
# Yttre loop, från index 1 till längden av listan
# inre index = yttre index
# Håll på så länge inre index > 0 och aktuellt tal är större än det i den sorterade listan.
#     Räkna ner inre index
# Returnera listan












def insertion_sort(seq):
    """
    Sorts a list with integer values with the insertion sort algorithm. O(n*n)
    """
    # Loop in the unsorted part, outer loop
    for index in range(1, len(seq)):
        print("Sorted list", seq[:index])
        current_pos = index
        current_val = seq[index]
        # Sort current into the sorted part, inner loop, backward
        while current_pos > 0 and seq[current_pos-1] > current_val: # while j > 0 and seq[j-1] > seq[j]:
            seq[current_pos] = seq[current_pos-1]
            current_pos -= 1
        seq[current_pos] = current_val
    return seq


my_list = [7, 2, 11, 4, 1, 8]

print(insertion_sort(my_list))














def insertion_sort_slim(seq):
    """
    O(n^2)
    """
    # O(n-1)
    for index in range(1, len(seq)):
        print("Sorted list", seq[:index])
        current_pos = index
        # 1, 2, 3, 4...n
        while current_pos > 0 and seq[current_pos-1] > seq[current_pos]:
                (seq[current_pos], seq[current_pos-1]) = (seq[current_pos-1], seq[current_pos])
                current_pos -= 1
    # O(n-1)*(n) --> O(n²)
    return seq

#print(insertion_sort_slim(my_list))
