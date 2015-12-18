#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
from functools import partial
from edit_scr import settings
from gui.ImageModel import View, Scene, Setting, ImageItem

app = settings.app()

class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.data = json_service.Data("../data/models/json", "user_geometry.json")

        self.Centr = QtGui.QWidget()
        self.setCentralWidget(self.Centr)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())
