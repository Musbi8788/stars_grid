import sys
import pygame
from random import randint

from settings import Settings
from stars import Star

class StarGrid():
    """The represent of the star grid design
    """

    def __init__(self,):
        """Initialize the game resources
        """

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)

        self.star = pygame.sprite.Group()

        # create the stars
        self._create_fleet_star()

    def run_game(self):
        """Represent for running the game
        """
        while True:
            self._check_key_event()
            self._update_screen()


    def _check_key_event(self):
        """Reponse the to key press"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_fleet_star(self):
        """Create the fleet of star"""
        # Create a star and find the number of stars in a row
        # The spacing between two star is equal to one star width
        star = Star(self)
        star_width =  star.rect.width
        avaiable_space_x = self.settings.screen_width - (1 * star_width)
        number_cols = avaiable_space_x // (2 * star_width)

        # Determine the number of stars fit in the screen
        star_height = star.rect.height
        available_space_y = self.settings.screen_height - (1 * star_height) 
        number_rows = available_space_y // (2 * star_height)

        # Create full fleet of star
        for num_row in range(number_rows):
            for num_col in range(number_cols):
                self._create_star(num_col, num_row)
    
    def _create_star(self, num_col, num_row):
        """Create star"""
        star = Star(self)
        star_width, star_height = star.rect.size
        rand_x = randint(-10, 10)
        rand_y = randint(-10, 10)
        
        # Star horizontal position
        star.x = rand_x + 2 * star_width * num_col
        star.rect.x = star.x
        
        # Star vertical position
        star.rect.y = rand_y + 2 * star_height * num_row

        self.star.add(star)



    def _update_screen(self):
        """Update the star and show background color"""
        self.screen.fill(self.settings.bg_color) # Show background color
        self.star.draw(self.screen) # Draw star on the screen
        pygame.display.flip()


if __name__ == "__main__":
    """Make an instance and run the game"""
    s_run = StarGrid()
    s_run.run_game()