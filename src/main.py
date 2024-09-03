import pygame
import sys

from sun import Sun
from mercury import Mercury
from venus import Venus
from earth import Earth
from mars import Mars
from jupiter import Jupiter
from saturn import Saturn
from uranus import Uranus
from neptune import Neptune
from pluto import Pluto

def run_animation():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1025))
    pygame.display.set_caption("Solar System")

    clock = pygame.time.Clock()

    sun  = Sun(screen)
    mercury = Mercury(screen)
    venus = Venus(screen)
    earth = Earth(screen)
    mars = Mars(screen)
    jupiter = Jupiter(screen)
    saturn = Saturn(screen)
    uranus = Uranus(screen)
    neptune = Neptune(screen)
    pluto = Pluto(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        sun.blitme()
        mercury.update_orbit()
        venus.update_orbit()        
        earth.update_orbit()        
        mars.update_orbit()        
        jupiter.update_orbit()        
        saturn.update_orbit()        
        uranus.update_orbit()        
        neptune.update_orbit()        
        pluto.update_orbit()        
        
        mercury.blitme()        
        venus.blitme()        
        earth.blitme()
        mars.blitme()
        jupiter.blitme()
        saturn.blitme()
        uranus.blitme()
        neptune.blitme()
        pluto.blitme()
        
        pygame.display.flip()

        clock.tick(120)

run_animation()