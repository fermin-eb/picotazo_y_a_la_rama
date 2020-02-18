from unittest import TestCase

from picotazo_y_a_la_rama.temperature import (
    Temperature,
    TemperatureNegativeException
)

from picotazo_y_a_la_rama.temperature_test_class import TemperatureTestClass


class TestTemperatureTest(TestCase):

    def test_trytoCreateANonValidTemperature(self):
        with self.assertRaises(TemperatureNegativeException):
            Temperature.take(-1)

    def test_tryToCreateAValidTemperature(self):
        measure = 18
        self.assertEqual(
            measure,
            (Temperature.take(measure)).measure()
        )

    def test_trytoCreateAValidTemperatureWithNamedConstructor(self):
        measure = 18
        self.assertEqual(
            measure,
            (Temperature.take(measure)).measure()
        )
