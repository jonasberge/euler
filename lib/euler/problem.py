from functools import cached_property
import importlib.util as importlib
import inspect
import os
import uuid

from .definitions import DESK_DIR, DRAWER_DIR, SOLVED_DIR


DIRECTORIES = [
    os.getcwd(),
    DESK_DIR,
    SOLVED_DIR,
    DRAWER_DIR
]


class Script:
    def __init__(self, filename):

        for directory in DIRECTORIES:
            path = os.path.join(directory, filename)
            if os.path.exists(path):
                break
            path = None

        if not path:
            raise Exception("Unable to locate file {}".format(filename))

        self._path = path

    @property
    def path(self):
        return self._path

    @cached_property
    def problem_number(self):
        filename = os.path.basename(self.path)
        number = os.path.splitext(filename)[0]

        try: return int(number)
        except ValueError:
            return None

    @cached_property
    def uuid(self):
        class_name = self.__class__.__name__
        return uuid.uuid3(uuid.UUID(int=self.problem_number), class_name)

    @cached_property
    def module_name(self):
        return 'p{}-{}'.format(self.problem_number, self.uuid.bytes.hex())

    def create_module(self):
        spec = importlib.spec_from_file_location(self.module_name, self.path)
        module = importlib.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module


class Problem:
    def __init__(self, module):
        self._module = module

        if not hasattr(module, 'solve') or not callable(module.solve):
            raise Exception("Module does not have a solve() function")

        if not hasattr(module, 'solution'):
            raise Exception("Module does not have a 'solution' variable")

        if module.solution is not None \
                and not isinstance(module.solution, str):
            raise Exception("The module's solution is required "
                            "to be a string (str) or empty (None)")

        if not hasattr(module, 'args'):
            raise Exception("Module does not have an 'args' variable")

        if not isinstance(module.args, tuple):
            raise Exception("The module's 'args' variable "
                            "is required to be a tuple")

        # TODO: add optional **kwargs

        try:
            inspect.signature(module.solve).bind(*module.args)
        except TypeError as e:
            raise Exception("The module's function signature of solve() is "
                            "not compatible with the values in 'args'") from e

    @property
    def module(self):
        return self._module

    @property
    def solution(self):
        return self.module.solution

    @property
    def solve_function(self):
        return self.module.solve

    @property
    def args(self):
        return self.module.args

    @property
    def is_solved(self):
        return self.solution is not None

    def solve(self):
        return self.solve_function(*self.args)
