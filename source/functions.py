############################################################################   IMPORTS   #########################################################################

import random, math
from globals import console, dimension, game_size, resolution, board_size, square_size, active_button, in_pause_menu, playing, queens, active_queen, k
from globals import square_status, all_queens_clear, start

##########################################################################   FUNCTIONS   #########################################################################

def set_sizes():
    
    # Small
    if game_size[0] is 1:
        
        resolution[0] = resolution[1] = 450
        board_size[0] = board_size[1] = 400
        square_size[0] = 50
    
    # Medium
    if game_size[0] is 2:
        
        resolution[0] = resolution[1] = 594
        board_size[0] = board_size[1] = 528
        square_size[0] = 66
    
    # Big
    elif game_size[0] is 3:
        
        resolution[0] = resolution[1] = 756
        board_size[0] = board_size[1] = 672
        square_size[0] = 84
        
    return

def set_queens_positions():
     
    # Generating random queens positions
    i = 0
    while i < dimension:
         
        x = (random.randint(0, dimension - 1) * square_size[0]) + ((resolution[0] - board_size[0]) / 2)
        y = (random.randint(0, dimension - 1) * square_size[0]) + ((resolution[1] - board_size[1]) / 2)
         
        j = 0
        while j < i:
         
            if x != queens[j].pos[0] or y != queens[j].pos[1]: 
                j += 1
                     
            else:
                x = (random.randint(0, dimension - 1) * square_size[0]) + ((resolution[0] - board_size[0]) / 2)
                y = (random.randint(0, dimension - 1) * square_size[0]) + ((resolution[1] - board_size[1]) / 2)
                j = 0
        
        temp_k = int((y / square_size[0]) * dimension + (x / square_size[0]) + 1)
             
        queens[i].pos[0] = x
        queens[i].pos[1] = y
        queens[i].k = temp_k
        
        square_status[temp_k - 1] = 1
        i += 1
        
    return

def if_all_queens_clear():
    
    # For every queen
    for i in range(dimension):
        
        # Checking row
        for j in range(dimension):
            
            temp_k = int((queens[i].pos[1] / square_size[0]) * dimension + j + 1)
            
            if square_status[temp_k - 1] is 1:
                if temp_k != queens[i].k:
                    return False
                
        # Checking column
        for j in range(dimension):
            
            temp_k = int(((queens[i].pos[0] / square_size[0]) + j * dimension) + 1)
            
            if square_status[temp_k - 1] is 1:
                if temp_k != queens[i].k:
                    return False
                
        # Checking first diagonal (\)
        for j in range(dimension - int(math.fabs((queens[i].pos[0] / square_size[0]) - (queens[i].pos[1])/ square_size[0]))):
            
            temp_k = int((((((queens[i].pos[1] / square_size[0]) - min(queens[i].pos[0] / square_size[0], queens[i].pos[1] / square_size[0])) + j) * dimension) + ((queens[i].pos[0] / square_size[0]) - min(queens[i].pos[0] / square_size[0], queens[i].pos[1] / square_size[0]) + j)) + 1)
    
            if square_status[temp_k - 1] is 1:
                if temp_k != queens[i].k:
                    return False
                
        # Checking second diagonal (/)
        for j in range(dimension - int(math.fabs((dimension - 1 - (queens[i].pos[0] / square_size[0])) - (queens[i].pos[1])/ square_size[0]))):
            
            temp_k = int((((((queens[i].pos[1] / square_size[0]) + min(dimension - 1 - (queens[i].pos[1] / square_size[0]), queens[i].pos[0] / square_size[0])) - j) * dimension) + ((queens[i].pos[0] / square_size[0]) - min(dimension - 1 - (queens[i].pos[1] / square_size[0]), queens[i].pos[0] / square_size[0]) + j)) + 1)
    
            if square_status[temp_k - 1] is 1:
                if temp_k != queens[i].k:
                    return False
                
    return True

def sort_queens():
    
    min_index = 0;        
    
    # Sorting an array of queens by each queen's 'k' variable in ascending order
    for item in range(dimension):
    
        min_index = item
        j = item + 1
        
        while j < dimension: 
    
            if queens[j].k < queens[min_index].k: 
                min_index = j 
                
            j += 1
    
        if min_index != item:
            
            temp = queens[min_index]
            queens[min_index] = queens[item]
            queens[item] = temp
        
    # Updating 'active_queen' variable
    for item in range(dimension):
        if queens[item].k is k[0]:
            active_queen[0] = item
            break
    
    return

def refresh_important_variables():
    
    # Reset all the important variables
    for item in range(dimension):
        queens[item].pos[0] = queens[item].pos[1] = queens[item].k = 0
                            
    for item in range(dimension * dimension):
        square_status[item] = 0
        
    active_queen[0] = k[0] = 0
    all_queens_clear[0] = False
    
    start[0] = 0
    active_button[0] = 1
    
    return

def print_variables():
    
    # If printing in console is on
    if console[0] is True:
    
        print ("\n" * 80)
        print("SQUARES_STATUS:\n")
        
        # Printing squares statuses
        i = 0
        while i < dimension:
            
            string = ""
            j = i * dimension
            while j < (i * dimension) + dimension:
                string += str(square_status[j]) + " "
                j += 1
                
            print(string)
            i += 1
        
        print("\n")
        
        # Printing each queen's 'x', 'y' and 'k' variable
        for item in range(dimension):
            string = "Queen" + str(item) + ":      x = " + str(int(queens[item].pos[0] / square_size[0])) + "      "  + "y = " + str(int(queens[item].pos[1] / square_size[0]))
            string += "      " + "k = " + str(queens[item].k)
            print(string)
        
        # Printing 'active_queen' and global variables
        print("\nactive_queen = %d" % active_queen[0])
        print("k = %d" % k[0])
        print("all_queens_clear = %r" % all_queens_clear[0])
        
        # Printing menu info variables
        print("\nactive_button = %d" % active_button[0])
        print("in_pause_menu = %d" % in_pause_menu[0])
        print("playing = %d" % playing[0])
        
        # Printing system variables
        print("\nresolution = {}, {}".format(resolution[0], resolution[1]))
        print("game_size = %d" % game_size[0])
    
    return