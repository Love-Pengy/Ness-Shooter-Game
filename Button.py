import pygame
import sys

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x,y)
    
    def draw(self):
        # Draws a Button
        pos = pygame.mouse.get_pos() #Get mouse position
        if self.rect.collidepoint(pos):
            print("Mouse Over")
        DISPLAY.blit(self.image, self.rect)
TILESIZE = 40
MAPWIDTH = 45
MAPHEIGHT = 24
btn = pygame.image.load("tiles/2.png")

pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
BtnCheck = Button((MAPWIDTH * TILESIZE) // 2 - 50, (MAPHEIGHT * TILESIZE) // 2 + 100,btn)
while True:
    BtnCheck.draw()
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()