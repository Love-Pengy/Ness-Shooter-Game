import pygame
DEBUG = 1
#NOTE: .convert_alpha()
image = pygame.image.load("Assets/UIBorders.png")
image = pygame.transform.scale_by(image, 3)

class Game:
    def __init__(self, width, height):
        """
        Start up Pygame and instantiate all
        relevant actors.
        @width : sets width of the screen
        @height : sets height of the screen
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))

        # this allows us to filter the event queue
        # for faster event processing
        pygame.event.set_allowed([
            pygame.QUIT,
            pygame.KEYDOWN
        ])



    def loop(self):
        """
        Primary game loop. This should be
        run perpetually until the game is
        over or is closed.
        """
        self.screen.fill("black")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill("black")
            # first tuple is x,y of where to blit the cropped image , second tuple moves contents of cropped box, third tuple defines dimensions of cropped box


            #this is crop for weapons bar
            self.screen.blit(image, (1500, 900), (2300, 150, 250, 75))
            #this is crop for items bar, currentIdea: put numberes inside of the rings next to the pots
            self.screen.blit(image, (1500, 800), (2125, 425, 300, 75))
            #this is crop for the green deco indicator
            self.screen.blit(image, (1500, 250), (45, 360, 50, 50))
            #this is crop for the blue deco indicator
            self.screen.blit(image, (1450, 250), (95, 360, 47, 50))
            # this is the crop for the red indicator
            self.screen.blit(image, (1400, 250), (145, 360, 47, 50))
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game(1800, 960)
    game.loop()
