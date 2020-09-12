import inspect
from os import path

from .definitions import DATA_DIR


class Data:
    def __init__(self, problem_filename=None):
        if not problem_filename:
            problem_filename = inspect.stack()[-1][1]

        name = path.basename(problem_filename)
        problem = path.splitext(name)[0]

        try:
            self.problem_number = int(problem)
        except ValueError:
            raise Exception('Expected file to be named N.py, '
                            'with N being an integer, got ' + name)

    def read(self, filename):
        problem = str(self.problem_number)
        filename = path.join(DATA_DIR, problem, filename)
        with open(filename, 'r') as file:
            return file.read()


def read_data(filename, problem_filename=None):
    return Data(problem_filename).read(filename)

