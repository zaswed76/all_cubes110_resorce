#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from PyQt4 import QtGui, QtCore

from functools import partial

EXT_ICON = ".png"
path_temp_icon = "/home/serg/project/cube2015/resources/icons/mnext.png"

class FRAME(QtGui.QWidget):
    def __init__(self, parent=None):
        super().__init__()



class Button(QtGui.QPushButton):
    def __init__(self, icon):
        QtGui.QPushButton.__init__(self)
        self.setIcon(QtGui.QIcon(icon))
        self.setIconSize(QtCore.QSize(27, 27))
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Minimum)
        self.setSizePolicy(sizePolicy)
        self.setCursor(QtCore.Qt.PointingHandCursor)

class GameTool(FRAME):
    def __init__(self, parent, icon_dir):
        super().__init__()
        self.parent = parent
        self.icon_dir = icon_dir
        self.box = QtGui.QHBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)
        self.but_tool = {}
        self.names = ("mnext", "redo", "user_test", "mhelp")
        self.add_but()

    def add_but(self):
        for name in self.names:
            icon_path = os.path.join(self.icon_dir, name + EXT_ICON)
            i = os.path.normpath(icon_path)

            self.but_tool[name] = Button(i)
            self.but_tool[name].pressed.connect(
                partial(self.meth, name))
            self.box.addWidget(self.but_tool[name])

    def meth(self, name):
        self.parent.meth_tool(name)