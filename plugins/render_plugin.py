import pygame
from pygame import Surface

from components import Color, Position, Velocity
from ecs import EntityManager, Plugin, SystemManager

class RenderPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_setup_systems(self._update_render)
        system_manager.add_update_systems(self._update_render)

    def _update_render(self, screen: Surface, entity_manager: EntityManager):
        radius = 20
        for components in entity_manager.query(Color, Position):
            if components:
                color, position = components
                pygame.draw.circle(screen, color.color, (int(position.x), int(position.y)), radius)