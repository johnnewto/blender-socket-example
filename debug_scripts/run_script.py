    # see http://airplanes3d.net/pydev-000_e.xml
import sys
import os
import pydevd_pycharm
from importlib import reload

# SCRIPT      = script to run
# PYDEVD_PATH = path to the pycharm PyDev folder (or other ide) that contains a file named pydevd.py
if os.name in 'nt':
    SCRIPT='C:\\Users\John\\Documents\\git\\Blender_Debug_With_PyCharm\\testdebugx.py'
    PYDEVD_PATH = 'C:\\Program Files\\JetBrains\\PyCharm 2020.1.2\\plugins\\python\helpers\\pydev'
else:
    SCRIPT='/home/john/git/Blender_Debug_With_PyCharm/testdebugx.py' 
    PYDEVD_PATH = '/home/john/pycharm-2019.2.1/helpers/pydev'
    
if sys.path.count(PYDEVD_PATH) < 1: sys.path.append(PYDEVD_PATH)


pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)

script_dir = os.path.dirname(SCRIPT) #directory, where the script is located
script_file = os.path.splitext(os.path.basename(SCRIPT))[0] #script filename, without ".py" extension
if sys.path.count(script_dir) < 1:  sys.path.append(script_dir)

#Emulating Blender behavior: try to unregister previous version of this module 
#(if it has unregister() method at all:)
if script_file in sys.modules:
    try:
        sys.modules[script_file].unregister()
    except:
        pass

    reload(sys.modules[script_file])
else:    
    __import__(script_file) #NOTE: in the script loaded this way, __name__ != '__main__'
#That's why we have to try register its classes:

#Emulating Blender behavior: try to register this version of this module (if it has register() method...)
try:
    sys.modules[script_file].register()
except:
    pass




