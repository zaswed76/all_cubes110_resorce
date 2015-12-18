#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
from gui.ImageModel import View, Scene, Setting, ImageItem
from libs import data_service
from paths import root

IMG_DIR = os.path.join(root, "resources/image")
IMG_DIR_SELECT = os.path.join(root, "resources/image_select")

# Setting.set_rotate_mod(Setting, 29)
# Setting.set_scale_mod(Setting, 0.1)


class BaseWindow(QtGui.QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.setFixedSize(*self.size)
        self.data = data_service.JsonData("../data/models/json", "user_geometry.json")
        self.data.reload()
        self.view = View()
        self.scene = Scene(scene_geometry, IMG_DIR, IMG_DIR_SELECT,
                           ext,
                       parent=self, press_method=self.press_image,
                           geometry_data=self.data)
        self.scene.set_edit()


        self.setScene(self.scene)


    # def keyPressEvent(self, QKeyEvent):
    #     if QKeyEvent.modifiers() & QtCore.Qt.ControlModifier:
    #         if QKeyEvent.key() == QtCore.Qt.Key_E:
    #             print(1)
    #             self.scene.set_edit()

    def press_image(self, name):
        self.scene.set_effect(name, "select_change")


if __name__ == '__main__':
    #-------------------------------------------------------------
    size=(604, 604)
    scene_geometry = (0, 0, 600, 600)
    img_dir = os.path.join(root, IMG_DIR)
    ext = ".png"

    app = QtGui.QApplication(sys.argv)
    main = BaseWindow(size)


    #-----------------------------------------------------------------

    main.scene.add_images('0', "7", "5")
    main.show()
    sys.exit(app.exec_())