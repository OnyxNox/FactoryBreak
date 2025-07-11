from pygame import Surface

from components import Color, Position, Rectangle
from constants import WHITE
from ecs import EntityManager, Plugin, SystemManager

class WallPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_setup_systems(self._setup_walls)

    def _setup_walls(self, _: Surface, entity_manager: EntityManager):
        wall_entity = entity_manager.create_entity("Wall_Top")
        wall_entity.add_components(Color(WHITE), Position(200, 100), Rectangle(size=(520, 20)))
        wall_entity = entity_manager.create_entity("Wall_Right")
        wall_entity.add_components(Color(WHITE), Position(720, 100), Rectangle(size=(20, 520)))
        wall_entity = entity_manager.create_entity("Wall_Bottom")
        wall_entity.add_components(Color(WHITE), Position(200, 620), Rectangle(size=(520, 20)))
        wall_entity = entity_manager.create_entity("Wall_Left")
        wall_entity.add_components(Color(WHITE), Position(200, 100), Rectangle(size=(20, 520)))