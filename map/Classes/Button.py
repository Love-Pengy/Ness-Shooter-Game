import pygame

class Button():
    def __init__(self, screen, x, y, image):
        self.image = image
        try:
            self.rect = self.image.get_rect()
        except:
            self.rect = self.image
        self.rect = self.rect.move(x,y)
        self.clicked = False
        self.screen = screen

    def draw(self):
        # Draws a Button
        try:
            self.screen.blit(self.image, self.rect)
        except:
            pygame.draw.rect(self.screen,"purple",self.rect)
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