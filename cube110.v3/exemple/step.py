#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from exemple.abstract_graphics import ImageItem


class Image(ImageItem):
    def __init__(self, pixmap, parent=None, scene=None, name=None,
                 geometry=None,
                 ):
        super().__init__(pixmap, parent, scene)
        self.pixmap = pixmap
        self.x = geometry["x"]
        self.y = geometry["y"]
        self.scale = geometry["scale"]
        self.rotate = geometry["rotate"]
        self.mirror = geometry["mirror"]


class Step:
    def __init__(self, left_seq, right_seq, behavior, info):
        """

        :param left_seq: list; имена фотографий без разширений
        :param right_seq: list;
        :param behavior: str; игра (поведедение, что делать при нажатии)
        :param info: str; имя файла html
        """
        self.left_seq = left_seq
        self.right_seq = right_seq
        self.behavior = behavior
        self.info = info

    def get_left_images(self):
        """
        return
        """
        pass
