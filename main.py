import sys
import pygame

from constants import GREY, WINDOW_HEIGHT, WINDOW_WIDTH
from ecs import EntityManager, SystemManager
import logger
import plugins

logger.init()
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Factory Breakout")

clock = pygame.time.Clock()

entity_manager = EntityManager()
system_manager = SystemManager(screen, entity_manager)

plugins.init(system_manager)

system_manager.run_setup_systems()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GREY)

    system_manager.run_update_systems()

    pygame.display.flip()
    clock.tick(60)