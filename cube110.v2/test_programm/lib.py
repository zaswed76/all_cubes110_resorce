#!/usr/bin/env python
# -*- coding: utf-8 -*-



class SeqParse(list):
    def __init__(self, line=str("")):
        super().__init__()
        self.line = line
        self.parse()

    def parse(self):
        if not self.line:
            self.append([])
        else:
            self.extend(self.line.split("+"))






if __name__ == '__main__':
    s = "100 + (1000, 1090, 10)"
    s2 = "(1000, 1090, 10) + 100"
    s3 = "(1000, 1090, 10)"
    s4 = "100 + 1000"
    s5 = "100 + 130 + 150 + (1000, 1090, 10) + 150"
    s6 = "100"
    s7 = ""

    p = SeqParse(s4)
    print(p)