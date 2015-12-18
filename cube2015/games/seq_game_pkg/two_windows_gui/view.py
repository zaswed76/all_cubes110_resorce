#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui, QtCore

MASS = True
MOVE = True


def pass_method(*arg, **args):
    pass


class Element(QtGui.QGraphicsPixmapItem):
    def __init__(self, parent=None, scene=None,
                 meth_press=None, img_obj=None):

        QtGui.QGraphicsPixmapItem.__init__(self, parent,
                                           scene)

        self.meth_press = meth_press
        self.img_obj = img_obj
        self._rotate = self.img_obj.rotate
        self._x = self.img_obj.x
        self._y = self.img_obj.y
        self._scale = self.img_obj.scale
        self._path = self.img_obj.path

        self.setTransformationMode(
            QtCore.Qt.SmoothTransformation)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        if MOVE:
            self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
            self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)

        self.move_start()
        self.setPos(self._x, self._y)
        self.setScale(self._scale)
        self.setRotation(self._rotate)
        self.setPixmap(QtGui.QPixmap(self._path))


    def user_rotate(self, delta):
        mod = 3
        if delta < 0:
            mod *= -1
        self._rotate += mod
        self.setRotation(self._rotate)

    def move_start(self):
        s = (self.scale() * 459) / 2
        self.setTransformOriginPoint(s, s)

    def mousePressEvent(self, event):
        self.meth_press(name=self.img_obj.name)

    def get_geometry(self):
        x, y = self.pos().x(), self.pos().y()
        scale = self.scale()
        return [[x, y], scale, self._rotate]


class Scene(QtGui.QGraphicsScene):
    def __init__(self, method_press=None, parent=None):
        """

        :type method_press: parent method or pass_method
        """
        QtGui.QGraphicsScene.__init__(self, parent)
        if method_press is None:
            self.method_press = pass_method
        else:
            self.method_press = method_press

        self.current_method = None
        self.image_obj = {}

    def all_selected(self):
        for item in self.image_obj:
            self.image_obj[item].setSelected(True)

    def set_press_image(self, method):
        self.method_press = method

    def get_pos_image(self):
        return self.item2.offset()

    def draws(self, img_object):
        self.image_obj[img_object.name] = Element(None, self,
                                                  self.method_press,
                                                  img_object)

    def remove_image(self, name):
        self.removeItem(self.image_obj[name])
        self.image_obj.pop(name)


class View(QtGui.QGraphicsView):
    def __init__(self, scene=None,
                 parent=None, tool_names=None):
        QtGui.QGraphicsView.__init__(self, scene, parent)



if __name__ == '__main__':
    from games.seq_game_pkg.logic import geometry as imgobj

    path_geometry = "/home/serg/project/cube2015/etc/user_geometry.json"
    print(imgobj.IMAGE_DIR, "d")
    img = imgobj.GeometryObj(path_geometry, imgobj.IMAGE_DIR,
                           imgobj.EXT)
    img.init()
    app = QtGui.QApplication(sys.argv)
    scene = Scene()
    main = View(scene=scene)
    scene.draws(img["0"])
    main.show()
    sys.exit(app.exec_())
