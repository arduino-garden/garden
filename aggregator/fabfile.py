from fabric.api import task, run
import os
from db.utils import CassandraUtils


@task
def reset():
    CassandraUtils.reset_db()


@task
def start():
    os.system('sudo ./env/bin/python3 __init__.py')


@task
def install():
    with open('./dependencies.txt', 'r') as dependencies_file:
        for line in dependencies_file:
            os.system(line)


@task
def test():
    pass


@task
def lint():
    pass
