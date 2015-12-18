#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import time


class StepHelp(QtGui.QLabel):
    ix = 0.7
    def __init__(self, *__args):
        super().__init__(*__args)
        # self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(400, 400)
        self.setWindowOpacity(self.ix)

    def mousePressEvent(self, QMouseEvent):
        self._close()

    def _open(self):
        while self.ix < 1.0:
            self.ix += 0.05
            time.sleep(0.02)
            self.setWindowOpacity(self.ix)
