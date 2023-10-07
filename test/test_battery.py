import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):

    def test_needs_service(self):
        today = datetime.today().date()
        self.assertTrue(NubbinBattery(today.replace(year=today.year-5), today).needs_service())

    def test_does_not_need_service(self):
        today = datetime.today().date()
        self.assertFalse(NubbinBattery(today.replace(year=today.year-3), today).needs_service())


class TestSpindlerBattery(unittest.TestCase):

    def test_needs_service(self):
        today = datetime.today().date()
        self.assertTrue(SpindlerBattery(today.replace(year=today.year-3), today).needs_service())

    def test_does_not_need_service(self):
        today = datetime.today().date()
        self.assertFalse(SpindlerBattery(today.replace(year=today.year-1), today).needs_service())


if __name__ == "__main__":
    unittest.main()
