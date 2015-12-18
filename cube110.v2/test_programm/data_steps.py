#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from collections import OrderedDict
from libs import data_service
from paths import root
from test_programm.step import Step

left_data_geometry_path = "user_geometry.json"
right_data_geometry_path = "user_geometry.json"

data = data_service.JsonData(os.path.join(root, "data/models/json"),
                             left_data_geometry_path)
data.reload()

steps = OrderedDict()

steps[1] = Step(2, info="1.html", game="sort")
steps[1].set_left_images(100, 1000, 1010, 1020, 1030, 1040,
                         1050, 1060, 1070, 1080, 1090)
steps[1].set_right_images()