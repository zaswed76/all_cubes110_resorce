#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from exemple import abstract_graphics as gui


class Display(gui.View):
    def __init__(self, size, scene_geometry):
        super().__init__()
        self.size = size
        self.setFixedSize(*self.size)

        self.scene = gui.Scene(self)
        self.scene.setSceneRect(*scene_geometry)
        self.setScene(self.scene)

    def draw(self, item):
        self.scene.addItem(item)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    size=(604, 604)
    scene_geometry = (0, 0, 600, 600)
    main = Display(size, scene_geometry)
    main.show()
    sys.exit(app.exec_())