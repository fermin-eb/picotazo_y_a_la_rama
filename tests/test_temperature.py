from unittest import TestCase

from picotazo_y_a_la_rama.temperature import (
    Temperature,
)


class TestTemperatureTest(TestCase):

    def test_trytoCreateANonValidTemperature(self):
        with self.assertRaises(Exception):
            Temperature(-1)

    def test_tryToCreateAValidTemperature(self):
        measure = 18
        self.assertEqual(
            measure,
            (Temperature(measure)).measure
        )
