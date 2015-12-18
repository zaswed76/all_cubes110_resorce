#!/usr/bin/env python
# -*- coding: utf-8 -*-

from games.seq_game_pkg.logic import data


class SeqLogic:
    def __init__(self):
        self.game_over = False
        self.global_cursor = -1
        self.local_cursor = 0
        self.date = data.seqData
        self.current_data = None

    def next(self):
        while True:
            seq = self.date[self.global_cursor]
            if self.local_cursor == len(seq):
                self.next_global_cursor()
                self.restart_local_cursor()
                continue


            current_step = seq[self.local_cursor]
            return self.data_parser(current_step)


    def data_parser(self, current_step):
            left, right = current_step[:2]
            try:
                meth = current_step[2]
            except IndexError:
                raise Exception("не указан метод")
            try:
                html_message = current_step[3]
            except IndexError:
                raise Exception("не указан файл подсказки")
            return left, right, meth, html_message

    def get_current_data(self):
        return self.current_data

    def next_local_cursor(self):
        self.local_cursor += 1

    def prev_local_cursor(self):
        self.local_cursor -= 1

    def restart_local_cursor(self):
        self.local_cursor = 0

    def next_global_cursor(self):
        self.global_cursor += 1

if __name__ == '__main__':
    s = SeqLogic()
    print(s.next())
