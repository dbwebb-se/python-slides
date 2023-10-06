def read_from_file():
   """
   read file content and return content as a string
   """
   try:
       with open("read_from.txt", "r", encoding='utf8') as filehandler:
           return filehandler.read()
   except FileNotFoundError:
       print("You are missing the file")
   return None


def add_line():
   """
   add new line to file
   """
   new_line = input("Enter new line: ")
   write_to_file("\n" + new_line, "a")
   #with open("read_from.txt", "a", encoding='utf8') as filehandler:
    #   filehandler.write("\n" + new_line)

def write_to_file(content, mode):
   """
   write content to file
   """
   with open("read_from.txt", mode, encoding='utf8') as filehandler:
       filehandler.write(content)

def remove_line_from_file(content):
    """
    Remove a line from file with content as a list
    """
    print(content)
    rm_line = input("Enter line number to remove: ")
    content.pop(int(rm_line))
    content = "\n".join(content)
    write_to_file(content, "w")

def menu():
   """
   Main menu for program
   """
   while True:
       inp = input("""Enter option:
1. Read file
2. Append new line
3. Remove line
""")
       if inp == "1":
           print(read_from_file())
       elif inp == "2":
           add_line()
       elif inp == "3":
           content = read_from_file().split("\n")
           remove_line_from_file(content)
       else:
           exit()


if __name__ == "__main__":
   menu()
