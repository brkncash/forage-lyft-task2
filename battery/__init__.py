from abc import ABC, abstractmethod

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class Battery(ABC):

    @abstractmethod
    def needs_service(self):
        pass
