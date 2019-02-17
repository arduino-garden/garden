from fabric.api import task, run
import os
from src.db.utils import CassandraUtils


@task
def reset():
    CassandraUtils.reset_db()


@task
def start_aggregator():
    os.system('sudo ./env/bin/python3 ./src/start.py')


@task
def start_rest():
    os.system('export FLASK_APP=src/rest_start.py')
    os.system('flask run')


@task
def install():
    with open('./dependencies.txt', 'r') as dependencies_file:
        for line in dependencies_file:
            os.system(line)


@task
def test():
    os.system('python -m pytest')
    # os.system('coverage report -m')


@task
def lint():
    os.system('pylint src/')
