"""
Reads from file
"""

def read_from_file(filename):
    """
    Reads from file specified as argument
    """
    # with opens the file, reads and closes the file with the statement
    # is finished
    with open(filename) as filehandler:
        print(filehandler.read())


if __name__ == "__main__":
    read_from_file("read_from.txt")
    