#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from main import abstract_graphics as gui
from main import gui_template
from main import style_widgets as style

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

class LeftDisplay(Display):
    def __init__(self, size, scene_geometry):
        super().__init__(size, scene_geometry)



class RightDisplay(Display):
    def __init__(self, size, scene_geometry):
        super().__init__(size, scene_geometry)


class TwoDisplay(QtGui.QWidget):
    def __init__(self, size, scene_geometry, parent=None):
        super().__init__()
        # self.setParent(parent)
        self.scene_geometry = scene_geometry
        self._size = size
        self.box = gui_template.Layout(self)
        self.left_display = LeftDisplay(self._size, self.scene_geometry)
        self.right_display = RightDisplay(self._size, self.scene_geometry)
        self.box.addWidget(self.left_display)
        self.box.addWidget(self.right_display)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    size=(604, 604)
    scene_geometry = (0, 0, 600, 600)
    main = Display(size, scene_geometry)
    main.show()
    sys.exit(app.exec_())