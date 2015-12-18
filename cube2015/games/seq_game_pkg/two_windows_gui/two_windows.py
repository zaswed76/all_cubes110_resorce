#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from games.seq_game_pkg.two_windows_gui import view


class MousePressError(Exception):
    def init(self, value):
        self.value = value

    def str(self):
        return repr(self.value)


class EffectColor(QtGui.QGraphicsColorizeEffect):
    def __init__(self, color):
        super().__init__()
        self.setColor(QtGui.QColor(color))


class ContainerView(QtGui.QWidget):
    u"""
    класс является контейненом для левого и правого окна
    предоставляет api для управления обоими

    """

    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.current_select_object = None
        self.geometry_object = {}
        self.view = {}
        self.scene = {}
        self.box = QtGui.QHBoxLayout(self)

    def set_geometry_object(self, object, side):
        """

        @param object словарь объектов класса ImageModel
        см GeometryObj
        :param side: str имя стороны
        """
        self.geometry_object[side] = object

    def customize(self):
        self.box.setSpacing(self.spacing)
        self.box.setMargin(self.margin)

    def set_appearance(self, **kwargs):
        self.view_size = kwargs["size_view"]
        self.scene_geometry = kwargs["scene_geometry"]
        self.spacing = kwargs["spacing"]
        self.margin = kwargs["margin"]

    def init_view(self, side, mouse_press_method):
        """

        :param side: str "left" or "right"
        :param mouse_press_method: метод обработки нажатия на изображение
        """

        self.view[side] = view.View()
        self.view[side].setFixedSize(*self.view_size)
        self.scene[side] = view.Scene(parent=self.view[side])
        self.scene[side].setSceneRect(*self.scene_geometry)
        self.scene[side].set_press_image(mouse_press_method)
        self.view[side].setScene(self.scene[side])
        self.box.addWidget(self.view[side])

    def draw(self, side, *names):
        """

        :param side: str 'left' or 'right'
        :param names: int (str) имена файлов без расширения
        """
        for n in names:
            self.scene[side].draws(self.geometry_object[side][str(n)])

    def clear_image(self, side, *names):
        for n in names:
            self.scene[side].remove_image(str(n))

    def clear_all(self, side):
        self.scene[side].clear()
        self.scene[side].image_obj.clear()

    @property
    def get_left_images(self):
        images = self.scene["left"].image_obj.keys()
        return images

    @property
    def get_right_images(self):
        images = self.scene["right"].image_obj.keys()
        return images

    def mouse_press_left(self, **kwargs):
        raise MousePressError("необходимо переопределить этот метод")

    def mouse_press_right(self, **kwargs):
        raise MousePressError("необходимо переопределить этот метод")

    def set_effect(self, name, side):
        self.color_effect = EffectColor("#05B542")
        # если есть выделенный объект
        # то снимаем выделение
        if self.current_select_object is not None:
            self.color_effect.setEnabled(False)
            self.current_select_object.setGraphicsEffect(
                self.color_effect)
            self.current_select_object.setOpacity(1.0)

        # и выделяем нажатый
        self.color_effect.setEnabled(True)
        self.scene[side].image_obj[str(name)].setGraphicsEffect(
            self.color_effect)
        self.scene[side].image_obj[str(name)].setOpacity(0.3)
        self.current_select_object = self.scene[side].image_obj[
            str(name)]

    def reset_prev_object(self):
        self.current_select_object = None

    def get_geomety_images(self, side):
        geometry_dict = dict()
        for obj in self.scene[side].image_obj:
            geometry_dict[obj] = self.scene[side].image_obj[
                obj].get_geometry()
        return geometry_dict

    def save_geometry(self, obj, side):
        base_object = self.geometry_object[side].get_json_obj_base
        base_object.update(obj)
        self.geometry_object[side].save_geometry(base_object)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = ContainerView()

    main.show()

    sys.exit(app.exec_())
