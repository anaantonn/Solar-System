import pygame

class Sun():
    """Initialize the Sun's attributes."""

    def __init__(self, screen):
        """Iitialize the image and it's position."""
        self.screen = screen

        #Load the image.
        self.image = pygame.image.load('images/sun.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Position the star at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    
    def blitme(self):
        """Draw the image on the screen."""
        self.screen.blit(self.image, self.rect)