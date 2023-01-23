""" Showing recursion, bricks """

bricks = [ "red", "blue", "green"]

def print_colors(index):
    if index < 0:
        return
    else:
        print(bricks[index], end=" ") # Show the bottom one first
        print_colors(index-1)
        #print(bricks[index], end=" ") # Show the top one first
        return
        

  
print_colors(2)

    
    