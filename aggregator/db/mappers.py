from db.models import Measurement
import time
import uuid


class MeasurementMapper():
    def map_raw_input_to_entity(self, raw_input):
        print(raw_input)

        measurement = Measurement()
        measurement.id = uuid.uuid4()
        measurement.event_timestamp = time.time()

        return measurement
