import logging
from pygame import Surface

from components import Collider, Position, Velocity
from constants import PINK
from ecs import EntityManager, Plugin, SystemManager

class PhysicsPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        """"""
        system_manager.add_update_systems(self._apply_velocity, self._check_collision)

    def _apply_velocity(self, _: Surface, entity_manager: EntityManager):
        """
        Moves entities based on their Velocity component.
        """
        for position, velocity in entity_manager.query(Position, Velocity):
            position.x += velocity.x
            position.y += velocity.y

    def _check_collision(self, _: Surface, entity_manager: EntityManager):
        """
        Checks for collisions between moving entities and other entities with a Collider component.
        """
        move_collider, move_position, move_velocity = entity_manager.first(Collider, Position, Velocity)

        static_components = (components for components in entity_manager.query(Collider, Position) if components[0] != move_collider)

        for static_collider, static_position in static_components:
            if (static_position.x < move_position.x + move_collider.shape.radius and
                static_position.x + static_collider.shape.width > move_position.x and
                static_position.y < move_position.y + move_collider.shape.radius and
                static_position.y + static_collider.shape.height > move_position.y
            ):
                move_velocity.x, move_velocity.y = 0, 0