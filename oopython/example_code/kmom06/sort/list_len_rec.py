""" Showing recursion, length of a list """


def list_len(seq):
    if not seq:
        return 0
    else:
        return 1 + list_len(seq[1:])
        

bricks = [ "red", "blue", "green"]
  
print(list_len(bricks))