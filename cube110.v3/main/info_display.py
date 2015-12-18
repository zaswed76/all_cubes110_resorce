#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui




class InfoDisplay(QtGui.QLabel):
    def __init__(self, parent, size, *__args):
        super().__init__(*__args)
        self.setParent(parent)
        self.width = size[0] * 2
        self.height = size[0]
        self.setFixedSize(self.width, self.height)
        self.setText("""
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        aaaaaaaaaaaaaaaaa
        sssssssssssssssssssssssssssssssssssssssssssssss8888888888888888
        dddddddddddddddddddddddddddddddddddddddddddddddddd88888888888888888888866
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx66666666
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        aaaaaaaaaaaaaaaaa
        sssssssssssssssssssssssssssssssssssssssssssssss8888888888888888
        dddddddddddddddddddddddddddddddddddddddddddddddddd88888888888888888888866
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx66666666
        """)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = InfoDisplay()
    main.show()
    sys.exit(app.exec_())