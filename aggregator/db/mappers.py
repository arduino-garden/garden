from db.models import Measurement
import time
import uuid

AIR_QUALITY = "AQ"
AIR_HUMIDITY = "H"
AIR_TEMPERATURE = "T"
SOIL_MOISTURE = "SMV"
LIGHT = "SL"


class MeasurementMapper():
    def map_raw_input_to_entity(self, raw_input):
        measurement_data = raw_input.split()

        measurement = Measurement()
        measurement.id = uuid.uuid4()
        measurement.event_timestamp = time.time()
        self._map_measurement_data_to_entity(measurement_data, measurement)
        return measurement

    def _map_measurement_data_to_entity(self, measurement_data, measurement):
        for data in measurement_data:
            data_key_val = data.split(b":")
            sensor_acronym = data_key_val[0].decode('ascii')
            sensor_value = data_key_val[1].decode('ascii')
            print(sensor_acronym)
            if sensor_acronym == AIR_HUMIDITY:
                measurement.air_humidity = int(float(sensor_value))
            if sensor_acronym == AIR_TEMPERATURE:
                measurement.air_temperature = int(float(sensor_value))
            if sensor_acronym == SOIL_MOISTURE:
                measurement.soil_moisture = int(float(sensor_value))
            if sensor_acronym == LIGHT:
                measurement.light = int(float(sensor_value))
