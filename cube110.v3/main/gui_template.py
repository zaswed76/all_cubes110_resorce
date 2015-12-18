#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtCore import QTimeLine


MARGIN = 0
SPACING = 0


class Layout(QtGui.QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMargin(MARGIN)
        self.setSpacing(SPACING)



class FaderWidget(QtGui.QWidget):

    def __init__(self, old_widget, new_widget):

        QtGui.QWidget.__init__(self, new_widget)
        self.pixmap_opacity = 1.0
        self.old_pixmap = QtGui.QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)


        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(1000)
        self.timeline.start()

        self.resize(new_widget.size())
        self.show()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()

    def animate(self, value):
        self.pixmap_opacity = 1.0 - value
        self.repaint()

class StackedWidget(QtGui.QStackedLayout):
    def __init__(self, parent=None, *__args):

        super().__init__(*__args)

    def setCurrentIndex(self, index):
        self.fader_widget = FaderWidget(self.currentWidget(), self.widget(index))
        QtGui.QStackedLayout.setCurrentIndex(self, index)



