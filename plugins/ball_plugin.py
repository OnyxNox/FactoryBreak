from pygame import Surface

from components import Circle, Collider, Color, Position, Velocity
from constants import BALL_RADIUS, RED, WINDOW_HEIGHT, WINDOW_WIDTH
from ecs import EntityManager, Plugin, SystemManager

class BallPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_setup_systems(self._setup_ball)

    def _setup_ball(self, _: Surface, entity_manager: EntityManager):
        center_x, center_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2

        ball_entity = entity_manager.create_entity("Ball")
        ball_entity.add_components(
            Circle(BALL_RADIUS),
            Collider(),
            Color(RED),
            Position(center_x, center_y),
            Velocity(1, 1),
        )