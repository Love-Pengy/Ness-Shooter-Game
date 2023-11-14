import pygame
#Color class so I don't have to clutter the main code with declarations
class ColorList():
    def __init__(self):
        self.RED = (200, 25, 25)
        self.ORANGE = (255,140,0)
        self.YELLOW = (255,215,0)
        self.GREEN = (0,128,0)
        self.LIGHTGREEN = (144, 201, 120)
        self.BLUE = (0,0,255)
        self.PURPLE = (138,43,226)
        self.PINK = (255,105,180)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0,0,0)
#Made a class for outputting text to the screen
class Text:
    def __init__(self,screen,font,size):
        self.screen = screen
        self.font = pygame.font.SysFont(font,size)

    def write_text(self,text,color,x,y):
        img = self.font.render(text, True,color)
        self.screen.blit(img,(x,y))