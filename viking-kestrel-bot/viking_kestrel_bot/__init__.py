# Relative import issue. See: https://stackoverflow.com/a/49375740
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
