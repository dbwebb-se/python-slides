"""
shoe assignment. calc average show size
"""
from operator import itemgetter

def get_data():
    """
    Get names and sizes from user
    """
    data = {}
    choice = input("Enter 'name, shoesize': ")
    while choice != "done":
        name, size = choice.split(", ")
        data[name] = int(size)
        choice = input("Enter 'name, shoesize': ")
    return data

def print_data(data):
    """
    calculate average and print data
    """
    tot = 0
    print("Namn och skostorlek")
    sorted_data = sorted(data.items(), key=itemgetter(1))
    for name, size in sorted_data:
        print(f"{name}: {size}")
        tot += size
    print(f"average size is {tot/len(data)}")

if __name__ == "__main__":
    name_size = get_data()
    print_data(name_size)
