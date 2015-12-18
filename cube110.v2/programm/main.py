#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

from gui import one_window_game
from models import one_window_model

class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.current_game_window = None

        self.Center = QtGui.QWidget()
        self.setCentralWidget(self.Center)

        self.digit_image_window = one_window_game.View()
        self.digit_image_model = one_window_model.Scene()
        self.digit_image_window.setScene(self.digit_image_model)

    def next_step(self):
        self.current_game_window.next_step()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())