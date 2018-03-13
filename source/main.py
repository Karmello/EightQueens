############################################################################   IMPORTS   #########################################################################

import pygame, sys, os, random
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_KP1, K_KP2, K_KP3, K_KP4, K_KP6, K_KP7, K_KP8, K_KP9, K_SPACE, K_RETURN, K_ESCAPE

from globals import dimension, game_size, resolution, board_size, square_size, icon_path, font_path, menu_bg_path, info_bg_path, play_button_path, size_button_path 
from globals import info_button_path, quit_button_path, big_button_path, med_button_path, tiny_button_path, back_button_path, active_button_path, board_path
from globals import queen_path, active_queen_path, button_width, button_height, main_menu_top_offset, size_menu_top_offset, main_menu_buttons, size_menu_buttons
from globals import pause_menu_top_offset, pause_menu_buttons, font_size, title_left_offset, time_left_offset, text_in_line_top_offset, active_button, in_pause_menu
from globals import playing, queens, active_queen, k, square_status, all_queens_clear, start, stop, QUEEN
import functions

#######################################################################   SETTING UP STUFF   #####################################################################

# Determining game size
try:
    # Opening file stream
    stream = open("game_size.txt", "r")
    
    try:
        # Placing data into variable 
        game_size[0] = int(stream.read())
        stream.close()
        
        # If data is not valid
        if game_size[0] is not 1 and game_size[0] is not 2 and game_size[0] is not 3:
            game_size[0] = 2
    
    # If there's no data inside text file
    except(ValueError):
        game_size[0] = 2
        stream.close()
                
# If there's no file               
except(IOError):                                                  
    game_size[0] = 2
                             
functions.set_sizes()                                                                                   # Setting variables according to 'game_size'
pygame.init()                                                                                           # PYGAME initialization

# Setting window position on screen (middle)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (pygame.display.Info().current_w / 2 - resolution[0] / 2, pygame.display.Info().current_h / 2 - resolution[1] / 2)

screen = pygame.display.set_mode(resolution, 0, 32)                                                     # Setting window size and bit depth
font = pygame.font.SysFont("Tahoma", font_size[game_size[0] - 1], True, False)                          # Loading font and setting size

# Loading rest of the graphics
menu_bg = pygame.image.load(menu_bg_path[game_size[0] - 1]).convert()
info_bg = pygame.image.load(info_bg_path[game_size[0] - 1]).convert()

play_button = pygame.image.load(play_button_path[game_size[0] - 1]).convert_alpha()
size_button = pygame.image.load(size_button_path[game_size[0] - 1]).convert_alpha()
info_button = pygame.image.load(info_button_path[game_size[0] - 1]).convert_alpha()
quit_button = pygame.image.load(quit_button_path[game_size[0] - 1]).convert_alpha()

big_button = pygame.image.load(big_button_path[game_size[0] - 1]).convert_alpha()
med_button = pygame.image.load(med_button_path[game_size[0] - 1]).convert_alpha()
tiny_button = pygame.image.load(tiny_button_path[game_size[0] - 1]).convert_alpha()

back_button = pygame.image.load(back_button_path[game_size[0] - 1]).convert_alpha()
active_button_img = pygame.image.load(active_button_path[game_size[0] - 1]).convert()

board = pygame.image.load(board_path[game_size[0] - 1]).convert()
queen_img = pygame.image.load(queen_path[game_size[0] - 1]).convert_alpha()
active_queen_img = pygame.image.load(active_queen_path[game_size[0] - 1]).convert_alpha()

# Setting window icon, title and mouse visibility (hidden)
icon = pygame.image.load(icon_path).convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption("E I G H T   Q U E E N S   [ C r e a t e d   b y   N o g a   K a m i l ]")
pygame.mouse.set_visible(False)

#######################################################   FUNCTIONS THAT NEEDS TO BE DEFINED IN MAIN FILE   ######################################################

def draw_main_menu():
    
    # Drawing graphics
    screen.blit(menu_bg, (0, 0))
    screen.blit(active_button_img, (button_width[game_size[0] - 1], main_menu_top_offset[game_size[0] - 1] + (active_button[0] - 1) * button_height[game_size[0] - 1]))
    screen.blit(play_button, (button_width[game_size[0] - 1], main_menu_top_offset[game_size[0] - 1]))
    screen.blit(size_button, (button_width[game_size[0] - 1], main_menu_top_offset[game_size[0] - 1] + button_height[game_size[0] - 1]))
    screen.blit(info_button, (button_width[game_size[0] - 1], main_menu_top_offset[game_size[0] - 1] + 2*button_height[game_size[0] - 1]))
    screen.blit(quit_button, (button_width[game_size[0] - 1], main_menu_top_offset[game_size[0] - 1] + 3*button_height[game_size[0] - 1]))
    
    # Updating screen
    pygame.display.update()
    
    # Printing variables to console
    functions.print_variables()

    return

def draw_size_menu():
    
    # Drawing graphics
    screen.blit(menu_bg, (0, 0))
    screen.blit(active_button_img, (button_width[game_size[0] - 1], size_menu_top_offset[game_size[0] - 1] + (active_button[0] - 1) * button_height[game_size[0] - 1]))
    screen.blit(big_button, (button_width[game_size[0] - 1], size_menu_top_offset[game_size[0] - 1]))
    screen.blit(med_button, (button_width[game_size[0] - 1], size_menu_top_offset[game_size[0] - 1] + button_height[game_size[0] - 1]))
    screen.blit(tiny_button, (button_width[game_size[0] - 1], size_menu_top_offset[game_size[0] - 1] + 2*button_height[game_size[0] - 1]))
    
    # Updating screen
    pygame.display.update()
    
    # Printing variables to console
    functions.print_variables()

    return

def draw_pause_menu():
    
    # Drawing graphics
    screen.blit(menu_bg, (0, 0))
    screen.blit(active_button_img, (button_width[game_size[0] - 1], pause_menu_top_offset[game_size[0] - 1] + (active_button[0] - 1) * button_height[game_size[0] - 1]))
    screen.blit(back_button, (button_width[game_size[0] - 1], pause_menu_top_offset[game_size[0] - 1]))
    screen.blit(quit_button, (button_width[game_size[0] - 1], pause_menu_top_offset[game_size[0] - 1] + button_height[game_size[0] - 1]))
    
    # Updating screen
    pygame.display.update()
    
    # Print variables to console
    functions.print_variables()
    
    return

def draw_game():
    
    # Drawing graphics
    screen.blit(board, (0, 0))
    
    for item in range(dimension):
        
        # If still playing
        if all_queens_clear[0] is False:
            
            if item is active_queen[0]:
                screen.blit(active_queen_img, (queens[item].pos))
            else:
                screen.blit(queen_img, (queens[item].pos))
               
        # If game solved
        else:
            screen.blit(active_queen_img, (queens[item].pos))
        
    # If game solved
    if all_queens_clear[0] is True:
        
        stop[0] = pygame.time.get_ticks()
        screen_copy = pygame.Surface.copy(screen)
        draw_finish_info()
        screen.blit(screen_copy, (0, 0))
        
        playing[0] = False
        
    # Updating screen
    pygame.display.update()
    
    # Printing variables to console
    functions.print_variables()
    
    # If game was solved, final time screen is gone and we are waiting for the user to press 'ESC' for the last time before going back to main menu
    if playing[0] is False:
        while True:
            for event in pygame.event.get():
                
                # Quit program event
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()    
                    
                # Escape
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
    
    return

def change_game_size():
    
    # Using globals
    global screen, font, menu_bg, info_bg, play_button, size_button, info_button, quit_button, big_button, med_button, tiny_button, back_button
    global active_button_img, board, queen_img, active_queen_img
    
    # Setting variables according to 'game_size'
    functions.set_sizes()
    
    # Reloading display module
    screen = pygame.display.quit()
    screen = pygame.display.init()
    
    # Setting window position on screen (middle)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (pygame.display.Info().current_w / 2 - resolution[0] / 2, pygame.display.Info().current_h / 2 - resolution[1] / 2)
    
    # Setting window size and bit depth
    screen = pygame.display.set_mode(resolution, 0, 32)
    
    # Loading font and setting size
    font = pygame.font.SysFont("Tahoma", font_size[game_size[0] - 1], True, False)                                
    
    # Loading rest of the graphics
    menu_bg = pygame.image.load(menu_bg_path[game_size[0] - 1]).convert()
    info_bg = pygame.image.load(info_bg_path[game_size[0] - 1]).convert()
    
    play_button = pygame.image.load(play_button_path[game_size[0] - 1]).convert_alpha()
    size_button = pygame.image.load(size_button_path[game_size[0] - 1]).convert_alpha()
    info_button = pygame.image.load(info_button_path[game_size[0] - 1]).convert_alpha()
    quit_button = pygame.image.load(quit_button_path[game_size[0] - 1]).convert_alpha()
    
    big_button = pygame.image.load(big_button_path[game_size[0] - 1]).convert_alpha()
    med_button = pygame.image.load(med_button_path[game_size[0] - 1]).convert_alpha()
    tiny_button = pygame.image.load(tiny_button_path[game_size[0] - 1]).convert_alpha()
    
    back_button = pygame.image.load(back_button_path[game_size[0] - 1]).convert_alpha()
    active_button_img = pygame.image.load(active_button_path[game_size[0] - 1]).convert()
    
    board = pygame.image.load(board_path[game_size[0] - 1]).convert()
    queen_img = pygame.image.load(queen_path[game_size[0] - 1]).convert_alpha()
    active_queen_img = pygame.image.load(active_queen_path[game_size[0] - 1]).convert_alpha()
    
    # Setting window icon, title and mouse visibility (hidden)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("E I G H T   Q U E E N S   [ C r e a t e d   b y   N o g a   K a m i l ]")
    pygame.mouse.set_visible(False)

    # Saving game size to file
    try:
        stream = open("game_size.txt", "w")
        stream.write(str(game_size[0]))
        stream.close()
    
    # If cannot open stream to write
    except: 
        pass
    
    return

def draw_finish_info():
    
    # Converting m-seconds to hours, minutes and seconds
    miliseconds = round(stop[0] - start[0])
    hours = miliseconds // 3600000
    miliseconds -= (hours * 3600000)
    minutes = miliseconds // 60000
    miliseconds -= (minutes * 60000)
    seconds = miliseconds // 1000

    final_window_height = 2 * square_size[0]

    if hours < 10:
        hours_string = "0" + str(int(hours))
    else:
        hours_string = str(int(hours))
    if minutes < 10:
        minutes_string = "0" + str(int(minutes))
    else:
        minutes_string = str(int(minutes))
    if seconds < 10:
        seconds_string = "0" + str(int(seconds))
    else:
        seconds_string = str(int(seconds))

    string = font.render(hours_string + " : " + minutes_string + " : " + seconds_string, 10, (255, 255, 255))

    # Drawings
    pygame.draw.rect(screen, (0, 0, 0), (0, (resolution[1] - final_window_height) / 2, resolution[0], final_window_height), 0)
    title = font.render("Y O U R   T I M E", 10, (255, 255, 255))
    screen.blit(title, (title_left_offset[game_size[0] - 1], (resolution[1] - final_window_height) / 2 + text_in_line_top_offset[game_size[0] - 1]))
    screen.blit(string, (time_left_offset[game_size[0] - 1], (resolution[1] - final_window_height) / 2 + square_size[0] + text_in_line_top_offset[game_size[0] - 1]))
    pygame.display.update()
    
    # Printing variables to console
    functions.print_variables()
    
    # Waiting for user to press Escape
    while True:
        for event in pygame.event.get():
            
            # Quit program event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()    
                
            # Escape
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return
        
    return

############################################################################   LOOPS   ###########################################################################

def size_loop():
    
    # Size menu loop
    while True:
        
        # Event checking
        for event in pygame.event.get():
            
            # Quit program event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()    
                
            # Key events
            if event.type == KEYDOWN:
            
                # Escape
                if event.key == K_ESCAPE:
                    return
                
                # Up
                elif event.key == K_UP:
                    
                    if active_button[0] > 1:
                        active_button[0] -= 1
                        
                    elif active_button[0] == 1:
                        active_button[0] = size_menu_buttons[0]
                    
                    draw_size_menu()
                
                # Down
                elif event.key == K_DOWN:
                    
                    if active_button[0] < size_menu_buttons[0]:
                        active_button[0] += 1
                    
                    elif active_button[0] == size_menu_buttons[0]:
                        active_button[0] = 1
                    
                    draw_size_menu()
                    
                # Enter    
                elif event.key == K_RETURN:
                    
                    # If game size will be changed
                    if active_button[0] != size_menu_buttons[0] - game_size[0] + 1:
                        
                        game_size[0] = size_menu_buttons[0] - active_button[0] + 1
                        change_game_size()
                        draw_size_menu()
    return

def pause_loop():

    # Pause game loop
    while in_pause_menu[0] is True:
        
        # Event checking
        for event in pygame.event.get():
            
            # Quit program event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()    
                
            # Key events
            if event.type == KEYDOWN:
            
                # Escape or label1->Enter - continue playing
                if event.key == K_ESCAPE or (event.key == K_RETURN and active_button[0] is 1):
                    in_pause_menu[0] = False
                    draw_game()
                    
                # label2->Enter - quit playing    
                elif event.key == K_RETURN:
                    in_pause_menu[0] = False
                    playing[0] = False
                    return
                
                # Up or Down
                elif event.key == K_UP or event.key == K_DOWN:
                    
                    if active_button[0] == 1:
                        active_button[0] = pause_menu_buttons[0]
                        draw_pause_menu()
                        
                    elif active_button[0] == pause_menu_buttons[0]:
                        active_button[0] = 1
                        draw_pause_menu()
                        
    return

def game_loop():
   
    # Game loop
    while playing[0] is True:
            
        # Events checking
        for event in pygame.event.get():
            
            # Quit program event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Key events
            if event.type == KEYDOWN:
                
                # Escape
                if event.key == K_ESCAPE:
                    
                    in_pause_menu[0] = True
                    
                    active_button[0] = 1
                    draw_pause_menu()
                    
                    # To pause loop function >>>
                    stop[0] = pygame.time.get_ticks()
                    pause_loop()
                    start[0] += pygame.time.get_ticks() - stop[0]
                    
                    # Leaving game and going to main menu
                    if playing[0] is False:
                        
                        # Reset all the important variables
                        functions.refresh_important_variables()
                        
                        draw_main_menu()
                        return
                                
                # Left
                elif event.key == K_KP4 or event.key == K_LEFT:                                                                                   
                    
                    if queens[active_queen[0]].pos[0] >= square_size[0] + ((resolution[0] - board_size[0]) / 2) and square_status[k[0] - 2] is 0:
                        
                        queens[active_queen[0]].pos[0] -= square_size[0]
                        square_status[k[0] - 1] = 0
                        k[0] -= 1
                        square_status[k[0] - 1] = 1
                        queens[active_queen[0]].k = k[0]
                        functions.sort_queens()
                        all_queens_clear[0] = functions.if_all_queens_clear()
                        draw_game()
                
                # Right
                elif event.key == K_KP6 or event.key == K_RIGHT:                                                                                
                    
                    if queens[active_queen[0]].pos[0] <= ((dimension - 2) * square_size[0]) + ((resolution[0] - board_size[0]) / 2) and square_status[k[0]] is 0:
                        
                        queens[active_queen[0]].pos[0] += square_size[0]
                        square_status[k[0] - 1] = 0
                        k[0] += 1
                        square_status[k[0] - 1] = 1
                        queens[active_queen[0]].k = k[0]
                        functions.sort_queens()
                        all_queens_clear[0] = functions.if_all_queens_clear()
                        draw_game()
                
                # Up
                elif event.key == K_KP8 or event.key == K_UP:                                                                                  
                    
                    if queens[active_queen[0]].pos[1] >= square_size[0] + ((resolution[1] - board_size[1]) / 2) and square_status[k[0] - dimension - 1] is 0:
                        
                        queens[active_queen[0]].pos[1] -= square_size[0]
                        square_status[k[0] - 1] = 0
                        k[0] -= dimension
                        square_status[k[0] - 1] = 1
                        queens[active_queen[0]].k = k[0]
                        functions.sort_queens()
                        all_queens_clear[0] = functions.if_all_queens_clear()
                        draw_game()
                
                # Down  
                elif event.key == K_KP2 or event.key == K_DOWN:                                                                               
                    
                    if queens[active_queen[0]].pos[1] <= ((dimension - 2) * square_size[0]) + ((resolution[1] - board_size[1]) / 2) and square_status[k[0] + dimension - 1] is 0:
                        
                        queens[active_queen[0]].pos[1] += square_size[0]
                        square_status[k[0] - 1] = 0
                        k[0] += dimension
                        square_status[k[0] - 1] = 1
                        queens[active_queen[0]].k = k[0]
                        functions.sort_queens()
                        all_queens_clear[0] = functions.if_all_queens_clear()
                        draw_game()
                
                # Up - Left
                elif event.key == K_KP7:                                                                                                        
                    
                    if queens[active_queen[0]].pos[0] >= square_size[0] + ((resolution[0] - board_size[0]) / 2) and queens[active_queen[0]].pos[1] >= square_size[0] + ((resolution[1] - board_size[1]) / 2) and square_status[k[0] - (dimension + 1) - 1] is 0:
                        
                        queens[active_queen[0]].pos[0] -= square_size[0]
                        queens[active_queen[0]].pos[1] -= square_size[0]
                        square_status[k[0] - 1] = 0
                        k[0] -= (dimension + 1)
                        square_status[k[0] - 1] = 1
                        queens[active_queen[0]].k = k[0]
                        functions.sort_queens()
                        all_queens_clear[0] = functions.if_all_queens_clear()
                        draw_game()
                
                # Up - Right     
                elif event.key == K_KP9:                                                                                                                
                    
                    if queens[active_queen[0]].pos[0] <= ((dimension - 2) * square_size[0]) + ((resolution[0] - board_size[0]) / 2) and queens[active_queen[0]].pos[1] >= square_size[0] + ((resolution[1] - board_size[1]) / 2) and square_status[k[0] - (dimension - 1) - 1] is 0:
                        
                        queens[active_queen[0]].pos[0] += square_size[0]
                        queens[active_queen[0]].pos[1] -= square_size[0]
                        square_status[k[0] - 1] = 0
                        k[0] -= (dimension - 1)
                        square_status[k[0] - 1] = 1
                        queens[active_queen[0]].k = k[0]
                        functions.sort_queens()
                        all_queens_clear[0] = functions.if_all_queens_clear()
                        draw_game()
                
                # Down - Left
                elif event.key == K_KP1:                                                                                                                    
                    
                    if queens[active_queen[0]].pos[0] >= square_size[0] + ((resolution[0] - board_size[0]) / 2) and queens[active_queen[0]].pos[1] <= ((dimension - 2) * square_size[0]) + ((resolution[1] - board_size[1]) / 2) and square_status[k[0] + (dimension - 1) - 1] is 0:
                        
                        queens[active_queen[0]].pos[0] -= square_size[0]
                        queens[active_queen[0]].pos[1] += square_size[0]
                        square_status[k[0] - 1] = 0
                        k[0] += (dimension - 1)
                        square_status[k[0] - 1] = 1
                        queens[active_queen[0]].k = k[0]
                        functions.sort_queens()
                        all_queens_clear[0] = functions.if_all_queens_clear()
                        draw_game()
                
                # Down - Right
                elif event.key == K_KP3:
                    
                    if queens[active_queen[0]].pos[0] <= ((dimension - 2) * square_size[0]) + ((resolution[0] - board_size[0]) / 2) and queens[active_queen[0]].pos[1] <= ((dimension - 2) * square_size[0]) + ((resolution[1] - board_size[1]) / 2) and square_status[k[0] + (dimension + 1) - 1] is 0:
                        
                        queens[active_queen[0]].pos[0] += square_size[0]
                        queens[active_queen[0]].pos[1] += square_size[0]
                        square_status[k[0] - 1] = 0
                        k[0] += (dimension + 1)
                        square_status[k[0] - 1] = 1
                        queens[active_queen[0]].k = k[0]
                        functions.sort_queens()
                        all_queens_clear[0] = functions.if_all_queens_clear()
                        draw_game()
                        
                # Space
                elif event.key == K_SPACE:
                    
                    if active_queen[0] is dimension - 1:
                        active_queen[0] = 0
                    else:
                        active_queen[0] += 1
                        
                    k[0] = int((queens[active_queen[0]].pos[1] / square_size[0]) * dimension + (queens[active_queen[0]].pos[0] / square_size[0]) + 1)
                    draw_game()
            
    return

#############################################################   THE WHOLE PROGRAM STARTS FROM HERE   #############################################################

# Adding instances of 'QUEEN' class to 'queens' array
for _ in range(dimension):
    instance = QUEEN()
    queens.append(instance)

draw_main_menu()                                                                            # Drawing main menu
pygame.event.clear()                                                                        # Clearing every event that happened before main menu shown up

# Main loop
while True:
    for event in pygame.event.get():
        
        # Quit program events
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # Key events
        if event.type is KEYDOWN:
            
            # Up
            if event.key == K_UP:
                
                if active_button[0] > 1:
                    active_button[0] -= 1
                    
                elif active_button[0] == 1:
                    active_button[0] = main_menu_buttons[0]
                
                draw_main_menu()
            
            # Down
            elif event.key == K_DOWN:
                
                if active_button[0] < main_menu_buttons[0]:
                    active_button[0] += 1
                
                elif active_button[0] == main_menu_buttons[0]:
                    active_button[0] = 1
                
                draw_main_menu()
                
            # Enter
            elif event.key == K_RETURN:
                
                # Play
                if active_button[0] == 1:
                    
                    playing[0] = True
                    all_queens_clear[0] = True
                    
                    # Making sure program always starts with bad queens combination
                    while all_queens_clear[0] is True:
                        functions.set_queens_positions()
                        all_queens_clear[0] = functions.if_all_queens_clear()

                    active_queen[0] = random.randint(0, dimension - 1)
                    k[0] = queens[active_queen[0]].k
                    functions.sort_queens()
                    draw_game()
                    
                    # To game loop function >>>
                    start[0] = pygame.time.get_ticks()
                    game_loop()
        
                    # Back to main menu with fresh variables
                    functions.refresh_important_variables()
                    draw_main_menu()
                    
                # Size
                elif active_button[0] == 2:
                    
                    active_button[0] = size_menu_buttons[0] - game_size[0] + 1
                    draw_size_menu()
                    size_loop()
                    active_button[0] = 2
                    draw_main_menu()
                
                # Info
                elif active_button[0] == 3:
                    
                    screen.blit(info_bg, (0, 0))
                    pygame.display.update()
                    in_info_menu = True
                    
                    # Waiting for Escape
                    while in_info_menu is True:
                        for event in pygame.event.get():
                            
                            # Quit events
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()    
                                
                            # Going back to main menu
                            if event.type == KEYDOWN and event.key == K_ESCAPE:
                                in_info_menu = False
                                draw_main_menu()
                
                # Quit
                elif active_button[0] == 4:
                    pygame.quit()
                    sys.exit()