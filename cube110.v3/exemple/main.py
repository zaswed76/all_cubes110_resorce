#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from functools import partial
from exemple.controller_graphics import Display
from exemple import abstract_graphics as gui

size_display=(604, 604)
scene_geometry = (0, 0, 600, 600)

class ImageModel(gui.ImageItem):
    def __init__(self, pixmap, parent=None, scene=None):
        super().__init__(pixmap, parent, scene)

class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.display_left = Display(size_display, scene_geometry)
        self.display_right = Display(size_display, scene_geometry)

        self.center = QtGui.QWidget()
        self.setCentralWidget(self.center)
        self.box = QtGui.QHBoxLayout(self.center)
        self.box.addWidget(self.display_left)
        self.box.addWidget(self.display_right)


if __name__ == '__main__':
    path = r"1.png"


    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    item = ImageModel(QtGui.QPixmap(path))
    main.display_left.draw(item)

    sys.exit(app.exec_())