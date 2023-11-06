import pygame
import sys
import csv
import Button

class TileProperties:
    def __init__(self, TILETYPES):
        self.tile_list = []
        for x in range(TILETYPES):
            tile = pygame.image.load(f"tiles/{x}.png")
            self.tile_list.append(tile)
class screen(TileProperties):
    def __init__(self, Tile, MAPWIDTH, MAPHEIGHT):

        self.TileColor = Tile.tile_list

        self.screen = []
        for row in range(MAPHEIGHT + 1):
            r = [0] * MAPWIDTH
            self.screen.append(r)

        with open('map/Screen0.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.screen[x][y] = int(tile)
def draw_grid():
    #Draws Grid for level editor
    for c in range(MAPWIDTH+1):
        pygame.draw.line(DISPLAY, WHITE, (c * TILESIZE, 0), (c * TILESIZE, (MAPHEIGHT * TILESIZE)))
    for c in range(MAPHEIGHT+1):
        pygame.draw.line(DISPLAY, WHITE, (0, c * TILESIZE), (MAPWIDTH * TILESIZE, (c * TILESIZE)))
def make_buttons(tiles):
    button_list = []
    butcol = 0
    butrow = 0
    for i in range(TILETYPES):
        tile_button = Button.Button(DISPLAY,(MAPWIDTH*TILESIZE)+ (75*butcol) + 50, (75 * butrow) + 50, tiles.tile_list[i])
        button_list.append(tile_button)
        butcol += 1
        if butcol == 3:
            butrow += 1
            butcol = 0
    return button_list
TILESIZE = 30
TILETYPES = 4
MAPWIDTH = 45
MAPHEIGHT = 24
LOWER_MARGIN = 100
SIDE_MARGIN = 300
GREEN = (144, 201, 120)
RED = (200, 25, 25)
WHITE = (255, 255, 255)
current_tile = 0
tiles = TileProperties(TILETYPES)
screens = []

TestScreen = screen(tiles, MAPWIDTH, MAPHEIGHT)


#Create Display
pygame.init()
DISPLAY = pygame.display.set_mode(((MAPWIDTH*TILESIZE) + SIDE_MARGIN ,(MAPHEIGHT*TILESIZE) + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")
DISPLAY.fill(GREEN)
#Make Buttons
button_list = make_buttons(tiles)
for i in button_list:
    i.draw()

#User Interface
while True:
    button_count = 0
    for button_count, i in enumerate(button_list):
         if i.IsPressed():
            current_tile = button_count
    pygame.draw.rect(DISPLAY,RED, button_list[current_tile].rect, 3)
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for row in range(MAPHEIGHT): #Rows
        for col in range(MAPWIDTH): #Columns
            #pygame.draw.rect(DISPLAY,TestScreen.TileColor[TestScreen.map1[row][col]],(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
            DISPLAY.blit(TestScreen.TileColor[TestScreen.screen[row][col]],(col*TILESIZE,row*TILESIZE))
    #Update Display
    draw_grid()
    pygame.display.update()