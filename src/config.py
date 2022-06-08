import pygame

FPS = 30

WINDOWWIDTH = 950
WINDOWHEIGHT = 500

BOARDWIDTH = 300
BOARDHEIGHT = 300

XMARGIN = 50
YMARGIN = 65

TILESIZE = 40


BLACK    = (  0,   0,   0)
WHITE    = (255, 255, 255)
GREEN    = (  0, 150,   0)
GRAY     = (150, 140, 150)
BLUE     = (  0,  50, 255)
YELLOW   = (255, 255,   0)
DARKGRAY = ( 40,  40,  40)
RED      = (255,   0,   0)


BACKGROUND_IMAGE = pygame.image.load("images/sea.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOWWIDTH, WINDOWHEIGHT))

LOGO_IMAGE = pygame.image.load("images/battleship_logo.png")
