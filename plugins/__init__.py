from ecs import Plugin, SystemManager

from .ball_plugin import BallPlugin
from .physics_plugin import PhysicsPlugin
from .render_plugin import RenderPlugin
from .wall_plugin import WallPlugin

def init(system_manager: SystemManager):
    plugins: list[Plugin] = [BallPlugin(), PhysicsPlugin(), WallPlugin(), RenderPlugin()]
    for plugin in plugins:
        plugin.build(system_manager)