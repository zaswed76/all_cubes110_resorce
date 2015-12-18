#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from functools import partial


class View(QtGui.QGraphicsView):
    def __init__(self, scene=None,
                 parent=None, allpath=None, log=None):
        """


        @type self: object
        @type allpath: object
        """
        QtGui.QGraphicsView.__init__(self, scene, parent)