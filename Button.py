import pygame
import sys

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x,y)
        self.clicked = False

    def draw(self):
        # Draws a Button
        DISPLAY.blit(self.image, self.rect)
    def IsPressed(self):
        action = False
        pos = pygame.mouse.get_pos() #Get mouse position
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action