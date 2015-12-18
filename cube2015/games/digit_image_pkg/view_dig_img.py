#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

from functools import partial


class BaseWindow(QtGui.QLabel):
    def __init__(self):
        QtGui.QLabel.__init__(self)
        self.setStyleSheet("""
        background-color: grey; color: white;
        border: 3px solid green;
        border-radius: 5px;
        font-size: 22px;
        """)
        self.setText("AAAAAA")
        self.setFixedSize(602, 602)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())