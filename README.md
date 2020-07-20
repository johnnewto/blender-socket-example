# blender-socket-example
Using a modal socket with blender to move &amp; control cameras or objects

In Pycharm start Debug Blender-Debug profile remote debugger

<img src="assets/PyCharm-1.png" alt="" width="300"/>

The debug console should show waiting for connection

<img src="assets/PyCharm-2.png" alt="" width="500"/>

Open up a local terminal in pycharm and run the blend batch or bash file

<img src="assets/PyCharm-3.png" alt="" width="500"/>

The Blender debug screen should now show connected

<img src="assets/PyCharm-4.png" alt="" width="500"/>

Run the server.py script. this runs a pygame console

<img src="assets/PyCharm-5.png" alt="" width="500"/>

Then in blender run the blender_exec_script

<img src="assets/PyCharm-6.png" alt="" width="500"/>

This should connect to the server.py socket
Arrow keys pressed in pygame terminal should move the camera view in blender

<img src="assets/PyCharm-7.png" alt="" width="500"/>


