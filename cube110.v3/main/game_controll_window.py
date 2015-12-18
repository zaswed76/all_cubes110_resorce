#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
import paths
from main import gui_template
from main.game_display import TwoDisplay
from main.info_display import InfoDisplay


size_display=(602, 602)
scene_geometry = (0, 0, 600, 600)

class ASWERF(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

class BaseWindow(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.a = ASWERF()
        self.box = QtGui.QHBoxLayout()
        self.box.addWidget(self.a)
        self.game_display = TwoDisplay(size_display, scene_geometry, parent=self)
        # self.info_display = InfoDisplay(self, size_display)
        # # self.layers = [self.game_display, self.info_display]
        #
        #
        #
        #
        #
        #
        # self.box = gui_template.Layout(self)
        # self.layers_box = QtGui.QStackedLayout()
        # self.box.addLayout(self.layers_box)
        #
        # self.layers_box.addWidget(self.game_display)
        # self.layers_box.addWidget(self.info_display)
        # self.layers_box.setCurrentIndex(0)
        # self.setLayout(self.box)

    #
    #
    # def keyPressEvent(self, QKeyEvent):
    #     if  self.s == 0:
    #          self.s = 1
    #     else:
    #          self.s = 0
    #     if QKeyEvent.key() == QtCore.Qt.Key_E:
    #         self.layers_box.setCurrentIndex(self.s)




if __name__ == '__main__':
    style_path = os.path.join(paths.root, "css", "style.css")
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(open('{}'.format(style_path), "r").read())
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())
