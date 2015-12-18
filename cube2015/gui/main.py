#!/usr/bin/env python
# -*- coding: utf-8 -*-

# todo надо внедрять время

import sys
import os

from PyQt4 import QtGui, QtCore
import paths
from settings import setting
from gui import base
from games.seq_game_pkg.two_windows_gui import two_windows
from games.seq_game_pkg.logic import press_processor, game_logic
from games.seq_game_pkg.logic import geometry
from gui import text_help


class MainControllerWindow(base.BaseWindow):
    side = ["left", "right"]
    set_main = setting.Setting("./etc/main.json")
    set_main.read()
    two_windows_app = {}
    two_windows_app["size_view"] = set_main["size_view"]
    two_windows_app["scene_geometry"] = set_main["scene_geometry"]
    two_windows_app["spacing"] = set_main["spacing"]
    two_windows_app["margin"] = set_main["margin"]

    def __init__(self):
        base.BaseWindow.__init__(self)

        self.seq = game_logic.SeqLogic()
        self.press_processor = press_processor.PressLogic()
        self.geometry = geometry
        self.geometry_object = {}
        self.geometry_object[self.side[0]] = \
            geometry.GeometryObj(
                self.set_main["left_geometry_json"],
                self.set_main["image_dir"],
                self.set_main["ext_images"])

        self.geometry_object[self.side[1]] = \
            geometry.GeometryObj(
                self.set_main["right_geometry_json"],
                self.set_main["image_dir"],
                self.set_main["ext_images"])

        self.geometry_object[self.side[0]].init()
        self.geometry_object[self.side[1]].init()

        self.two_windows = two_windows.ContainerView()
        self.two_windows.set_appearance(**self.two_windows_app)
        self.two_windows.customize()
        self.two_windows.init_view("left", self.mouse_press_left)
        self.two_windows.init_view("right", self.mouse_press_right)

        self.two_windows.set_geometry_object(
            self.geometry_object[self.side[0]], self.side[0])
        self.two_windows.set_geometry_object(
            self.geometry_object[self.side[1]], self.side[1])

        self.step_help = text_help.StepHelp()
        self.step_help.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.step_help.setWindowOpacity(0)
        self.step_help.show()


        self.stck_box = QtGui.QStackedLayout()
        self.base_box.addLayout(self.stck_box)
        self.stck_box.addWidget(self.two_windows)
        self.stck_box.setCurrentIndex(0)

    def mnext(self):
        self.two_windows.reset_prev_object()
        left, right, method, html_message = self.seq.next()
        self.seq.next_local_cursor()
        self.two_windows.clear_all("left")
        self.two_windows.clear_all("right")
        self.two_windows.draw("left", *left)
        self.two_windows.draw("right", *right)
        # назначает имена левой и правой стороны и метод обработки
        self.press_processor.set_current_step(
            self.two_windows.get_left_images,
            self.two_windows.get_right_images,
            method)
        # устанавливает состояние ообъктов согласно текущему состоянию
        self.press_processor.set_condition_step()

    def redo(self):
        self.seq.restart_local_cursor()
        self.mnext()

    def mhelp(self):
        self.step_help._open()

    def mouse_press_right(self, **kwargs):
        name = kwargs["name"]
        meth, name, side = self.press_processor.right_press(name)
        getattr(self, meth)(name, side)

    def mouse_press_left(self, **kwargs):
        name = (kwargs["name"])
        meth, name, side = self.press_processor.left_press(name)
        getattr(self, meth)(name, side)

    def keyPressEvent(self, event):
        if event.matches(QtGui.QKeySequence.Save):
            # dict
            geometry_vis_objects = self.two_windows.get_geomety_images(
                "left")
            self.two_windows.save_geometry(geometry_vis_objects,
                                           "left")

    def user_test(self):
        self.two_windows.view["right"].hide()
        self.setFixedSize(604, 604)

    # ---------------------------------------------------------------------

    def select_image(self, name, side):
        print(name, side, "QQQ")
        self.two_windows.set_effect(name, side)

    def move_right_to_left(self, name, *args):
        self.two_windows.clear_image("left", name)
        self.two_windows.clear_image("right", -int(name))
        self.two_windows.draw("left", -int(name))

    def reset_game(self, *args):
        self.seq.prev_local_cursor()
        self.mnext()

    def none(self, *args):
        print(args, "none")


if __name__ == '__main__':
    css_path = os.path.join(paths.root, "css/style.css")
    app = QtGui.QApplication(sys.argv)
    main = MainControllerWindow()
    app.setStyleSheet(open(css_path, "r").read())
    main.show()
    main.add_tool()
    main.mnext()
    sys.exit(app.exec_())
