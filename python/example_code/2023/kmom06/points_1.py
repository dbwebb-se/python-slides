"""
Solve A4 in marvin1 using dictionaries
"""
def count_score(point_str):
    """
    Calculated points for each player
    """
    
    # loop in step of 2, [index] <=> player and [index + 1] <=> its points
    for index in range(0, len(point_str), 2):
        # Count the points, if upper subtract the points and if lower add the points
        print("Player " + point_str[index] + " with points: " + point_str[index + 1])
    

if __name__ == "__main__":
    count_score("a2b4A5s3B1")
