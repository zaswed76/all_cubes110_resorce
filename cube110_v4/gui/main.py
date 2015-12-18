#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import paths
from gui import graphics as gui
from gui import templates, styles, tool

from PyQt4 import QtGui

size_display = (602, 602)
height_tool = 35



class BaseWindow(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.left_model = gui.Scene(self)
        self.right_model = gui.Scene(self)
        self.game_display = gui.TwoDisplay(self.left_model,
                                           self.right_model,
                                           size_display)
        self.tool = tool.ToolBar(self, height_tool)
        self.tool.setStyleSheet(styles.tool_css)
        self.box = templates.VBoxLayout(self)
        self.box.addWidget(self.game_display)
        self.box.addWidget(self.tool)





if __name__ == '__main__':
    css_path = os.path.join(paths.get_css_dir(), "base.css")
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open(css_path, "r").read())
    main = BaseWindow()
    main.show()
    img = os.path.join(paths.get_image_dir(), "1.png")
    pxm = QtGui.QPixmap(img)
    item = gui.ImageItem(pxm, scene=main.left_model)
    main.left_model.draw(item)




    sys.exit(app.exec_())