#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from libs import data_service
from paths import root
from test_programm.image import Image, GroupImage

left_data_geometry = "user_geometry.json"

image = Image

image.set_ext(image, ".png")
image.set_image_dir(image, os.path.join(root, "resources/image"))
image.set_image_select_dir(image,
                         os.path.join(root, "resources/image_select"))

data = data_service.JsonData(os.path.join(root, "data/models/json"),
                             left_data_geometry)
data.reload()


if __name__ == '__main__':
    g = GroupImage(image, data, [1, 2, 3, 7, 4])
    print(g)
