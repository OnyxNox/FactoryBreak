from ecs import Plugin, SystemManager

from .ball_plugin import BallPlugin
from .physics_plugin import PhysicsPlugin
from .render_plugin import RenderPlugin

def init(system_manager: SystemManager):
    plugins: list[Plugin] = [BallPlugin(), PhysicsPlugin(), RenderPlugin()]
    for plugin in plugins:
        plugin.build(system_manager)