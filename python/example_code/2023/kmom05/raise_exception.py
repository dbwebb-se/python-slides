"""
Raise an exception when list is accessed out of range
"""

def print_number(a_list, index):
    """ 
    Prints out item in list, raise error if index is out of range.
    """
    if index >= len(a_list) or index < 0:
        raise IndexError(f"Index must be between 0 and {len(a_list)-1}")
    return a_list[index]

if __name__ == "__main__":   
    numbers = [ 1, 2, 3, 4]

    try:
        print("\nTestar index 1, ska bli 2")
        print(print_number(numbers, 1))
    except IndexError:
        print("Try again")
        
#     	print("\nTestar index mindre än 0")
#     	print(print_number(numbers, -1))
#     	print("\nTestar index 4, precis utan listan")
#     	print(print_number(numbers, 4))
    
#         print("\nTestar index större än 4")
#         print(print_number(numbers, 4))
