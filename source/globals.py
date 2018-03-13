############################################################################   IMPORTS   #########################################################################

import math

##################################################################################################################################################################

console = [False]                                                                                   # True = print info variables in console

### CONSTANTS ###
# Paths
icon_path = "files/icon.png"
font_path = "files/font.ttf"    

menu_bg_path = ["files/menu_bg_small.png", "files/menu_bg_medium.png", "files/menu_bg_big.png"]
info_bg_path = ["files/info_bg_small.png", "files/info_bg_medium.png", "files/info_bg_big.png"]

play_button_path = ["files/play_small.png", "files/play_medium.png", "files/play_big.png"]
size_button_path = ["files/size_small.png", "files/size_medium.png", "files/size_big.png"]
info_button_path = ["files/info_small.png", "files/info_medium.png", "files/info_big.png"]
quit_button_path = ["files/quit_small.png", "files/quit_medium.png", "files/quit_big.png"]

big_button_path = ["files/big_small.png", "files/big_medium.png", "files/big_big.png"]
med_button_path = ["files/med_small.png", "files/med_medium.png", "files/med_big.png"]
tiny_button_path = ["files/tiny_small.png", "files/tiny_medium.png", "files/tiny_big.png"]

back_button_path = ["files/back_small.png", "files/back_medium.png", "files/back_big.png"]
active_button_path = ["files/active_button_small.png", "files/active_button_medium.png", "files/active_button_big.png"]

board_path = ["files/chess_board_small.png", "files/chess_board_medium.png", "files/chess_board_big.png"]
queen_path = ["files/queen_small.png", "files/queen_medium.png", "files/queen_big.png"]
active_queen_path = ["files/active_queen_small.png", "files/active_queen_medium.png", "files/active_queen_big.png"]

# Game
dimension = 8                                                                                       # Chess board dimension

# Menu
button_width = [150, 198, 252]                                                                      # Menu buttons width (different for each game size)
button_height = [38, 50, 63]                                                                        # Menu buttons height

main_menu_top_offset = [130, 170, 220]                                                              # Top button offset from top border
size_menu_top_offset = [170, 220, 280]
pause_menu_top_offset = [170, 220, 280]
                                                             
main_menu_buttons = [4]                                                                             # Number of buttons menu contains
size_menu_buttons = [3]
pause_menu_buttons = [2]

# Final window
font_size = [28, 36, 48]                                                                       
text_in_line_top_offset = [7, 10, 10]                                                               # Text offset from top of its own line
title_left_offset = [110, 145, 180]                                                                 # Title ('Your time') left offset  
time_left_offset = [145, 195, 240]                                                                        

### NON - CONSTANTS ###
# Sizes
game_size = [0]                                                                                     # 1 = small, 2 = medium, 3 = big
resolution = [0] * 2                                                                                # Window width and height
board_size = [0] * 2                                                                                # Chess board width and height (without labels)
square_size = [0]                                                                                   # Size of a single chess board square in pixels

# Menu
active_button = [1]                                                                                 # Number of active menu button counting from 1
in_pause_menu = [False]                                                                             # True when game paused
playing = [False]                                                                                   # True when playing
        
# Game
queens = []                                                                                         # An array for 'QUEEN' class objects
active_queen = [0]                                                                                  # Active queen index (from 0 to dimension-1)
k = [0]                                                                                             # Active k index (from 1 to dimension^2)
square_status = [0] * int(math.pow(dimension, dimension))                                           # An array holding info where queens are (0 = free, 1 = occupied)
all_queens_clear = [False]                                                                          # True when game solved

# For time counting
start = [0]                                             
stop = [0]

# Structures
class QUEEN:
    
    # Constructor
    def __init__(self, x = 0, y = 0, k = 0):   
        self.pos = [x, y]                                                                           # x and y positions    (from 0 to dimension-1)
        self.k = k                                                                                  # k index              (from 1 to dimension^2)