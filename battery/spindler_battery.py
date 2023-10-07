from abc import ABC
from datetime import datetime

from battery import Battery


class SpindlerBattery(Battery, ABC):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.last_service_date.replace(year=self.last_service_date.year + 2) > datetime.today().date():
            return False
        else:
            return True
