from pygame import Surface

from components import Circle, Color, Position, Velocity
from constants import BLUE, RED
from ecs import EntityManager, Plugin, SystemManager

class BallPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_setup_systems(self._setup_ball)

    def _setup_ball(self, _: Surface, entity_manager: EntityManager):
        ball_entity = entity_manager.create_entity("Ball_1")
        ball_entity.add_components(Color(RED), Position(100, 100), Circle(radius=16), Velocity(1, 1))
        ball_entity = entity_manager.create_entity("Ball_2")
        ball_entity.add_components(Color(BLUE), Position(200, 200), Circle(radius=24))