# see http://airplanes3d.net/pydev-000_e.xml
import sys
import os


# SCRIPT      = script to run
# PYDEVD_PATH = path to the pycharm PyDev folder (or other ide) that contains a file named pydevd.py
if os.name in 'nt':
    SCRIPT='C:\\Users\John\\Documents\\git\\Blender_Debug_With_PyCharm\\move_x_by_1.py'
    PYDEVD_PATH = 'C:\\Program Files\\JetBrains\\PyCharm 2020.1.2\\plugins\\python\helpers\\pydev'
else:
    SCRIPT='/home/john/git/Blender_Debug_With_PyCharm/move_x_by_1.py' 
    PYDEVD_PATH = '/home/john/pycharm-2019.2.1/helpers/pydev'

# import pydev_debug  which should be in your SCRIPT directory (or elsewhere if you choose)
pydev_debug_dir = os.path.dirname(SCRIPT)
if sys.path.count(pydev_debug_dir) < 1:  sys.path.append(pydev_debug_dir)  
import pydev_debug as pydev
 
pydev.debug(SCRIPT, PYDEVD_PATH, trace = True)


