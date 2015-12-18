#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PyQt4 import QtGui, QtCore

NUL_GEOMETRY = 0.0


class Setting:
    rotate_mod = 3
    scale_mod = 0.005

    def get_rotate_mod(self):
        return self.rotate_mod

    def get_scale_mod(self):
        return self.scale_mod

    def set_rotate_mod(self, mod):
        self.rotate_mod = mod

    def set_scale_mod(self, mod):
        self.scale_mod = mod


class EffectColor(QtGui.QGraphicsColorizeEffect):
    def __init__(self, color):
        super().__init__()
        self.setColor(QtGui.QColor(color))


class ImageItem(QtGui.QGraphicsPixmapItem):
    User_rotate = "set_rotate"
    User_increase = "set_scale_increase"
    User_decrease = "set_scale_decrease"
    User_mirror = "mirror"
    User_allow_edit = "allow_edit"
    User_disable_edit = "disable_edit"
    User_ability_change_edit = "ability_change_edit"

    def __init__(self, parent=None, scene=None, press_method=None,
                 path=None, name=None, edit=False, geometry=None,
                 *__args):

        super().__init__(parent, scene)
        self.setting = Setting()
        self.rotate_mod = self.setting.get_rotate_mod()
        self.scale_mod = self.setting.get_scale_mod()
        self.parent = parent
        self.press_method = press_method
        self.name = name
        self.path = path
        self.edit = edit
        self.geometry = geometry
        if geometry is not None:
            self._x = self.geometry[0][0]
            self._y = self.geometry[0][1]
            self._scale = self.geometry[1]
            self._rotate = self.geometry[2]
            try:
                self._mirror = self.geometry[3]
            except IndexError:
                self._mirror = False
        else:
            self._x = NUL_GEOMETRY
            self._y = NUL_GEOMETRY
            self._scale = NUL_GEOMETRY
            self._rotate = NUL_GEOMETRY
            self._mirror = False

        self.setTransformationMode(
            QtCore.Qt.SmoothTransformation)

        self.pixmap = self.get_pixmap(self.path)
        self.move_start()
        self.restart_geometry()
        self.draw()

        if self.edit:
            self.allow_edit()

    def __str__(self):
        return self.name

    def get_pixmap(self, path):
        return QtGui.QPixmap(self.path)

    def draw(self):
        self.setPixmap(self.pixmap)

    def allow_edit(self):
        self.setFlags(
            QtGui.QGraphicsItem.ItemIsMovable | \
            QtGui.QGraphicsItem.ItemIsSelectable)

    def disable_edit(self):
        self.setFlags(QtGui.QGraphicsItem.ItemSendsGeometryChanges)

    def ability_change_edit(self):
        self.edit = not self.edit
        if self.edit:
            self.allow_edit()
        else:
            self.disable_edit()

    @property
    def get_geometry(self):
        x, y = self.pos().x(), self.pos().y()
        scale = self.scale()
        rotate = self._rotate
        mirror = self._mirror
        return [[x, y], scale, rotate, mirror]

    def mousePressEvent(self, event):
        if self.press_method is not None:
            self.press_method(name=self.name)

    def set_geometry_settings(self, x=NUL_GEOMETRY,
                              y=NUL_GEOMETRY,
                              scale=NUL_GEOMETRY,
                              rotate=NUL_GEOMETRY):
        self._x = x
        self._y = y
        self._scale = scale
        self._rotate = rotate

    def restart_geometry(self):
        self.setPos(self._x, self._y)
        self.setScale(self._scale)
        self.setRotation(self._rotate)
        self._load_mirror()

    def _load_mirror(self):
        if self._mirror:
            self.scale(-1, 1)

    @property
    def get_pixmap_size(self):
        width = self.pixmap.size().width()
        height = self.pixmap.size().height()
        return max(width, height)

    def move_start(self):
        size = self.get_pixmap_size
        s = size / 2
        self.setTransformOriginPoint(s, s)

    def set_rotate(self, **kwargs):
        delta = kwargs['delta']
        mod = self.rotate_mod
        if delta < 0:
            mod = -mod
        self._rotate += mod
        self.setRotation(self._rotate)

    def set_scale_increase(self, **kwargs):
        self._scale += self.scale_mod
        self.setScale(self._scale)

    def set_scale_decrease(self, **kwargs):
        self._scale -= self.scale_mod
        self.setScale(self._scale)

    def mirror(self):
        self.prepareGeometryChange()
        self.scale(-1, 1)
        if not self._mirror:
            self.moveBy(self.get_pixmap_size, 0)
            self._mirror = not self._mirror
        else:
            self.moveBy(-self.get_pixmap_size, 0)
            self._mirror = not self._mirror


class View(QtGui.QGraphicsView):
    def __init__(self, size=None, scene=None,
                 parent=None):
        QtGui.QGraphicsView.__init__(self, scene, parent)
        if size is not None:
            self.setFixedSize(*size)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)


class Scene(QtGui.QGraphicsScene):
    # ссылка на QGraphicsPixmapItem объект см set_image_object
    img_obj = ImageItem

    def __init__(self, scene_geometry, image_dir, select_image_dir,
                 ext, parent=None,
                 press_method=None, edit=False, geometry_data=None,
                 img_geometry_path="", *__args):
        """

        :param scene_geometry: tuple (x, y, width, height)
        :param image_dir: str каталог с изображениями
        :param ext: str расщирение рабочих изображений
        :param parent: QGraphicsView
        :param press_method: метод вызываемый при клике на изображение
        :param edit: bool можно ли редактировать
        """

        super().__init__(*__args)

        self.scene_geometry = scene_geometry
        self.image_dir = image_dir
        self.select_image_dir = select_image_dir
        self.ext = ext
        self.parent = parent
        self.press_method = press_method
        self.edit = edit
        self.select_image = None

        self.setSceneRect(*self.scene_geometry)
        # объкты класса ImageItem
        self.image_obj = {}
        # словарь с настройками геометрии изборажений
        if geometry_data is None:
            self.img_geometry_data = dict()
        else:
            self.img_geometry_data = geometry_data
        # выделенный в данный момент объект
        self.current_select_object = None

    def add_image(self, name, **geometry):
        geometry = self.img_geometry_data[name]
        path = Scene._get_path_image(self.image_dir, name, self.ext)
        self.image_obj[name] = self.img_obj(parent=None,
                                            scene=self,
                                            press_method=self.press_method,
                                            path=path,
                                            name=name,
                                            edit=self.edit,
                                            geometry=geometry
                                            )

    def select(self, name, **geometry):
        geometry = self.img_geometry_data[name]
        path = Scene._get_path_image(self.select_image_dir,
                                     name, self.ext)
        self.select_image = self.img_obj(parent=None,
                                            scene=self,
                                            press_method=self.press_method,
                                            path=path,
                                            name=name,
                                            edit=self.edit,
                                            geometry=geometry
                                            )

    def add_images(self, *images_name):
        for name in images_name:
            self.add_image(name)

    def set_image_object(self, image):
        # назначить другой объкт для отрисовки
        self.img_obj = image

    def set_edit(self):
        # можно ли редактировать
        self.edit = not self.edit
        if self.edit:
            self._applied_to_all(ImageItem.User_allow_edit)
        else:
            self._applied_to_all(ImageItem.User_disable_edit)

    def set_press_method(self, method):
        self.press_method = method

    def set_geometry_data(self, data):
        self.img_geometry_data = data

    @property
    def get_geometry_images(self):
        """
        :return: словарь с настройками геометрии видимых объектов
        {'name': [[x, y], scale, rotate, mirror]
        """
        geometry = {}
        for name in self.image_obj:
            geometry[name] = self.image_obj[name].get_geometry
        return geometry


    def save_geometry(self):
        """
        сохраняет настройки в файл
        """
        geometry = self.get_geometry_images
        self.img_geometry_data.update(geometry)
        print("!!!")
        self.img_geometry_data.save()

    def wheelEvent(self, event):
        self._applied_to_selected(ImageItem.User_rotate,
                                  delta=event.delta())

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.modifiers() & QtCore.Qt.ControlModifier:
            if QKeyEvent.key() == QtCore.Qt.Key_Equal:
                self._applied_to_selected(ImageItem.User_increase)

            elif QKeyEvent.key() == QtCore.Qt.Key_Minus:
                self._applied_to_selected(ImageItem.User_decrease)

            elif QKeyEvent.key() == QtCore.Qt.Key_Backslash:
                self._applied_to_selected(ImageItem.User_mirror)

            elif QKeyEvent.key() == QtCore.Qt.Key_S:
                self.save_geometry()

            elif QKeyEvent.key() == QtCore.Qt.Key_E:
                self.set_edit()
                self._applied_to_all(
                    ImageItem.User_ability_change_edit)

    def set_effect(self, name, effect):
        if not self.edit:
            getattr(self, effect)(name)

    def select_change(self, name):
        if self.select_image is None:
            self.select(name)
        else:
            self.select_image.setVisible(False)
            self.select_image = None
            self.select(name)


    def _applied_to_all(self, method, **kwargs):
        obj = self.image_obj
        if obj:
            for i in obj:
                getattr(obj[i], method)(**kwargs)

    def _applied_to_selected(self, method, **kwargs):
        select_obj = self.selectedItems()
        if select_obj:
            for i in select_obj:
                getattr(i, method)(**kwargs)

    @staticmethod
    def _get_path_image(dir, name, ext):
        return os.path.join(dir, name + ext)
