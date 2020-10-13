import maya.OpenMayaUI as omui
from Pyside2 import QtWidgets
from shiboken2 import wrapInstance


def maya_rain_window():
    """Return the maya main window widget"""
    main_windows = omui.MQUtil.mainWindow()
    

class SimpleUI(QtWidgets.QDialog):
    """Simple UI Class"""

    def __init__(self):
        """Constructor"""
        # Passing the object SimpleUI as an argument to super()
        # makes this ine python 2 and 3 compatible.
        super(SimpleUI, self).__init__()
        self.setWindowTitle("A Simple UI")
