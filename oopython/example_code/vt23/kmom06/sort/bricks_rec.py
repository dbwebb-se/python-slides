""" Showing recursion, bricks """

bricks = [ "red", "blue", "green"]

def print_colors(index):
    if index < 0:
        return
    else:
        print(bricks[index], end=" ") # Show the bottom one first
        print_colors(index-1)
        #print(bricks[index], end=" ") # Show the top one first
        

print("\n Räkna ner mot 0")   
print_colors(2)

    




def print_colors2(bricks,index):
    if index == len(bricks):
        return
    else:
        #print(bricks[index], end=" ") # Show the top one first
        print_colors2(bricks, index+1)
        print(bricks[index], end=" ") # Show the bottom one first
        

print("\n\nMed listan och index")   
print_colors2(bricks, 0)

