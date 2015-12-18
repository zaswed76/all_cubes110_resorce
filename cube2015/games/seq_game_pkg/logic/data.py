#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import OrderedDict


class Ten(list):
    def __init__(self, key):
        super().__init__()
        self.key = key
        self.init()

    def init(self):
        self.extend(range(self.start, self.end, self.step))

    @property
    def step(self):
        return 1

    @property
    def start(self):
        return self.key + 1

    @property
    def end(self):
        return self.key + 10

    def __add__(self, other):
        if isinstance(other, int):
            self.insert(0, other)
        elif isinstance(other, list):
            self.extend(other)
        else:
            raise Exception(u"надо либо int либо list")

        return self


class TenEmpty(Ten):
    def __init__(self, key):
        super().__init__(key)

    def init(self):
        self.extend(range(-self.start, -self.end, -self.step))


class Key(Ten):
    def __init__(self, key):
        """
        возвращает последовательность с началом key,
        длиной 10,
        шагом 10

        :param key: начало списка
        """
        super().__init__(key)

    @property
    def step(self):
        return 10

    @property
    def start(self):
        return self.key

    @property
    def end(self):
        return self.key + 100

class KeyEmpty(Key):
    def __init__(self, key):
        super().__init__(key)


    def init(self):
        self.extend(range(-self.start, -self.end, -self.step))



seqData = OrderedDict()
seqData[-1] = [
    (Key(1000) + 100, [], "_no_action", 'key_see'),
    (KeyEmpty(1000) + 100, Key(1000), "_sort_game", "sort"),
    (KeyEmpty(1000) + 100, Key(1000), "_revers_game", "revers")
]

seqData[0] = [
    (Ten(0) + 0, []),
    (TenEmpty(0) + 0, Ten(0))
]


if __name__ == '__main__':
    print(Key(1000)) # [1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090]
    print(KeyEmpty(1000)) # [-1000, -1010, -1020, -1030, -1040, -1050, -1060, -1070, -1080, -1090]
    print(Ten(0)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(TenEmpty(0)) # [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    # < + > добавляет в начало списка
    print(Key(1000) + 100) # [100, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090]
