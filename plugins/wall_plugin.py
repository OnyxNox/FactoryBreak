from pygame import Surface

from components import Color, Position, Rectangle
from constants import WALL_H_WIDTH, WALL_THICKNESS, WALL_V_WIDTH, WHITE, WINDOW_HEIGHT, WINDOW_WIDTH
from ecs import EntityManager, Plugin, SystemManager

class WallPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_setup_systems(self._setup_walls)

    def _setup_walls(self, _: Surface, entity_manager: EntityManager):
        center_x, center_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        wall_h_center, wall_v_center = WALL_H_WIDTH // 2, WALL_V_WIDTH // 2
        left_anchor, right_anchor = center_x - wall_h_center, center_x + wall_h_center - WALL_THICKNESS
        top_anchor, bottom_anchor = center_y - wall_v_center, center_y + wall_v_center - WALL_THICKNESS

        wall_entity = entity_manager.create_entity("Wall_Left")
        wall_entity.add_components(
            Color(WHITE),
            Position(left_anchor, top_anchor),
            Rectangle(size=(WALL_THICKNESS, WALL_V_WIDTH)),
        )
        wall_entity = entity_manager.create_entity("Wall_Right")
        wall_entity.add_components(
            Color(WHITE),
            Position(right_anchor, top_anchor),
            Rectangle(size=(WALL_THICKNESS, WALL_V_WIDTH)),
        )
        wall_entity = entity_manager.create_entity("Wall_Top")
        wall_entity.add_components(
            Color(WHITE),
            Position(left_anchor, top_anchor),
            Rectangle(size=(WALL_H_WIDTH, WALL_THICKNESS)),
        )
        wall_entity = entity_manager.create_entity("Wall_Bottom")
        wall_entity.add_components(
            Color(WHITE),
            Position(left_anchor, bottom_anchor),
            Rectangle(size=(WALL_H_WIDTH, WALL_THICKNESS)),
        )