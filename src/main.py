import pygame, random, sys, math, time
from config import *
from pygame.locals import *


user_ships = []
computer_ships = []
user_occupied_tiles = []
computer_occupied_tiles = []
ship_lengths = [2, 3, 3, 4, 5]
ship_names = ["2", "3", "3a", "4", "5"]
alphabet = "ABCDEFGHIJ"


def main():
    global DISPLAY, FPS_CLOCK, user_grid, computer_grid, user_ships, user_occupied_tiles, computer_ships, ship_lengths, alphabet

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Battleship')
    pygame.display.set_icon(LOGO_IMAGE)

    MEDIUM_FONT = pygame.font.Font('freesansbold.ttf', 20)
    BIG_FONT = pygame.font.Font('freesansbold.ttf', 30)

    user_grid, computer_grid = generate_grids()

    game_setup()
    run_game()
def run_game():
    count = 0
    users_shot = True
    clicked = False
    shots_taken = 0
    generate_computer_ships()
    while True:

        DISPLAY.blit(BACKGROUND_IMAGE, (0, 0)) #Background sea image
        display_ships()
        display_tiles()


        draw_grid("Left", 3)
        draw_grid("Right", 3)
        draw_axis("Horizontal", "Left")
        draw_axis("Horizontal", "Right")
        draw_axis("Vertical", "Middle")
        display_text(50, 45, "Your board", GREEN, 20)
        display_text(730, 45, "Computers board", RED, 20)



        if users_shot == True:
            display_text(365, 1, "Your shot!", YELLOW, 40)
            display_text(410, 40, "Click to fire", YELLOW, 20)

            x, y = get_pos(highlight=True, topleft=True, board="Right")
            if clicked: #Mouse is clicked
                if x != False: #Mouse on computers grid
                    x_grid, y_grid = get_grid_ref(x, y, board="Right")
                    if computer_grid[y_grid][x_grid].uncovered == False:
                        users_shot = False
                        computer_grid[y_grid][x_grid].uncovered = True
                        shots_taken += 1



        elif users_shot == False:
            display_text(730, 45, "Computers board", GREEN, 20)
            users_shot = True

            while True:
                x_grid = random.randint(0, 9)
                y_grid = random.randint(0, 9)
                print(x_grid, y_grid)


                if user_grid[x_grid][y_grid].uncovered == False:
                    user_grid[x_grid][y_grid].uncovered = True
                    shots_taken += 1
                    break


        check_if_end(shots_taken)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP: # Left clicked

                x = event.pos[0]
                y = event.pos[1]

                if x > 50+450 and y > 65: #Top left grid corner
                    if x < 450+450 and y < 465: #Bottom right grid corner
                        clicked = True
                        click_location = event.pos
            else:
                clicked = False

            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()
        FPS_CLOCK.tick(FPS)
def game_setup():
    rotated = False
    ship_allowable_position = False
    clicked = False
   # user_ships = []

    while True:

        DISPLAY.blit(BACKGROUND_IMAGE, (0, 0)) #Background sea image
        draw_grid("Left", 3) #Displays user grid (left)
        draw_axis("Horizontal", "Left") #Displays Horizontal axis on the left
        draw_axis("Vertical", "Left") #Displays vertical axis on the left
        display_text(520, 400, "SPACE - Rotate       LEFTCLICK - Place", WHITE) #Controls to place instructions
        display_ships()

        ships_placed = len(user_ships) #How many ships have been placed so far

        display_text(483, 110, f"Place your {ship_lengths[ships_placed]} long ship!", WHITE, 40) # Instructions title
        x, y = get_pos(highlight=ship_allowable_position, topleft=True, length=ship_lengths[ships_placed], rotated=rotated) # Returns pos of topleft corner of grid square

        if x is False: #If pointer not on grid
            ship_allowable_position = False
        elif y <= 465-ship_lengths[ships_placed]*40 and rotated == True or rotated == False and x <= 450-ship_lengths[ships_placed]*40: # Full ship on the grid
            ship_allowable_position = check_tile_in_use(x, y, rotated, ship_lengths[ships_placed]) # Tile doesn't have other ship on it
        else:
            ship_allowable_position = False


        if ships_placed == 0:
            if ship_allowable_position == True:
                display_image(x, y, "images/ships/2.png", 80, 40, rotated)
                if clicked == True:
                    ship_2 = Ships(x, y, rotated, 2, "2")
                    user_ships.append(ship_2)
                    add_tile_in_use(x, y, rotated, ship_lengths[ships_placed])
            else:
                display_image(660, 260, "images/ships/2.png", 80, 40)

        elif ships_placed == 1:
            if ship_allowable_position == True:
                display_image(x, y, "images/ships/3.png", 120, 40, rotated)
                if clicked == True:
                    ship_3 = Ships(x, y, rotated, 3, "3")
                    user_ships.append(ship_3)
                    add_tile_in_use(x, y, rotated, ship_lengths[ships_placed])
            else:
                display_image(640, 260, "images/ships/3.png", 120, 40)

        elif ships_placed == 2:
            if ship_allowable_position == True:
                display_image(x, y, "images/ships/3a.png", 120, 40, rotated)
                if clicked == True:
                    ship_3a = Ships(x, y, rotated, 3, "3a")
                    user_ships.append(ship_3a)
                    add_tile_in_use(x, y, rotated, ship_lengths[ships_placed])
            else:
                display_image(640, 260, "images/ships/3a.png", 120, 40)

        elif ships_placed == 3:
            if ship_allowable_position == True:
                display_image(x, y, "images/ships/4.png", 160, 40, rotated)
                if clicked == True:
                    ship_4 = Ships(x, y, rotated, 4, "4")
                    user_ships.append(ship_4)
                    add_tile_in_use(x, y, rotated, ship_lengths[ships_placed])
            else:
                display_image(640, 260, "images/ships/4.png", 160, 40)

        elif ships_placed == 4:
            if ship_allowable_position == True:
                display_image(x, y, "images/ships/5.png", 200, 40, rotated)
                if clicked == True:
                    ship_5 = Ships(x, y, rotated, 5, "5")
                    user_ships.append(ship_5)
                    add_tile_in_use(x, y, rotated, ship_lengths[ships_placed])
                    return #All ships placed, head back to main game loop
            else:
                display_image(640, 260, "images/ships/5.png", 200, 40)


        # Checking events (Mouse/Keypresses)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP: # Left clicked

                x = event.pos[0]
                y = event.pos[1]

                if x > 50 and y > 65: #Top left grid corner
                    if x < 450 and y < 465: #Bottom right grid corner
                        clicked = True
                        click_location = event.pos
            else:
                clicked = False


            if event.type == KEYDOWN:
                if event.key == 32: #spacebar
                    rotated = not rotated #Swap boolean

            elif event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPS_CLOCK.tick(FPS)
def blowup(x, y, time=5):
    for i in range(5):
        display_image(x, y, f"images/explosion/blowup{i+1}.png", size_x=40, size_y=40, rotated=False)
        pygame.display.flip()
        FPS_CLOCK.tick(5)


def get_grid_ref(x, y, board="Left"):
    x_offset = 0
    # if board == "Right":
    #     x_offset = 450
    x_gr = math.floor((x-50-x_offset)/40)
    y_gr = math.floor((y-65)/40)

    return x_gr, y_gr


def check_if_end(shots_taken):
    user_won = True
    for y_axis in range(10):
        for x_axis in range(10):
            tile = computer_grid[x_axis][y_axis]
            if tile.contains_ship == True:
                if tile.uncovered == False:
                    user_won = False
    if user_won == True:
        show_end_screen("User", shots_taken)

    computer_won = True
    for y_axis in range(10):
        for x_axis in range(10):
            tile = user_grid[x_axis][y_axis]
            if tile.contains_ship == True:
                if tile.uncovered == False:
                    computer_won = False
    if computer_won == True:
        show_end_screen("Computer", shots_taken)


def show_end_screen(winner:str, shots_taken):
    while True:
        DISPLAY.blit(BACKGROUND_IMAGE, (0, 0)) #Background sea image
        display_text(160, 20, "GAME OVER", WHITE, 100)
        display_text(290, 360, f"In {math.floor(shots_taken/2)} shots", WHITE, 75)

        if winner == "User":
            display_text(315, 200, "You won!", GREEN, 75)

        elif winner == "Computer":
            display_text(310, 200, "You lost!", RED, 75)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)

