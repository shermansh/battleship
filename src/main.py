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
