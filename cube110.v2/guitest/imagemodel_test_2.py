#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
from gui import ImageModel
from libs import data_service
from paths import root

IMG_DIR = "resources/image"

class Image(ImageModel.ImageItem):
    def __init__(self):
        super().__init__()


class Scene(ImageModel.Scene):
    def __init__(self, scene_geometry, image_dir, ext, parent=None,
                 press_method=None, edit=False,
                 img_geometry_path="", *__args):
        super().__init__(scene_geometry, image_dir,
                                            ext, *__args)
        self.img_geometry_path = img_geometry_path
        self.ext = ext
        self.image_dir = image_dir
        self.edit = edit
        self.press_method = press_method
        self.parent = parent




class BaseWindow(ImageModel.View):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.setFixedSize(*self.size)
        self.scene = Scene(scene_geometry, img_dir, ext,
                       parent=self)
        self.scene.set_image_object(Image)
        self.data = data_service.JsonData("../data/models/json", "user_geometry.json")
        self.data.reload()

        self.scene.set_geometry_data(self.data)
        self.scene.set_edit(True)
        self.setScene(self.scene)


    # def mousePressEvent(self, event):
    #    print(self.scene.save_geometry())



if __name__ == '__main__':
    #-------------------------------------------------------------
    size=(604, 604)
    scene_geometry = (0, 0, 600, 600)
    img_dir = os.path.join(root, IMG_DIR)
    ext = ".png"

    app = QtGui.QApplication(sys.argv)
    main = BaseWindow(size)


    #-----------------------------------------------------------------

    main.scene.add_images('0', "1")
    main.show()
    sys.exit(app.exec_())