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
