import sys
assert sys.version_info[0] == 3
assert sys.version_info[1] >= 5

from platform import python_version
assert int(python_version().split(".")[1]) >= 5

from gensim.models import KeyedVectors
from gensim.test.utils import datapath

print("End")