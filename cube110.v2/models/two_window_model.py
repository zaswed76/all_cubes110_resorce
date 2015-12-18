#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui

from gui import ImageModel


class SceneLeft(ImageModel.Scene):
    def __init__(self, method_press=None, parent=None,
                 images_geometry=None):
        QtGui.QGraphicsScene.__init__(self, parent)
        self.image_geometry = images_geometry
        self.method_press = method_press

class SceneRight(ImageModel.Scene):
    def __init__(self, method_press=None, parent=None,
                 images_geometry=None):
        QtGui.QGraphicsScene.__init__(self, parent)
        self.image_geometry = images_geometry
        self.method_press = method_press