#!/usr/bin/env python
# -*- coding: utf-8 -*-


from guitest import test

a = test.A()
print(a.getx)
test.A.setx(test.A, 100)
a2 = test.A()
print(a2.getx)
b = test.B()

b.disp()