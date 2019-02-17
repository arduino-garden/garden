from flask import Flask
from src.db.models import Measurement
from src.db.utils import CassandraUtils
from src.db.mappers import MeasurementMapper
import json

app = Flask(__name__)

CassandraUtils.init_connection()
measurement_mapper = MeasurementMapper()


@app.route('/measurements')
def all_measuremets():
    measurements = Measurement.objects.all().limit(100)
    measurement_dicts = []
    for measurement in measurements:
        measurement_dict = measurement_mapper.to_dict(measurement)
        measurement_dicts.append(measurement_dict)

    return json.dumps(measurement_dicts)
