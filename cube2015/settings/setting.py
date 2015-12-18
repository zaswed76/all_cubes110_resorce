#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import json
import paths

etc_dir = os.path.join(paths.root, "etc")
MAIN_SETTINGS_PATH = os.path.join(etc_dir, "main.json")


class Setting(dict):
    def __init__(self, json_file_path, indent=4, **kwargs):
        super().__init__(**kwargs)
        self.indent = indent
        self.json_file_path = json_file_path


    def read(self):
        self.clear()
        with open(self.json_file_path, "r") as json_obj:
            self.update(json.load(json_obj))

    @property
    def get_json_obj(self):
        return self

    def save(self):
        with open(self.json_file_path, "w") as json_obj:
            json.dump(self, json_obj, indent=self.indent)


if __name__ == '__main__':
    set_main = Setting(MAIN_SETTINGS_PATH)
    set_main.read()
    print(set_main)