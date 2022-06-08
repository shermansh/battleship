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
def generate_computer_ships():

    while True:
        ships_placed = len(computer_ships) #How many ships have been placed so far
        if ships_placed > 4:
                return
        x = XMARGIN + 450 + random.randint(0, 9)*40
        y = YMARGIN + random.randint(0, 9)*40
        rotated = random.choice([True, False])
        length = ship_lengths[ships_placed]

        if y <= 465-ship_lengths[ships_placed]*40 and rotated == True or rotated == False and x <= 450+450-ship_lengths[ships_placed]*40: # Full ship on the grid
            ship_allowable_position = check_tile_in_use(x, y, rotated, length, user=False) # Tile doesn't have other ship on it
        else:
            ship_allowable_position = False



        if ship_allowable_position:
            if ships_placed == 0:
                ship_2 = Ships(x, y, rotated, length, "2")
                computer_ships.append(ship_2)

            elif ships_placed == 1:
                ship_3 = Ships(x, y, rotated, length, "3")
                computer_ships.append(ship_3)

            elif ships_placed == 2:
                ship_3a = Ships(x, y, rotated, length, "3a")
                computer_ships.append(ship_3a)

            elif ships_placed == 3:
                ship_4 = Ships(x, y, rotated, length, "4")
                computer_ships.append(ship_4)

            elif ships_placed == 4:
                ship_5 = Ships(x, y, rotated, length, "5")
                computer_ships.append(ship_5)

            add_tile_in_use(x, y, rotated, length, user=False)
def check_tile_in_use(x, y, rotated, length, user=True):
    if user == True:
        occupied_tiles_list = user_occupied_tiles
    else:
        occupied_tiles_list = computer_occupied_tiles

    if x != False and y != False:

        if f"{x},{y}" in occupied_tiles_list:
            return False

        for i in range(length):
            if rotated == False: #Ship is Horizontal
                if f"{x+(40*i)},{y}" in occupied_tiles_list:
                    return False
            elif rotated == True: #Ship is vertical
                if f"{x},{y+(40*i)}" in occupied_tiles_list:
                    return False

    return True


def add_tile_in_use(x, y, rotated, length, user=True):
   # user_occupied_tiles.append(f"{x},{y}")
    x_offset = 0
    if user == False:
        x_offset = 450
    x_grid = math.floor((x-50-x_offset)/40)
    y_grid = math.floor((y-65)/40)

    if user:
        for i in range(length):
            if rotated == True: # Vertical
                user_occupied_tiles.append(f"{x},{y+40*i}")
                user_grid[y_grid+i][x_grid].contains_ship = True
            else: # Horizontal
                user_occupied_tiles.append(f"{x+40*i},{y}")
                user_grid[y_grid][x_grid+i].contains_ship = True
    else:
        for i in range(length):
            #(f"X:{x}({x_grid}), Y:{y}({y_grid}), Rotated:{rotated}, Len:{length}, User:{user}, i:{i}\n")
            if rotated == True: # Vertical
                computer_occupied_tiles.append(f"{x},{y+40*i}")
                computer_grid[y_grid+i][x_grid].contains_ship = True
            else: # Horizontal
                computer_occupied_tiles.append(f"{x+40*i},{y}")
                computer_grid[y_grid][x_grid+i].contains_ship = True
def display_ships():
    if user_ships:
        for i in user_ships:
            if i.rotated == True:
                width = 40
                height = i.length*40
            else:
                width = i.length*40
                height = 40

            display_image(i.x, i.y, f"images/ships/{i.image}.png", 40*i.length, 40, i.rotated)
    if computer_ships:
        for i in computer_ships:
            if i.rotated == True:
                width = 40
                height = i.length*40
            else:
                width = i.length*40
                height = 40

            display_image(i.x, i.y, f"images/ships/{i.image}.png", 40*i.length, 40, i.rotated)


def get_pos(highlight=True, topleft=False, length=1, rotated=False, board="Left"):
    coords = pygame.mouse.get_pos() # Get mouse pointer location
    x = coords[0]
    y = coords[1]
    if board == "Right":
        x_offset = 450
        x_tiles_offset = 11.25
    else:
        x_offset = 0
        x_tiles_offset = 0

    # Checks mouse location is on the gri
    if x > 50+x_offset and y > 65: #Top left grid coords
        if x < 450+x_offset and y < 465: #Bottom right grid coords

            # Converts pointer location to the grid square it is in
            x = math.floor((x-50-x_offset)/40)
            y = math.floor((y-65)/40)

            # Draw the blue rectangle
            if highlight == True:
                highlight_tile(x+x_tiles_offset, y, length, rotated)
            #
            if topleft == True:
                tl_x, tl_y = get_topleft_pixel(x, y)
                return tl_x, tl_y
            else:
                return x, y #gridsquare
    return False, False

# Finds the top left pixel from the grid square
def get_topleft_pixel(x, y):
    x = 50 + x*40
    y = 65 + y*40
    return x, y

# Display the blue highlighted rectangle
def highlight_tile(x, y, length, rotated):
    if rotated == False:
        pygame.draw.rect(DISPLAY, BLUE, pygame.Rect(50+40*x, 65+40*y, 40*length, 40), 4)
    elif rotated == True:
        pygame.draw.rect(DISPLAY, BLUE, pygame.Rect(50+40*x, 65+40*y, 40, 40*length), 4)

# Function to display text at a set location, size and colour
def display_text(x, y, text, colour, font_size=20):
    FONT = pygame.font.Font('freesansbold.ttf', font_size)
    TEXT = FONT.render(text, True, colour)
    TEXT_RECTANGLE = TEXT.get_rect()
    TEXT_RECTANGLE.topleft = (x, y)
    DISPLAY.blit(TEXT, TEXT_RECTANGLE)

# Function to display an image at a set location/rotation
def display_image(x, y, file, size_x=None, size_y=None, rotated=False):
    image = pygame.image.load(file)
    if size_x != None and size_y != None:
        image = pygame.transform.smoothscale(image, (size_x, size_y))
    if rotated == True:
        image = pygame.transform.rotate(image, -90)
    DISPLAY.blit(image, (x, y))

# Draws axis labels
def draw_axis(axis:str="Horizontal", position:str="Left"):

    if axis == "Horizontal": #Horizontal computer axis labels
        if position == "Left":
            offset = 0
        elif position == "Right":
            offset = 450

        for i in range(10):
            display_text(offset+65+TILESIZE*i, 473, str(i), WHITE)

    elif axis == "Vertical": #Vertical axis labels
        if position == "Left":
            x = 20
        elif position == "Middle":
            x = 468

        for i in range(10):
            display_text(x, 79+TILESIZE*i, alphabet[i], WHITE)
def display_tiles():

    for y_axis in range(10):
        for x_axis in range(10):
            tile = computer_grid[x_axis][y_axis]
            if tile.uncovered == True:
                if tile.contains_ship == True:
                    pygame.draw.rect(DISPLAY, RED, pygame.Rect(450+50+40*y_axis, 65+40*x_axis, 40, 40))
                else:
                    pass
            else:
                pygame.draw.rect(DISPLAY, GRAY, pygame.Rect(450+50+40*y_axis, 65+40*x_axis, 40, 40))

    for y_axis in range(10):
        for x_axis in range(10):
            tile = user_grid[x_axis][y_axis]
            if tile.uncovered == True:
                if tile.contains_ship == True:
                    pygame.draw.rect(DISPLAY, RED, pygame.Rect(50+40*y_axis, 65+40*x_axis, 40, 40))
                else:
                    pass
            else:
                pygame.draw.rect(DISPLAY, GRAY, pygame.Rect(50+40*y_axis, 65+40*x_axis, 40, 40))

# Draws grid lines
def draw_grid(side:str="Left", thickness=1):

    if side == "Left":
        for x in range(11): #Horizontal user gridlines
            pygame.draw.line(DISPLAY, DARKGRAY,
            (x*TILESIZE+XMARGIN, YMARGIN),
            (x*TILESIZE+XMARGIN, WINDOWHEIGHT - 35),
            thickness)
        for x in range(11): #Vertical user gridlines
            pygame.draw.line(DISPLAY, DARKGRAY,
            (XMARGIN, x*TILESIZE+YMARGIN),
            (WINDOWHEIGHT - XMARGIN, x*TILESIZE+YMARGIN),
            thickness)

    elif side == "Right":
        for x in range(11): #Horizontal computer gridlines
            pygame.draw.line(DISPLAY, DARKGRAY,
            (x*TILESIZE+XMARGIN+450, YMARGIN),
            (x*TILESIZE+XMARGIN+450, WINDOWHEIGHT - 35),
            thickness)

        for x in range(11): #Vertical computer gridlines
            pygame.draw.line(DISPLAY, DARKGRAY,
            (XMARGIN+450, x*TILESIZE+YMARGIN),
            (WINDOWHEIGHT - XMARGIN+450, x*TILESIZE+YMARGIN),
            thickness)
def generate_grids():
    user_grid = []
    computer_grid = []

    for y_axis in range(10):
        user_grid.append([])
        for x_axis in range(10):
            tile = Tiles(x_axis + 1, y_axis + 1, user=True)
            user_grid[y_axis].append(tile)
    for y_axis in range(10):
        computer_grid.append([])
        for x_axis in range(10):
            tile = Tiles(x_axis + 1, y_axis + 1, user=False)
            computer_grid[y_axis].append(tile)

    return user_grid, computer_grid






# Class for ship objects
class Ships:
    def __init__(self, x, y, rotated, length, image):
        self.x = x
        self.y = y
        self.rotated = rotated
        self.length = length
        self.image = image

# Class for tile objects
class Tiles:
    def __init__(self, x, y, user:bool):
        self.x = x
        self.y = y
        self.user = user
        self.contains_ship = False
        self.uncovered = False

#Starts game
if __name__ == "__main__":
    main()

