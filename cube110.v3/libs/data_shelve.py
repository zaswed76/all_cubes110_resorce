#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import shelve
import paths
# from libs.image_geometry import ImageGeometry





#
# if __name__ == '__main__':
#     data_path = os.path.join(paths.root,
#                              r"data\cls_shl\secondary_geometry_shl")
#
#
#     geometry_img = {}
#     data = shelve.open(data_path)
#     geometry_img["0"] = data["0"]
#
#     # изменяем
#     print(geometry_img["0"].x)
#     geometry_img["0"].x = 45.0
#
#     # сохраняем
#     data["0"] = geometry_img["0"]
#     print(data["0"].x)


class Shl(dict):
    def __init__(self, data_path):
        super().__init__()
        self.data_path = data_path
        self.data = None

    def load(self):
        self.data = shelve.open(self.data_path)
        self.update(self.data)

    def save(self, name):
        self.data[name] = self[name]
        self.data.sync()


    def __setitem__(self, key, value):
        print("!!")
        dict.__setitem__(self, key, value)

data_path = os.path.join(paths.root,
                             r"data\cls_shl\secondary_geometry_shl")

s = Shl(data_path)
s.load()
print(s["0"].x )
s["0"].x = 33.3
s.save("0")










