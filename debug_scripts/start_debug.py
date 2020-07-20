#============================== DEBUG CODE ==================================

# insert this code in an addon or call as command line argument
# The addon directory is at C:\Users\<USER>\AppData\Roaming\Blender Foundation\Blender\2.82\scripts\addons
# Example command line  blender debug.blend --python start_debug.py
import sys
import os

# PYDEVD_PATH = path to the pycharm PyDev folder (or other ide) that contains a file named pydevd.py
if os.name in 'nt':
   PYDEVD_PATH = 'C:\\Program Files\\JetBrains\\PyCharm 2020.1.2\\plugins\\python\helpers\\pydev'
else:
   PYDEVD_PATH = '/home/<USER>/pycharm-2019.2.1/helpers/pydev'

if sys.path.count(PYDEVD_PATH) < 1: sys.path.append(PYDEVD_PATH)
import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True, suspend=False)

#========================================================================
