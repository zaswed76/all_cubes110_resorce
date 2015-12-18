#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui
import paths
from gui import main

css_path = os.path.join(paths.root, "css/style.css")
app = QtGui.QApplication(sys.argv)
m = main.MainControllerWindow()
app.setStyleSheet(open(css_path,"r").read())
m.show()
m.add_tool()
m.mnext()

sys.exit(app.exec_())
