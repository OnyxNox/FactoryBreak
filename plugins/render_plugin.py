import pygame
from pygame import Surface

from components import Circle, Color, Position, Rectangle, Shape
from ecs import EntityManager, Plugin, SystemManager

class RenderPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_setup_systems(self._update_render)
        system_manager.add_update_systems(self._update_render)

    def _update_render(self, screen: Surface, entity_manager: EntityManager):
        for circle, color, position in entity_manager.query(Circle, Color, Position):
            pygame.draw.circle(screen, color.color, (int(position.x), int(position.y)), circle.radius)
        for rectangle, color, position in entity_manager.query(Rectangle, Color, Position):
            pygame.draw.rect(screen, color.color, (int(position.x), int(position.y), *rectangle.size))