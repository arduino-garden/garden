from fabric.api import task, run
import os
from src.db.utils import CassandraUtils


@task
def reset():
    CassandraUtils.reset_db()


@task
def start():
    os.system('sudo ./env/bin/python3 ./src/start.py')


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
