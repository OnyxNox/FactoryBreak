from pygame import Surface

from components import Circle, Collider, Position, Rectangle, Velocity
from ecs import EntityManager, Plugin, SystemManager

class PhysicsPlugin(Plugin):
    def build(self, system_manager: SystemManager):
        system_manager.add_update_systems(self._apply_velocity, self._check_collision)

    def _apply_velocity(self, _: Surface, entity_manager: EntityManager):
        for position, velocity in entity_manager.query(Position, Velocity):
            position.x += velocity.x
            position.y += velocity.y

    def _check_collision(self, _: Surface, entity_manager: EntityManager):
        ball, _, ball_position, ball_velocity = entity_manager.first(Circle, Collider, Position, Velocity)

        for _, wall_position, wall in entity_manager.query(Collider, Position, Rectangle):
            if (wall_position.x < ball_position.x + ball.radius and
                wall_position.x + wall.width > ball_position.x and
                wall_position.y < ball_position.y + ball.radius and
                wall_position.y + wall.height > ball_position.y
            ):
                ball_velocity.x, ball_velocity.y = 0, 0