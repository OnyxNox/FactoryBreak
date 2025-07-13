from abc import ABC, abstractmethod
import logging
from typing import Callable, Generator, Type

from pygame import Surface

from components import Component, Name

class Entity:
    def __init__(self, id: int):
        """
        Initialize a new Entity instance.
        """
        self._id: int = id
        self._components: dict[Type[Component], Component] = {}

    def add_components(self, *components: Component):
        """
        Add components to the Entity. If a component already exists on the Entity it will be overwritten.
        """
        for component in components:
            component_type = type(component)
            self._components[component_type] = component
            logging.debug(f"Added {component_type.__name__} Component to Entity {self._id}")

    def get_components(self, *component_types: Type[Component]) -> list[Component]:
        """
        Return the Entity's specified components.
        """
        return [self._components[component_type] for component_type in component_types]

    def has_components(self, *component_types: Type[Component]) -> bool:
        """
        Return true if the Entity has all specified components, otherwise false.
        """
        return all(component_type in self._components for component_type in component_types)

class EntityManager:
    def __init__(self):
        """
        Initialize a new EntityManager instance.
        """
        self._entities: list[Entity] = []
        self._next_id: int = 0

    def create_entity(self, name: str | None = None) -> Entity:
        """
        Create and return a new Entity instance. A Name component will be added if provided, otherwise components will
        be empty.
        """
        entity_id = self._next_id
        self._next_id += 1
        entity = Entity(entity_id)
        if name:
            logging.debug(f"Created {name} Entity (ID: {entity_id})")
            entity.add_components(Name(name))
        else:
            logging.debug(f"Created Entity {entity_id}")
        self._entities.append(entity)
        return entity

    def first(self, *component_types: Type[Component]) -> list[Component] | None:
        try:
            return next(self.query(*component_types))
        except StopIteration:
            return None
    
    def query(self, *component_types: Type[Component]) -> Generator[list[Component], None, None]:
        """
        Search and return components grouped by Entity if the Entity has all specified components.
        """
        for entity in self._entities:
            if entity.has_components(*component_types):
                yield entity.get_components(*component_types)

class SystemManager:
    _screen: Surface
    _entity_manager: EntityManager
    _setup_systems: list[Callable]
    _update_systems: list[Callable]

    def __init__(self, screen: Surface, entity_manager: EntityManager):
        """
        Initialize a new SystemManager instance.
        """
        self._screen = screen
        self._entity_manager = entity_manager
        self._setup_systems = []
        self._update_systems = []

    def add_setup_systems(self, *systems: Callable):
        """
        Add setup systems to the SystemManager.
        """
        self._setup_systems.extend(systems)

    def add_update_systems(self, *systems: Callable):
        """
        Add update systems to the SystemManager.
        """
        self._update_systems.extend(systems)

    def run_setup_systems(self):
        """
        Run the setup systems in the SystemManager.
        """
        for setup_system in self._setup_systems:
            setup_system(self._screen, self._entity_manager)

    def run_update_systems(self):
        """
        Run the update systems in the SystemManager.
        """
        for update_system in self._update_systems:
            update_system(self._screen, self._entity_manager)

class Plugin(ABC):
    @abstractmethod
    def build(self, system_manager: SystemManager):
        """
        Initializes the plugin's entities and systems.
        """
        pass