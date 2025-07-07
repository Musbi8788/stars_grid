import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to manage the star
    """

    def __init__(self, s_game):
        """Initailize the star attributes and the game recourses
        """
        super().__init__()
        self.screen = s_game.screen

        # Load the image and set it rect attributes
        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()

        # Start each new star the right site of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store star's in a horizontal position and convert it to float
        self.x = float(self.rect.x)
