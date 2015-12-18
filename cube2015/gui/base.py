#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os

from PyQt4 import QtGui, QtCore

import paths
from gui import tool


ERROR_MESSAGE = {"override_method": u"необходимо переопределить этот метод"}

class Error(Exception):
    def init(self, value):
        self.value = value
    def str(self):
        return repr(self.value)



class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.Centr = QtGui.QWidget()
        self.setCentralWidget(self.Centr)

        self.base_box = QtGui.QVBoxLayout(self.Centr)
        self.base_box.setMargin(0)
        self.base_box.setSpacing(0)


    def add_tool(self):
        icon_dir = os.path.join(paths.root, "resources/icons")
        self.tool = tool.GameTool(self, icon_dir)
        self.base_box.addWidget(self.tool)

    def mouse_press_right(self, **kwargs):
        raise Error(u"""нажатие на образ с правой стороны
        {}""".format(ERROR_MESSAGE["override_method"]))

    def mouse_press_left(self, **kwargs):
        raise Error(u"""нажатие на образ с левой стороны
        {}""".format(ERROR_MESSAGE["override_method"]))

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.RightButton:
            raise Exception("""нажатие на пустом поле
            {}""".format(ERROR_MESSAGE["override_method"]))



    def meth_tool(self, name):
        getattr(self, name)()


if __name__ == '__main__':
    css_path = os.path.join(paths.root, "css/style.css")
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    app.setStyleSheet(open(css_path,"r").read())
    main.show()
    main.add_tool()

    sys.exit(app.exec_())