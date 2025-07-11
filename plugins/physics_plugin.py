from pygame import Surface

from components import Position, Velocity
from ecs import EntityManager, Plugin, SystemManager

class PhysicsPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_update_systems(self._update_physics)

    def _update_physics(self, _: Surface, entity_manager: EntityManager):
        for components in entity_manager.query(Position, Velocity):
            if components:
                position, velocity = components
                position.x += velocity.x
                position.y += velocity.y