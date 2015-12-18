#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from libs import data_service
import paths

_Default_Base_geometry = os.path.join(paths.root,
                                      "data/base_geometry.json")
_Default_Secondary_geometry = os.path.join(paths.root,
                                           "data/secondary_geometry.json")


class JsonGeometry(dict):
    def __init__(self, json_file_path):
        """
        класс посредник
        наследует от встроенного типа - dict
        должен содержать три обязательных метода:
            load_data() загрузить данные из файла
            save_data() сохранить данные в файл
            data() получить данные

        :param json_file_path: str путь к json файлу
        """
        super().__init__()
        self.json_file_path = json_file_path
        self.__data = None

    def load_data(self):
        self.__data = data_service.JsonData()
        self.__data.load(self.json_file_path)

    def save_data(self):
        self.__data.save()

    @property
    def data(self):
        return self.__data


if __name__ == '__main__':
    base_data = JsonGeometry(_Default_Base_geometry)
    base_data.load_data()
    print(base_data.data)
    print(base_data.data)
