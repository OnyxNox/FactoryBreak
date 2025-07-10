import pygame
from pygame import Surface

from ecs import EntityManager, System
from components import Color, Position

class RenderSystem(System):
    def run(self, screen: Surface, entity_manager: EntityManager):
        """
        Draw the game.
        """
        radius = 20
        for components in entity_manager.query(Color, Position):
            if components != None:
                color, position = components
                pygame.draw.circle(screen, color.color, (int(position.x), int(position.y)), radius)
    
class StartupSystem(System):
    def run(self, _, entity_manager: EntityManager):
        """
        Initialize the game.
        """
        ball_entity = entity_manager.create_entity("Ball_1")
        ball_entity.add_components(Color((180, 13, 13)), Position(100, 100))
        ball_entity = entity_manager.create_entity("Ball_2")
        ball_entity.add_components(Color((13, 13, 180)), Position(200, 200))