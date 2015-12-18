#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from gui import main

css_path = "css/style.css"
app = QtGui.QApplication(sys.argv)
m = main.BaseWindow()
app.setStyleSheet(open(css_path, "r").read())
m.show()


sys.exit(app.exec_())