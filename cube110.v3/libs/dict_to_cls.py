#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import paths
import shelve
from libs import image_geometry

path_shelve_dict = os.path.join(paths.root,
                                "data/dict_shl/secondary_geometry_shl")

path_shelve_cls = os.path.join(paths.root,
                               "data/cls_shl/secondary_geometry_shl")


def convert():
    db_dict = shelve.open(path_shelve_dict)
    db_cls = shelve.open(path_shelve_cls)
    for key in db_dict:
        x = db_dict[key]["x"]
        y = db_dict[key]["y"]
        scale = db_dict[key]["scale"]
        rotate = db_dict[key]["rotate"]
        mirror = db_dict[key]["mirror"]
        db_cls[key] = image_geometry.ImageGeometry(key,
                                                   x,
                                                   y,
                                                   scale,
                                                   rotate,
                                               mirror)
    db_dict.close()
    db_cls.close()


convert()