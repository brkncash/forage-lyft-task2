from abc import ABC, abstractmethod

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class Engine(ABC):

    @abstractmethod
    def needs_service(self):
        pass
