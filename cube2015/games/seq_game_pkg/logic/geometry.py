#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
geometry.json содережит словарь где ключи str, а значения list
value[0] [x, y] - положение
value[1] scale - коэффициент размера
value[2] rotate - коэффициент поворота
"""

import os
import json


def save_geometry(obj, path):
    with open(path, "w") as json_obj:
        json.dump(obj, json_obj, indent=4)


def get_json_object(path):
    with open(path, "r") as json_obj:
        return json.load(json_obj)


def get_path(name, dir_img, ext):
    if name[0] == "-":
        name = "-1"
    return os.path.join(dir_img,
                        name + "." + ext)


class ImageModel:
    def __init__(self, img_obj):
        self._x, self._y = img_obj[0]
        self._scale = img_obj[1]
        self._rotate = img_obj[2]
        self._name = img_obj[3]
        self._path = img_obj[4]

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def scale(self):
        return self._scale

    @property
    def rotate(self):
        return self._rotate

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path


class GeometryObj(dict):
    u"""
    класс является словарём значения которого - объекты
    класса ImageModel свойства которого хранят параметры изображения
    см. class ImageModel
    """

    def __init__(self, path_geometry, img_dir, ext, **kwargs):
        """

            :param path_geometry:
            :param img_dir:
            :param ext:
            """
        super(GeometryObj, self).__init__(**kwargs)
        self.path_geometry = path_geometry
        self.img_dir = img_dir
        self.ext = ext
        self._json_obj_base = {}

    def init(self):
        """
        прочитать json объект = list
        дополнить полями name, path
        создать объект ImageModel передав созданный список аргументом
        создать ключь словаря (self) присвоив значением объект ImageModel


        """
        self.__read_json_object()
        self.clear()
        for key in self._json_obj_base:
            self._json_obj_base[key].append(key)
            self._json_obj_base[key].append(
                get_path(key, self.img_dir, self.ext))
            self[key] = ImageModel(self._json_obj_base[key])

    def __read_json_object(self):
        self._json_obj_base = get_json_object(self.path_geometry)


    @property
    def get_json_obj_base(self):
        return get_json_object(self.path_geometry)

    def save_geometry(self, obj, path=None):
        if path is None:
            path = self.path_geometry
        save_geometry(obj, path)

if __name__ == '__main__':
    import paths

    direct = os.path.join(paths.root, r"resources\image")
    geometry = os.path.join(paths.root,
                            r"seq_game_pkg\json\user_geometry.json")


    img = GeometryObj(geometry, direct, "png")
    img.init()
    print(img._json_obj_base["-5"])



