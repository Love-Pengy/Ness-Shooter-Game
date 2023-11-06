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
#Draws Grid for level editor
def draw_grid():
    for c in range(MAPWIDTH+1):
        pygame.draw.line(DISPLAY, WHITE, (c * TILESIZE, 0), (c * TILESIZE, (MAPHEIGHT * TILESIZE)))
    for c in range(MAPHEIGHT+1):
        pygame.draw.line(DISPLAY, WHITE, (0, c * TILESIZE), (MAPWIDTH * TILESIZE, (c * TILESIZE)))
#function makes buttons for all tiletypes automatically
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
#function for outputting text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    DISPLAY.blit(img,(x,y))
TILESIZE = 30
TILETYPES = 4
MAPWIDTH = 45
MAPHEIGHT = 24
LOWER_MARGIN = 100
SIDE_MARGIN = 300
GREEN = (144, 201, 120)
RED = (200, 25, 25)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
current_tile = 0
CurrentX = 5
CurrentY = 5
tiles = TileProperties(TILETYPES)
screens = []
#Create Save and Load Buttons
save = pygame.image.load("tiles/save.png")
load = pygame.image.load("tiles/load.png")

TestScreen = screen(tiles, MAPWIDTH, MAPHEIGHT)


#Create Display
pygame.init()
DISPLAY = pygame.display.set_mode(((MAPWIDTH*TILESIZE) + SIDE_MARGIN ,(MAPHEIGHT*TILESIZE) + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")
DISPLAY.fill(BLACK)
#Make Buttons
savebtn = Button.Button(DISPLAY,(MAPWIDTH*TILESIZE)//2,((MAPHEIGHT*TILESIZE)+LOWER_MARGIN-75),save)
loadbtn = Button.Button(DISPLAY,(MAPWIDTH*TILESIZE)//2+200,((MAPHEIGHT*TILESIZE)+LOWER_MARGIN-60),load)
button_list = make_buttons(tiles)
font = pygame.font.SysFont("ubuntumono", 30)

#User Interface
while True:
    #Update Displays
    DISPLAY.fill(BLACK)
    draw_grid()
    draw_text(f"Screen: {CurrentX}{CurrentY}", font, WHITE, 10, 730)
    draw_text("Left/Right/Up/Down to Change Screens", font, WHITE, 10, 760)
    savebtn.draw()
    loadbtn.draw()
    #Save and Load Data
    if savebtn.IsPressed():
        print("Now Saving...")
        with open(f"map/Screen{CurrentX}{CurrentY}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter= ",")
            for row in TestScreen.screen:
                writer.writerow(row)
        print("Save Complete!")
    if loadbtn.IsPressed():
        print("Now Loading...")
        with open(f"map/Screen{CurrentX}{CurrentY}.csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter= ",")
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    TestScreen.screen[x][y] = int(tile)
    #Checks for Button Presses
    button_count = 0
    for button_count, i in enumerate(button_list):
         i.draw()
         if i.IsPressed():
            current_tile = button_count
    pygame.draw.rect(DISPLAY,RED, button_list[current_tile].rect, 3)
    #Checks Mouse Position
    pos = pygame.mouse.get_pos()
    x = pos[0] // TILESIZE
    y = pos[1] // TILESIZE
    #Check if Mouse is within Map
    if pos[0] < (MAPWIDTH * TILESIZE) and pos[1] < (MAPHEIGHT * TILESIZE):
        if pygame.mouse.get_pressed()[0] == 1:
                if TestScreen.screen[y][x] != current_tile:
                    TestScreen.screen[y][x] = current_tile
    #Event Handler
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and CurrentX != 1:
                CurrentX = CurrentX - 1
            if event.key == pygame.K_RIGHT and CurrentX != 9:
                CurrentX = CurrentX + 1
            if event.key == pygame.K_UP and CurrentY != 9:
                CurrentY = CurrentY + 1
            if event.key == pygame.K_DOWN and CurrentY != 1:
                CurrentY = CurrentY - 1
    for row in range(MAPHEIGHT): #Rows
        for col in range(MAPWIDTH): #Columns
            #pygame.draw.rect(DISPLAY,TestScreen.TileColor[TestScreen.map1[row][col]],(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
            DISPLAY.blit(TestScreen.TileColor[TestScreen.screen[row][col]],(col*TILESIZE,row*TILESIZE))
    #Update Display
    draw_grid()
    pygame.display.update()