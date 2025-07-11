import pygame
from pygame import Surface

from ecs import EntityManager
from components import Color, Position, Velocity

def render_system(screen: Surface, entity_manager: EntityManager):
    """
    Draw the game.
    """
    radius = 20
    for components in entity_manager.query(Color, Position):
        if components:
            color, position = components
            pygame.draw.circle(screen, color.color, (int(position.x), int(position.y)), radius)

def startup_system(_: Surface, entity_manager: EntityManager):
    """
    Initialize the game.
    """
    ball_entity = entity_manager.create_entity("Ball_1")
    ball_entity.add_components(Color((180, 13, 13)), Position(100, 100), Velocity(1, 1))
    ball_entity = entity_manager.create_entity("Ball_2")
    ball_entity.add_components(Color((13, 13, 180)), Position(200, 200))

def velocity_system(_: Surface, entity_manager: EntityManager):
    """
    Apply velocity to entities.
    """
    for components in entity_manager.query(Position, Velocity):
        if components:
            position, velocity = components
            position.x += velocity.x
            position.y += velocity.y