#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile
import os
import json



class JsonData(dict):
    def __init__(self):
        super().__init__()
        self._path_json = None


    def load(self, path):
        if not os.path.isfile(path):
            raise Exception("""файла - {} не существует""".format(path))
        else:
            with open(path, "r") as json_obj:
                self.update(json.load(json_obj))
            self._set_path(path)

    def save(self, obj=None, path=None):
        if obj is None: obj = self
        if not isinstance(obj, dict):
            raise Exception("obj может быть только dict")
        if path is None:
            path = self.get_path
        with open(path, "w") as json_obj:
            json.dump(obj, json_obj, indent=4)
        self._set_path(path)

    def new_file(self, path):
        if self.get_path is not None:
            raise Exception("файл уже открыт")

        if os.path.isfile(path):
            raise Exception("""файла - {}
            существует""".format(path))
        else:
            obj = {}
            with open(path, "w") as json_obj:
                json.dump(obj, json_obj, indent=4)
            self._set_path(path)


    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise Exception("{} - нужна только строка".format(key))
        dict.__setitem__(self, key, value)

    def __getitem__(self, item):
        item = str(item)
        return dict.__getitem__(self, item)

    @property
    def get_path(self):
        return self._path_json

    def _set_path(self, path):
        self._path_json = path



if __name__ == '__main__':
    import paths
    path = os.path.join(paths.root, "libs", "test.json")
    path2 = os.path.join(paths.root, "libs", "test2.json")



    def test1():
        obj = JsonData()
        obj.load(path)
        obj["1"] = 10
        obj.save()
        print(obj.get_path)

    def test2():
        obj = JsonData()
        obj.load("аабр")

    def test3():
        # открыть существующий и записать в новый
        obj = JsonData()
        obj.load(path)
        obj["1"] = 10
        obj.save(path=path2)
        print(obj.get_path)

    def test4():
        obj2 = {"5": 55}
        # открыть существующий и записать в новый
        obj = JsonData()
        obj.new_file(path)
        obj["1"] = 100
        obj.save(path=path2, obj=obj2)
        print(obj.get_path)

    def test5():

        # открыть существующий и записать в новый
        obj = JsonData()
        obj.load(path)
        obj["1"] = 100
        obj.save()
        obj.save(path=path2)
        print(obj.get_path)


    test5()






