#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

def data():
    con = lite.connect('test.db')
    cur = con.cursor()
    cur.execute("SELECT Data FROM Images LIMIT 1")
    return cur.fetchone()[0]