import pygame

class Button():
    #initilizes button with image and location specified
    def __init__(self, screen, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x,y)
        self.clicked = False
        self.screen = screen
    
    # Draws a Button
    def draw(self):
        self.screen.blit(self.image, self.rect)
    #checks if pressed ; returns a bool
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
