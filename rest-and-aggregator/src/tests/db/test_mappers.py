import unittest
from src.db.mappers import MeasurementMapper
from src.db.models import Measurement


class TestMeasurementMapper(unittest.TestCase):
    def setUp(self):
        self.measurement_mapper = MeasurementMapper()
        return super().setUp()

    def test_map_raw_input_to_entity_success(self):
        raw_input = 'H:52.00 T:23.00 SMV:0 SMP:100 SL:862\r\n'
        measurement = self.measurement_mapper.map_raw_input_to_entity(
            raw_input)
        self.assertEqual(measurement.air_humidity, 52)
        self.assertEqual(measurement.air_temperature, 23)
        self.assertEqual(measurement.soil_moisture, 0)
        self.assertEqual(measurement.light, 862)
        self.assertIsNotNone(measurement.event_timestamp)
        self.assertIsNotNone(measurement.measurement_id)

    def test_map_raw_input_to_entity_no_sensor_values(self):
        raw_input = ''
        measurement = self.measurement_mapper.map_raw_input_to_entity(
            raw_input)
        self.assertIsNone(measurement.air_humidity)
        self.assertIsNone(measurement.air_temperature)
        self.assertIsNone(measurement.soil_moisture)
        self.assertIsNone(measurement.light)
        self.assertIsNotNone(measurement.event_timestamp)
        self.assertIsNotNone(measurement.measurement_id)

    def test_map_raw_input_to_entity_no__sensor_values_matching(self):
        raw_input = 'HT:52.00 TS:23.00 SMSV:0 SMSP:100 SSL:862\r\n'
        measurement = self.measurement_mapper.map_raw_input_to_entity(
            raw_input)
        self.assertIsNone(measurement.air_humidity)
        self.assertIsNone(measurement.air_temperature)
        self.assertIsNone(measurement.soil_moisture)
        self.assertIsNone(measurement.light)
        self.assertIsNotNone(measurement.event_timestamp)
        self.assertIsNotNone(measurement.measurement_id)

    def test_map_raw_input_to_entity_success_with_exesive_fields(self):
        raw_input = 'H:52.00 T:23.00 SMV:22 SMP:100 SL:862 SDL:862 SDSL:862 SSDL:862\r\n'
        measurement = self.measurement_mapper.map_raw_input_to_entity(
            raw_input)
        self.assertEqual(measurement.air_humidity, 52)
        self.assertEqual(measurement.air_temperature, 23)
        self.assertEqual(measurement.soil_moisture, 22)
        self.assertEqual(measurement.light, 862)
        self.assertIsNotNone(measurement.event_timestamp)
        self.assertIsNotNone(measurement.measurement_id)

    def test_map_measurement_data_to_entity_success(self):
        measurement_data = ["H:52.00", "T:23.00",
                            "SMV:0", "SMP:100", "SL:862"]
        measurement = Measurement()
        self.measurement_mapper._map_measurement_data_to_entity(
            measurement_data, measurement)
        self.assertEqual(measurement.air_humidity, 52)
        self.assertEqual(measurement.air_temperature, 23)
        self.assertEqual(measurement.soil_moisture, 0)
        self.assertEqual(measurement.light, 862)
        self.assertIsNone(measurement.event_timestamp)
        self.assertIsNone(measurement.measurement_id)

    def test_map_measurement_data_to_entity_no_sensor_values(self):
        measurement_data = []
        measurement = Measurement()
        self.measurement_mapper._map_measurement_data_to_entity(
            measurement_data, measurement)
        self.assertIsNone(measurement.air_humidity)
        self.assertIsNone(measurement.air_temperature)
        self.assertIsNone(measurement.soil_moisture)
        self.assertIsNone(measurement.light)
        self.assertIsNone(measurement.event_timestamp)
        self.assertIsNone(measurement.measurement_id)

    def test_map_measurement_data_to_entity_no__sensor_values_matching(self):
        measurement_data = ["HS:52.00", "TS:23.00",
                            "SMSV:0", "SMSP:100", "SSL:862"]
        measurement = Measurement()
        self.measurement_mapper._map_measurement_data_to_entity(
            measurement_data, measurement)
        self.assertIsNone(measurement.air_humidity)
        self.assertIsNone(measurement.air_temperature)
        self.assertIsNone(measurement.soil_moisture)
        self.assertIsNone(measurement.light)
        self.assertIsNone(measurement.event_timestamp)
        self.assertIsNone(measurement.measurement_id)

    def test_map_measurement_data_to_entity_success_with_exesive_fields(self):
        measurement_data = ["H:52.00", "T:23.00",
                            "SMV:0", "SMP:100", "SL:862", "HS:52.00", "TS:23.00",
                            "SMSV:0", "SMSP:100", "SSL:862"]
        measurement = Measurement()
        self.measurement_mapper._map_measurement_data_to_entity(
            measurement_data, measurement)
        self.assertEqual(measurement.air_humidity, 52)
        self.assertEqual(measurement.air_temperature, 23)
        self.assertEqual(measurement.soil_moisture, 0)
        self.assertEqual(measurement.light, 862)
        self.assertIsNone(measurement.event_timestamp)
        self.assertIsNone(measurement.measurement_id)
