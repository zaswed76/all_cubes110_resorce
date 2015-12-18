#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ImageGeometry:
    def __init__(self, name, x, y):
        self._name = name
        self._x = x
        self._y = y
        self.state = []

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        step = ('_x', self._x)
        self.state.append(step)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        step = ('_y', self._y)
        self.state.append(step)
        self._y = value

    def back(self):

        step = self.state.pop()
        print(step, "back")
        self.__dict__[step[0]] = step[1]

    def display(self, atr):
        print(atr, getattr(self, atr), sep=" = ")

if __name__ == '__main__':
    img = ImageGeometry('0', 0, 0)
    print("----------------------\nпо умолчанию")
    img.display("x")
    img.display("y")

    img.x = 99
    img.y = 99
    print(img.state)

    print("----------------------\nизменил")
    img.display("x")
    img.display("y")

    img.back()
    print(img.state)

    print("----------------------\nвернул")
    print(img.x)
    print(img.y)

