import pygame
from pygame import Surface

from components import Circle, Collider, Color, Position, Rectangle, Shape
from constants import PINK
from ecs import EntityManager, Plugin, SystemManager

class RenderPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_setup_systems(self._update_render)
        system_manager.add_update_systems(self._update_render, self._update_debug_render)

    def _update_render(self, screen: Surface, entity_manager: EntityManager):
        for circle, color, position in entity_manager.query(Circle, Color, Position):
            pygame.draw.circle(screen, color.color, (int(position.x), int(position.y)), circle.radius)
        for rectangle, color, position in entity_manager.query(Rectangle, Color, Position):
            pygame.draw.rect(screen, color.color, (int(position.x), int(position.y), *rectangle))

    def _update_debug_render(self, screen: Surface, entity_manager: EntityManager):
        for collider, position in entity_manager.query(Collider, Position):
            if isinstance(*collider, Circle):
                pygame.draw.circle(screen, PINK, (int(position.x), int(position.y)), collider.shape.radius, width=1)
            elif isinstance(*collider, Rectangle):
                pygame.draw.rect(screen, PINK, (int(position.x), int(position.y), *collider.shape), width=1)