import pygame, sys, csv
import Button, GraphicDesign

#Tracks the various images and 
class TileProperties:
    def __init__(self, TILETYPES):
        self.tile_list = []
        self.IsCollider = []
        self.tile_names = []
        self.Data = open("tiles/TileData.txt")
        for x in range(TILETYPES):
            tile = pygame.image.load(f"tiles/{x}.png")
            tiletransform = pygame.transform.scale(tile,(TILESIZE,TILESIZE))
            self.tile_list.append(tiletransform)
            self.Collision()
        self.Data.close()

 #Running Collision Checks if a tiletype is supposed to have collision and stores it in IsCollider
    def Collision(self):
        CurrentTileProperties = self.Data.readline()
        TileData = CurrentTileProperties.split()
        self.tile_names.append(TileData[0])
        self.IsCollider.append(int(TileData[1]))
class screen(TileProperties):
    def __init__(self, Tile, MAPWIDTH, MAPHEIGHT):
        self.Tiles = Tile.tile_list
        self.IsCollider = Tile.IsCollider
        self.screen = []
        
        for row in range(MAPHEIGHT + 1):
            r = [0] * MAPWIDTH
            self.screen.append(r)
    def load(self,CurrentX,CurrentY):
        print("Now Loading...")
        with open(f'map/Screen{CurrentX}{CurrentY}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.screen[x][y] = int(tile)
        print("Load Complete!")
    def save(self, CurrentX, CurrentY):
        print("Now Saving...")
        with open(f"map/Screen{CurrentX}{CurrentY}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter= ",")
            for row in CurrentScreen.screen:
                writer.writerow(row)
        print("Save Complete!")
#Draws Grid for level editor
def draw_grid():
    for c in range(MAPWIDTH+1):
        pygame.draw.line(DISPLAY, color.WHITE, (c * TILESIZE, 0), (c * TILESIZE, (MAPHEIGHT * TILESIZE)))
    for c in range(MAPHEIGHT+1):
        pygame.draw.line(DISPLAY, color.WHITE, (0, c * TILESIZE), (MAPWIDTH * TILESIZE, (c * TILESIZE)))
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

TILESIZE = 30
TILETYPES = 6
MAPWIDTH = 45
MAPHEIGHT = 24
LOWER_MARGIN = 100
SIDE_MARGIN = 300
color = GraphicDesign.ColorList()
current_tile = 0
CurrentX = 5
CurrentY = 5
#Initialize all our Tiles
tiles = TileProperties(TILETYPES)

#Load in Screen data
CurrentScreen = screen(tiles, MAPWIDTH, MAPHEIGHT)
CurrentScreen.load(CurrentX, CurrentY)

#Create Display
pygame.init()
DISPLAY = pygame.display.set_mode(((MAPWIDTH*TILESIZE) + SIDE_MARGIN ,(MAPHEIGHT*TILESIZE) + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")
DISPLAY.fill(color.LIGHTGREEN)

#Text init
description = GraphicDesign.Text(DISPLAY, "ubuntumono", 30)
tileNames = GraphicDesign.Text(DISPLAY, "ubuntumono", 15)
#Make Buttons
save = pygame.image.load("tiles/save.png")
load = pygame.image.load("tiles/load.png")
savebtn = Button.Button(DISPLAY,(MAPWIDTH*TILESIZE)//2,((MAPHEIGHT*TILESIZE)+LOWER_MARGIN-75),save)
loadbtn = Button.Button(DISPLAY,(MAPWIDTH*TILESIZE)//2+200,((MAPHEIGHT*TILESIZE)+LOWER_MARGIN-60),load)
button_list = make_buttons(tiles)

#User Interface
while True:
    #Update Displays
    DISPLAY.fill(color.LIGHTGREEN)
    draw_grid()
    description.write_text(f"Screen: {CurrentX}{CurrentY}", color.WHITE, 10, 730)
    description.write_text("Left/Right/Up/Down to Change Screens", color.WHITE, 10, 760)
    savebtn.draw()
    loadbtn.draw()
    #Save and Load Data
    if savebtn.IsPressed():
        CurrentScreen.save(CurrentX, CurrentY)
    if loadbtn.IsPressed():
        CurrentScreen.load(CurrentX,CurrentY)
    #Checks for Button Presses
    button_count = 0
    butcol = 0
    butrow = 0
    for button_count, i in enumerate(button_list):
         i.draw()
         tileNames.write_text(tiles.tile_names[button_count], color.BLACK,(MAPWIDTH*TILESIZE) + (75*butcol) + 50, (75 * butrow) + 90)
         butcol += 1
         if butcol == 3:
             butcol = 0
             butrow += 1
         if i.IsPressed():
            current_tile = button_count
    pygame.draw.rect(DISPLAY,color.RED, button_list[current_tile].rect, 3)
    #Checks Mouse Position
    pos = pygame.mouse.get_pos()
    x = pos[0] // TILESIZE
    y = pos[1] // TILESIZE
    #Check if Mouse is within Map
    if pos[0] < (MAPWIDTH * TILESIZE) and pos[1] < (MAPHEIGHT * TILESIZE):
        if pygame.mouse.get_pressed()[0] == 1:
                if CurrentScreen.screen[y][x] != current_tile:
                    CurrentScreen.screen[y][x] = current_tile
    #Event Handler
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Key Press
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
            DISPLAY.blit(CurrentScreen.Tiles[CurrentScreen.screen[row][col]],(col*TILESIZE,row*TILESIZE))
            if CurrentScreen.IsCollider[CurrentScreen.screen[row][col]]:
                        collideRect = CurrentScreen.Tiles[CurrentScreen.screen[row][col]].get_rect()
                        collideRect.x = col * TILESIZE
                        collideRect.y = row * TILESIZE
                        pygame.draw.rect(DISPLAY, color.RED, collideRect,2)
    #Update Display
    draw_grid()
    pygame.display.update()