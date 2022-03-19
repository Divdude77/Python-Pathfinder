'''
###################################
#        PYTHON PATHFINDER        #
#          BY Divdude77           #
###################################
'''

#############################################
# READ readme.md BEFORE RUNNING THIS SCRIPT #
#############################################

# Get the map
map = open("map.txt").read().split("\n")

# Check if start and end point are present
if "X" not in "".join(map) or "O" not in "".join(map):
    print("Invalid Map!")
    begin = False
else: begin = True    


# Find starting point
x = y = None
for i in range(len(map)):
    if "O" in map[i]:
        x,y = map[i].index("O"), i

# Function to check if spot is available        
def checkspot(b,a):
    try:
        if map[a][b] == " " and (b,a) not in moves and (b,a) not in deadends: return True
    except: pass
    try: 
        if map[a][b] == "X": return "X"
    except: pass
    return False

places = []
moves = []
deadends = []
found = False
final = ["START!"]

while begin:
    moves.append((x,y))
    
    # Check for forks in path
    if checkspot(x,y+1) or checkspot(x,y-1) or checkspot(x+1,y) or checkspot(x-1,y):
        if checkspot(x,y+1) and (x,y+1) not in [i[-1] for i in places]:
            if checkspot(x,y-1): 
                places.append(((x,y),(x,y-1)))
            if checkspot(x+1,y):
                places.append(((x,y),(x+1,y)))
            if checkspot(x-1,y):
                places.append(((x,y),(x-1,y)))

        if checkspot(x,y-1) and (x,y-1) not in [i[-1] for i in places]:
            if checkspot(x,y+1):
                places.append(((x,y),(x,y+1)))
            if checkspot(x+1,y):
                places.append(((x,y),(x+1,y)))
            if checkspot(x-1,y):
                places.append(((x,y),(x-1,y))) 
        
        if checkspot(x+1,y) and (x+1,y) not in [i[-1] for i in places]:
            if checkspot(x,y+1):
                places.append(((x,y),(x,y+1)))
            if checkspot(x,y-1):
                places.append(((x,y),(x,y-1)))
            if checkspot(x-1,y):
                places.append(((x,y),(x-1,y)))
            
        if checkspot(x-1,y) and (x-1,y) not in [i[-1] for i in places]:
            if checkspot(x,y+1):
                places.append(((x,y),(x,y+1)))
            if checkspot(x,y-1):
                places.append(((x,y),(x,y-1)))
            if checkspot(x+1,y):
                places.append(((x,y),(x+1,y)))
    
    # Check if no more spots left to move
    elif checkspot(x,y+1) == checkspot(x,y-1) == checkspot(x+1,y) == checkspot(x-1,y) == False:
        if places:
            
            # Revert to last fork in path
            deadends.append((x,y))
            x,y = places[-1][-1] 
            moves = moves[:moves.index(places[-1][0]) + 1] + [places[-1][-1]]
            places.pop()

        else:
            
            # Exit if no forks existed
            print("No path!")
            break
    
    # Check if we reached end
    if checkspot(x,y+1) == "X":
        moves.append((x,y+1))
        found = True
        break
    if checkspot(x,y-1) == "X":
        moves.append((x,y-1)) 
        found = True
        break
    if checkspot(x+1,y) == "X":
        moves.append((x+1,y))
        found = True
        break
    if checkspot(x-1,y) == "X":
        moves.append((x-1,y))
        found = True
        break
    
    # Move position
    if checkspot(x,y+1): x,y = x,y+1
    elif checkspot(x,y-1): x,y = x,y-1
    elif checkspot(x+1,y): x,y = x+1,y
    elif checkspot(x-1,y): x,y = x-1,y
    
    del_list = []
    if places:
        for i in range(len(places)):
            if places[i][-1] == (x,y):
                del_list.append(i)
        for i in del_list:
            del places[i]
            for j in range(len(del_list)): del_list[j] -= 1
        
# Change moves to visible format
if found:
    for i in range(len(moves)):
        if i + 1 != len(moves):
            if moves[i][1] - 1 == moves[i+1][1]:
                final.append("UP")
            elif moves[i][1] + 1 == moves[i+1][1]:
                final.append("DOWN")
            elif moves[i][0] + 1 == moves[i+1][0]:
                final.append("RIGHT")
            elif moves[i][0] - 1 == moves[i+1][0]:
                final.append("LEFT")
    # print(final)
    # To print readable solution: print(final)
    
    for i in moves[1:-1]:
        map[i[-1]] = map[i[-1]][:i[0]] + "·" + map[i[-1]][i[0]+1:]
    print("\n".join(map))
    # To print drawn path solution: print("\n".join(map))
