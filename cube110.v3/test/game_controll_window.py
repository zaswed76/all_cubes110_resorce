#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

class GraphicsView(QtGui.QGraphicsView):
    """
    QGraphicsView(QWidget parent=None)
    QGraphicsView(QGraphicsScene, QWidget parent=None)
    """
    def __init__(self, scene, parent=None, *__args):
        super().__init__(*__args)