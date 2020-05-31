# ramen added multipurpose screen

screen scene_overlay(img):
    add img xpos 0 ypos 0

screen hbox_line(what, value, field_width=180, fa=0.0, va=1.0):

    hbox:
        text str(what) text_align fa xalign fa min_width field_width
        text str(value) text_align va xalign va

screen hbox_label(what, value, field_width=180, fa=0.0, va=1.0):

    hbox:
        label str(what):
            xsize field_width
            xalign fa
            text_xalign fa
            text_min_width field_width

        text str(value) text_align va xalign va xoffset 16
