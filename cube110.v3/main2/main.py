#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from main2 import game_display

size_display=(602, 602)
scene_geometry = (0, 0, 600, 600)


class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()

        self.center = QtGui.QWidget()
        self.setCentralWidget(self.center)
        self.scene = abstract_graphics.Scene(self)
        self.view = abstract_graphics.View(size_display, self.scene,
                                           self)
        self.box = QtGui.QHBoxLayout(self.center)
        self.box.addWidget(self.view)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())
