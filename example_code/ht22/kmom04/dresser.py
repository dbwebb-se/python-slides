"""
Examples of the mutable datatype lists with a dresser
"""

# For prettier printing https://docs.python.org/3/library/pprint.html
from pprint import pprint

def add_item(dresser, drawer_no, item):
    """ Add 'item' in list 'dresser' on place 'drawer_no' """
    dresser[drawer_no] += item
    """ if (drawer_no < len(dresser)) :
        dresser[drawer_no] += item
    else:
        dresser.append(item) """

def add_part_wrong(dresser_part2):
    """ Add in a faulty way """
    dresser_part2 = "part 2 dresser" # String are immutable
    pprint(dresser_part2) # dresser_part2 is now a string and not a list

def add_part_new_list(dresser):
    """ Add to " jewelry to a new list """
    new_dresser = []
    for drawer in dresser:
        new_dresser.append(drawer + " jewelry")

    return new_dresser

def add_part_change_list(dresser):
    """ Add 'candy' and change the old list """
    for index, drawer in enumerate(dresser):
        dresser[index] = drawer + " candy"
    pprint(dresser)

dresser_part1 = [
    "jeans", # drawer no 0, top drawer
    "t-shirts", # drawer no 1
    "underwear", # drawer no 2
    "socks" # drawer no 3, bottom drawer
    ]

pprint("Example to add clothing to a drawer or items to a list")
pprint(dresser_part1)
add_item(dresser_part1, 1, " tank top")
add_item(dresser_part1, 3, " rag sock")
pprint(dresser_part1)
add_item(dresser_part1, 4, "hoody")
pprint(dresser_part1)
pprint("")

add_part_wrong(dresser_part1)
pprint(dresser_part1)
pprint("")

dresser_part3 = add_part_new_list(dresser_part1)
pprint(dresser_part3)
pprint(dresser_part1)
pprint("")

add_part_change_list(dresser_part1)
pprint(dresser_part1)
pprint("")

dresser_part1 = [
    "jeans", # drawer no 0, top drawer
    "t-shirts", # drawer no 1
    "underwear", # drawer no 2
    "socks" # drawer no 3, bottom drawer
    ]

pprint("List to string")
dresser_str = " ".join(dresser_part1)
pprint(dresser_str)
pprint(dresser_part1)
pprint("")

pprint("String to list")
dresser_str += " cardigan blanket"
dresser_from_str = dresser_str.split(" ")
pprint(dresser_str)
pprint(dresser_from_str)
pprint("")
