#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui


class ImageItem(QtGui.QGraphicsPixmapItem):
    def __init__(self, pixmap, parent=None, scene=None):
        super().__init__()
        self.pixmap = pixmap
        self.setPixmap(self.pixmap)


class View(QtGui.QGraphicsView):
    def __init__(self, size=None, scene=None,
                 parent=None):
        QtGui.QGraphicsView.__init__(self, scene, parent)
        if size is not None:
            self.setFixedSize(*size)
        # резиновая нить
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.setStyleSheet("""
        .QGraphicsView  {
            border: 20px solid black;
            }
        """)

class Scene(QtGui.QGraphicsScene):
    def __init__(self, parent, *__args):
        super().__init__(*__args)



