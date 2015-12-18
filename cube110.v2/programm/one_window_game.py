#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

from gui import graphicsview


class View(graphicsview.View):
    def __init__(self, scene=None,
                 parent=None):
        graphicsview.View.__init__(self, scene, parent)



if __name__ == '__main__':
    from models import one_window_model
    app = QtGui.QApplication(sys.argv)


    scene = one_window_model.Scene()
    main = View()
    main.setScene(scene)
    main.show()
    sys.exit(app.exec_())