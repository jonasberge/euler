import importlib.util as importlib
import os
import sys
import uuid

from sys import argv


assert __name__ == '__main__'

if len(argv) < 2: sys.exit('please specify a problem number')
if not argv[1].isdigit(): sys.exit('the problem number needs to be numeric')

problem_number = int(argv[1])
filename = '{}.py'.format(problem_number)
path = os.path.join(os.getcwd(), filename)

module_uuid = uuid.uuid3(uuid.UUID(int=problem_number), 'problem')
module_name = 'p{}-{}'.format(problem_number, module_uuid.bytes.hex())

spec = importlib.spec_from_file_location(module_name, path)
problem = module = importlib.module_from_spec(spec)
spec.loader.exec_module(problem)

# register the module so that it can be imported elsewhere if necessary.
# (e.g. the pickle library can't dump classes that it cannot import)
sys.modules[module_name] = module

problem.solve(*problem.args)

print(module_name)
