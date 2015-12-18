#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from gui import templates

class ToolBar(QtGui.QFrame):
    def __init__(self, parent, height):
        super().__init__()
        self.parent = parent
        self.setFixedHeight(height)
        self.box = templates.HBoxLayout()

