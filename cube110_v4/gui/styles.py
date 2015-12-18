#!/usr/bin/env python
# -*- coding: utf-8 -*-

border_view_color = '#b6b6b6'
border_style = 'solid'
border_size = '1px'
background_color = "white"
radius = "1em"



options = dict(size=border_size, style=border_style,
                color=border_view_color,
                bg=background_color, rad=radius)



left_display_css = """
    QGraphicsView {{
    border-right: {size} {style} {color};
    border-left: {size} {style} {color};
    border-top: {size} {style} {color};
    border-bottom: {size} {style} {color};
    background-color: {bg};
    border-top-left-radius: {rad}
     }}
     """.format(**options)


right_display_css = """
    QGraphicsView {{
    border-right: {size} {style} {color};
    border-left: none;
    border-top: {size} {style} {color};
    border-bottom: {size} {style} {color};
    background-color: {bg};
    border-top-right-radius: {rad}
     }}
     """.format(**options)

tool_css = """
    QFrame {{
    border-right: {size} {style} {color};
    border-left: {size} {style} {color};
    border-top: none;
    border-bottom: {size} {style} {color};
    background-color: {bg};
     }}
     """.format(**options)