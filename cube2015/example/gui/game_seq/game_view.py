#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class View(QtGui.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedSize(604, 604)
        self.setStyleSheet('background-color: {0};'.format('green'))

class ContainerView(QtGui.QGraphicsView):
    def __init__(self):
        super().__init__()
        box = QtGui.QHBoxLayout(self)
        self.left_view = View()
        self.right_view = View()
        box.addWidget(self.left_view)
        box.addWidget(self.right_view)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = ContainerView()
    main.show()
    sys.exit(app.exec_())