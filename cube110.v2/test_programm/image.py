#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from collections import OrderedDict


class Image:
    _image_dir = None
    _image_select_dir = None
    _ext = None


    def __init__(self, name, geometry):
        self.geometry = geometry
        self.name = str(name)
        self.image_path = None
        self.image_select_path = None

    # def __str__(self):
    #     return "name = {}".format(self.name)

    def set_image_dir(self, dir):
        self._image_dir = dir

    def set_image_select_dir(self, dir):
        self._image_select_dir = dir

    def set_ext(self, ext):
        self._ext = ext

    def set_geometry(self, geometry):
        self.geometry = geometry

    @property
    def get_image_dir(self):
        return self._image_dir

    @property
    def get_image_select_dir(self):
        return self._image_select_dir

    @property
    def get_ext(self):
        return self._ext

    @property
    def get_geometry(self):
        return self.geometry

    @property
    def get_path_image(self):
        return os.path.join(self._image_dir, self.name + self._ext)

    def get_path_select_image(self):
        return os.path.join(self._image_select_dir,
                            self.name + self._ext)


class GroupImage(OrderedDict):
    def __init__(self, image, geometry_data, lst):
        super().__init__()
        self.image = image
        self.lst = lst
        self.geometry_data = geometry_data
        self.init()

    def __getitem__(self, item):
        item = str(item)
        return dict.__getitem__(self, item)

    def init(self):
        for i in self.lst:
            i = str(i)
            obj = self.image(i, self.geometry_data[i])
            self[i] = obj


    # def __str__(self):
    #     return str([x.__str__() for x in self.values()])


if __name__ == '__main__':
    pass
