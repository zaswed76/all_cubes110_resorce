#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from libs import data_service
import paths
dir_name_app = "data/view"
name_app = "app.json"
dir_path_app = os.path.join(paths.root, dir_name_app)


def get_app():
    settings = data_service.JsonData(dir_path_app, name_app)
    settings.reload()
    return settings


if __name__ == '__main__':
    app = get_app()
    print(app)
