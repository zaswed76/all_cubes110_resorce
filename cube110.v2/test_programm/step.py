#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from collections import OrderedDict

from libs import data_service
from paths import root
from test_programm.image import Image, GroupImage

left_data_geometry = "user_geometry.json"

data = data_service.JsonData(os.path.join(root, "data/models/json"),
                             left_data_geometry)
data.reload()



Image.set_ext(Image, ".png")
Image.set_image_dir(Image, os.path.join(root, "resources/image"))
Image.set_image_select_dir(Image,
                           os.path.join(root,
                                        "resources/image_select"))


class Step():
    def __init__(self, left_names=None, right_names=None,
                 left_geometry_path=None, right_geometry_path=None):
        self._left_names = left_names
        self._right_names = right_names

    def set_left_images(self, *images):
        self._left_images = GroupImage(Image, self.get_geometry_dada, images)

    @property
    def get_geometry_dada(self):
        return "data"

if __name__ == '__main__':
    pass
