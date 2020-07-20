# DEBUG = 0 #A debug flag - just for the convinience (Set to 0 in the final version)
#
# ###--- for direct debugging of this add-on (update the pydevd path!) ---------------------------
# if DEBUG == 1:
#     import sys
#     # pydev_path = '/home/john/.p2/pool/plugins/org.python.pydev.core_7.5.0.202001101138/pysrc'
#     pydev_path = '/home/john/pycharm-2019.2.1/helpers/pydev'
#
#     if sys.path.count(pydev_path) < 1: sys.path.append(pydev_path)
#     sys.path.append("/home/john/blender-2.82a")
#     import pydevd
#     pydevd.settrace(stdoutToServer=True, stderrToServer=True, suspend=False) #stop at first breakpoint
# ###-- end remote debug initialization ----------------------------------------------------------

import bpy
import traceback #for error handling
obj = bpy.context.object #active object
# obj2 = bpy.

print("hello there")
for i in range(2):
    print(i)