'''Utility for running Blender scripts and addons in pycharm or Eclipse PyDev debugger
Place this file somwhere in a folder that occurs in Blender's sys.path
(You can check the sys.path list in Python Console)
'''
import sys
import os

from importlib import reload

def debug(script, pydev_path, trace=True):
    '''Runs script in PyDev remote debugger
        Arguments:
        @script (string): full path to script file
        @pydev_path (string): full path to the PyDev folder that contains the pydevd.py module. 
                    (Actually this is the *core/pysrc subfolder, but it may vary in the future PyDevs) 
        @trace (bool): whether to start debugging (if not - just run the script)
    '''
    script_dir = os.path.dirname(script) #directory, where the script is located
    script_file = os.path.splitext(os.path.basename(script))[0] #script filename, without ".py" extension
    #update the PYTHONPATH for this script. 
    if sys.path.count(pydev_path) < 1: sys.path.append(pydev_path)
    if sys.path.count(script_dir) < 1:  sys.path.append(script_dir)  
    #NOTE: These paths stay in PYTHONPATH even when this script is finished.
    #try to not use scripts having identical names from different directories!

    import pydevd  # this is found in "pydev_path"
    if trace:
        pydevd.settrace('localhost', stdoutToServer=True, stderrToServer=True, suspend=False, port=5678) #stop at first breakpoint
    # pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)

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
    