

def print_x_last_elements(list, number):
    if not list:
        return 0
    counter = print_x_last_elements(list[1:], number)
    if counter < number:
        print(list[0])
    counter += 1
    return counter


my_list = [7, 2, 11, 4, 1, 8]

print_x_last_elements(my_list, 3)