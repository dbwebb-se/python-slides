"""
Reads specified lines from file
"""

def read_from_file(filename):
    """
    Reads from file specified as argument and returns list with all the lines
    """
    with open(filename, "r", encoding='utf8') as filehandler:
        content = filehandler.readlines()

    return content

def read_specified_lines_from_file(filename, number_of_lines):
    """
    Reads specified lines from file specified as first argument
    """
    lines = read_from_file(filename)

    for line in lines[:number_of_lines]:
        print(line.rstrip()) # rstrip removes whitespaces to the right, such as 
        # space ' ', tab '\t', newline '\n' etc


if __name__ == "__main__":
    specified_lines = int(input("How many lines do you want to print: "))
    read_specified_lines_from_file("manifesto.txt", specified_lines)
