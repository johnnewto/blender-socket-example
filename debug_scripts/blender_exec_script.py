#See tips and tricks  https://docs.blender.org/api/current/info_tips_and_tricks.html

import sys
import os
if os.name in 'nt':
    SCRIPT='C:\\Users\John\\Documents\\git\\blender-socket-example\\remote_camera.py'
else:
    SCRIPT='/home/john/git/blender-socket-example/remote_camera.py'

exec(compile(open(SCRIPT).read(), SCRIPT, 'exec'))

#script_dir = os.path.dirname(SCRIPT) #directory, where the script is located
#script_file = os.path.splitext(os.path.basename(SCRIPT))[0] #script filename, without ".py" extension
#if sys.path.count(script_dir) < 1:  sys.path.append(script_dir)

#print(script_dir)

#print(script_file)

#import importlib
#script_file = __import__(script_file)    
##module = importlib.import_module(script_file, package=None)
#importlib.reload(script_file)
#script_file.register()
#script_file.run_modal()
