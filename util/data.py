import inspect
from os import path


DIR = path.dirname(path.abspath(__file__))
DATA_DIR = path.abspath(path.join(DIR, '..', 'data'))


class Data:
    def __init__(self, problem_file=None):
        if not problem_file:
            problem_file = inspect.stack()[-1][1]

        name = path.basename(problem_file)
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
