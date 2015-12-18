#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shelve
from libs import data_service
import paths


class JsonToShelve:
    def __init__(self, json_path, shelve_path):
        self.shelve_path = shelve_path
        self.json_path = json_path

    def get_json_data(self, path):
        data = data_service.JsonData()
        data.load(path)
        return data

    def create_shelve_data(self, json_data, shelve_path):
        dbase = shelve.open(shelve_path)
        dbase.clear()
        dbase.update(json_data)
        dbase.close()

    def convert(self):
        jsondb = self.get_json_data(self.json_path)
        self.create_shelve_data(jsondb, self.shelve_path)


def convert_json_list_to_dict(old_dada_path, new_data_path):
    data = data_service.JsonData()
    data.load(old_dada_path)
    data_dict = {}

    for key in data:
        geometry = {}
        value = data[key]
        geometry["x"] = value[0][0]
        geometry["y"] = value[0][1]
        geometry["scale"] = value[1]
        geometry["rotate"] = value[2]
        try:
            geometry["mirror"] = value[3]
        except IndexError:
            geometry["mirror"] = False
        data_dict[key] = geometry
    data.save(path=new_data_path, obj=data_dict)


if __name__ == '__main__':
    pass
    # path_data1 = os.path.join(paths.root, "data/secondary_geometry.json")
    # path_data_dict1 = os.path.join(paths.root, "data/secondary_geometry_dict.json")
    # convert(path_data1, path_data_dict1)

    path_json_data = os.path.join(paths.root,
                                  r"data\base_geometry_dict.json")
    path_shelve_data = os.path.join(paths.root,
                                    "data/test_shl/secondary_geometry_shl")

    json_to_shl = JsonToShelve(path_json_data, path_shelve_data)
    json_to_shl.convert()


