"""
Add items to a shoppinglist
"""

def read_file(filename):
    """
    Read content from file
    """
    try:
        with open(filename, "r", encoding='utf8') as filehandler:
            return filehandler.read()
    except FileNotFoundError:
        print("You are missing the file")
        return ""



def write_to_file(filename, content, mode):
    """
    write to file, mode should be "a" or "w"
    """
    with open(filename, mode, encoding='utf8') as filehandler:
        filehandler.write(content)



def main():
    """
    Meny for program
    """
    filename = "shopping.txt"
    while True:
        inp = input("Enter things to buy or shop: ")
        if inp == "shop":
            print("Shopping list:")
            print(read_file(filename))
            write_to_file(filename, "", "w")
        elif inp == "q":
            exit()
        else:
            write_to_file(filename, inp+"\n", "a")



if __name__ == "__main__":
    main()
