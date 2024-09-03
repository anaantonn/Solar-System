import pygame
import math

class Pluto():
    """Initialize Pluto's attributes."""

    def __init__(self, screen):
        """Initialize the image and it's position"""
        self.screen = screen

        #Load the image.
        self.image = pygame.image.load('images/pluto.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Position the planet relative to the Sun.
        self.center_x = screen.get_rect().centerx
        self.center_y = screen.get_rect().centery

        #Orbit radius.
        self.orbit_radius = 900

        #Initial angle.
        self.angle = 0

        #Create a list to store the coordinates of the planet's movement.
        self.orbit_path = []

    def update_orbit(self):
        """Move the planet on its orbit around the sun."""
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.angle+=0.0009

        self.rect.centerx = self.center_x + self.orbit_radius * math.cos(self.angle)
        self.rect.centery = self.center_y + self.orbit_radius * math.sin(self.angle)
        self.orbit_path.append((self.rect.centerx, self.rect.centery))

        if len(self.orbit_path) > 10000:
            self.orbit_path.pop(0)

        if len(self.orbit_path) > 1:
            pygame.draw.lines(self.screen, 'white', False, self.orbit_path)


    def blitme(self):
        """Draw the image on the screen."""
        self.screen.blit(self.image, self.rect)