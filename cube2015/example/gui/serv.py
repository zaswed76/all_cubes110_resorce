#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore


class CentralFrame(QtGui.QFrame):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent)
        self.setFrameShape(QtGui.QFrame.Box)
        # self.setFrameShadow(QtGui.QFrame.Plain)
        self.setLineWidth(1)
        # self.setMidLineWidth(30)
        self.setStyleSheet('color: {0};'.format('#000000'))

    def mousePressEvent(self, event):
        pass
        #print "press"


class LeftButton(QtGui.QLabel):
    def __init__(self, parent=None, image=None):
        QtGui.QLabel.__init__(self, parent)
        self.image = image
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored,
                                       QtGui.QSizePolicy.Ignored)
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet('background-color: {0};'.format('#F2F2F2'))
        self.setScaledContents(True)


class StartButton(QtGui.QLabel):
    def __init__(self, parent=None, image=None):
        QtGui.QLabel.__init__(self, parent)
        img_path = image
        self.parent = parent
        pxm = QtGui.QPixmap(img_path)
        self.setPixmap(pxm)

    def mousePressEvent(self, event):
        self.parent.lab.setVisible(False)


class TestWidget(QtGui.QLabel):
    def __init__(self):
        QtGui.QLabel.__init__(self)
        self.setAlignment(QtCore.Qt.AlignCenter)




if __name__ == '__main__':
    pass