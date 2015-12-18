#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class BaseWindow(QtGui.QLabel):
    def __init__(self):
        QtGui.QLabel.__init__(self)

        # -------------------------------------------

        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)

    def next_step(self):
        self.setText()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())