from pygame import Surface

from components import Collider, Color, Position, Rectangle
from constants import WALL_H_WIDTH, WALL_THICKNESS, WALL_V_WIDTH, WHITE, WINDOW_HEIGHT, WINDOW_WIDTH
from ecs import EntityManager, Plugin, SystemManager

class WallPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_setup_systems(self._setup_walls)

    def _create_wall(self, entity_manager: EntityManager, name: str, position: tuple[int, int], size: tuple[int, int]):
        wall_entity = entity_manager.create_entity(name)
        wall_entity.add_components(
            Collider(),
            Color(WHITE),
            Position(*position),
            Rectangle(*size),
        )

    def _setup_walls(self, _: Surface, entity_manager: EntityManager):
        center_x, center_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        wall_h_center, wall_v_center = WALL_H_WIDTH // 2, WALL_V_WIDTH // 2
        left_anchor, right_anchor = center_x - wall_h_center, center_x + wall_h_center - WALL_THICKNESS
        top_anchor, bottom_anchor = center_y - wall_v_center, center_y + wall_v_center - WALL_THICKNESS

        self._create_wall(
            entity_manager,
            name="Wall_Left",
            position=(left_anchor, top_anchor),
            size=(WALL_THICKNESS, WALL_V_WIDTH),
        )
        self._create_wall(
            entity_manager,
            name="Wall_Right",
            position=(right_anchor, top_anchor),
            size=(WALL_THICKNESS, WALL_V_WIDTH),
        )
        self._create_wall(
            entity_manager,
            name="Wall_Top",
            position=(left_anchor, top_anchor),
            size=(WALL_H_WIDTH, WALL_THICKNESS),
        )
        self._create_wall(
            entity_manager,
            name="Wall_Bottom",
            position=(left_anchor, bottom_anchor),
            size=(WALL_H_WIDTH, WALL_THICKNESS),
        )