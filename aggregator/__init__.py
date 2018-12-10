import serial
import sys
from db.mappers import MeasurementMapper
from db.utils import CassandraUtils

ser = serial.Serial('/dev/ttyACM0', 9600)
CassandraUtils.init_connection()

while True:
    read_serial = ser.readline()

    if read_serial:
        measurement_mapper = MeasurementMapper()
        measurement_entity = measurement_mapper.map_raw_input_to_entity(
            read_serial)
        measurement_entity.save()
