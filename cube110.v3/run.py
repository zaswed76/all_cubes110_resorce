#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui
import paths
from main import game_controll_window

css_path = os.path.join(paths.root, "css/style.css")
app = QtGui.QApplication(sys.argv)
m = game_controll_window.BaseWindow()
app.setStyleSheet(open(css_path, "r").read())
m.show()


sys.exit(app.exec_())
