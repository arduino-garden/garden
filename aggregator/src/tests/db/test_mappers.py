import unittest
from src.db.mappers import MeasurementMapper


class TestMeasurementMapper(unittest.TestCase):

    def test_measurement_mapper_success(self):
        raw_input = 'H:52.00 T:23.00 SMV:0 SMP:100% SL:862\r\n'
        measurement_mapper = MeasurementMapper()
        measurement = measurement_mapper.map_raw_input_to_entity(raw_input)
        self.assertEqual(measurement.air_humidity, 52)
        self.assertEqual(measurement.air_temperature, 23)
        self.assertEqual(measurement.soil_moisture, 0)
        self.assertEqual(measurement.light, 862)
