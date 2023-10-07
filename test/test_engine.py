import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):

    def test_needs_service(self):
        self.assertTrue(CapuletEngine(0, 30001).needs_service())

    def test_does_not_need_service(self):
        self.assertFalse(CapuletEngine(0, 30000).needs_service())


class TestSternmanEngine(unittest.TestCase):

    def test_needs_service(self):
        self.assertTrue(SternmanEngine(True).needs_service())

    def test_does_not_need_service(self):
        self.assertFalse(SternmanEngine(False).needs_service())


class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service(self):
        self.assertTrue(WilloughbyEngine(0, 60001).needs_service())

    def test_does_not_needs_service(self):
        self.assertFalse(WilloughbyEngine(0, 60000).needs_service())


if __name__ == "__main__":
    unittest.main()
