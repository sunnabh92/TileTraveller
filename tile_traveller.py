# Making a game that has 9 tiles. Main goal is to move from tile 1,1 to 3,1.
# Make function for begining location.
# For each tile the program prints out in which direciton you can move.
# Function for the winner.
# For each tile, the function must alert if the direction is invalid and keep still in the same tile. If the direction that is available is chosen then move to that direction.
# Have the functions for each direction not each tile.
# Program has to track current location and future locations, print out available direcitons for the right tile and ask for direction.
# https://github.com/sunnabh92/TileTraveller.git
def Initialize():
    location = (1,1)
    return location
location = (1,1)
    
'''
Tells where to go
''' 

def Possible_direction():
    if Position_of_player() == (1,1)or(2,1)or(3,1)or(1,2)or(3,2):
        if Directions() == "n" or "N":
            print("(N)orth")
    elif Position_of_player() == (1,2) or (2,2) or (3,2) or (1,3) or (3,3):
        if Directions() == "s" or "S":
            print("(S)outh")
    elif Position_of_player() == (1,3) or (3,2) or (1,2):
        if Directions() == "e" or "E":
            print("(E)ast")
    elif Position_of_player() == (3,3) or (2,3) or (2,2):
        if Directions() == "w" or "W":
            print("(W)est") 
    return Possible_direction

     

def Directions():
    direction_input = input("Direction: ")
    return direction_input
  

def Position_of_player():
    Position_of_player = location
    for char in (a,b):
        if Directions() == "n" or "N":
            b = b+1
        elif Directions() == "s" or "S":
            b = b-1
        elif Directions() == "e" or "E":
            a = a+1
        elif Directions() == "w" or "W":
            a = a-1
        else:
            a = a and b = b

    return Position_of_player

def Win():
    if Position_of_player() == (3,1):
        print("Victory!")

position = Initialize() #Tell game where player is positioned
print("You can travel: " + Possible_direction()) #Tell player which direction he can go
print("Direction: " + Directions()) #Player inputs direction
Win()




