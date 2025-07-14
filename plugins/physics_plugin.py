from pygame import Surface

from components import Circle, Collider, Position, Rectangle, Velocity
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
        Checks for collisions between all entities with a Collider component.
        """
        moving_components = list(entity_manager.query(Collider, Position, Velocity))
        static_components = list(entity_manager.query(Collider, Position))

        for move_collider, move_position, move_velocity in moving_components:
            for static_collider, static_position in static_components:
                if move_collider is static_collider:
                    continue

                if isinstance(move_collider.shape, Circle):
                    move_width = move_height = move_collider.shape.radius
                elif isinstance(move_collider.shape, Rectangle):
                    move_width, move_height = move_collider.shape.width, move_collider.shape.height
                else:
                    continue

                if isinstance(static_collider.shape, Circle):
                    static_width = static_height = static_collider.shape.radius
                elif isinstance(static_collider.shape, Rectangle):
                    static_width, static_height = static_collider.shape.width, static_collider.shape.height
                else:
                    continue

                if (static_position.x < move_position.x + move_width and
                    static_position.x + static_width > move_position.x and
                    static_position.y < move_position.y + move_height and
                    static_position.y + static_height > move_position.y
                ):
                    move_velocity.x, move_velocity.y = 0, 0