import sys
import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Factory Breakout")

clock = pygame.time.Clock()

GREY = (13, 13, 13)

is_running = True
while is_running:
    screen.fill(GREY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)