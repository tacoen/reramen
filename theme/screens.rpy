
init -11 python:

    def ramen_overlay(imgs):
        renpy.show_screen('scene_overlay', imgs=imgs)


# ramen added multipurpose screen

screen scene_overlay(imgs):

    layer 'master'

    python:
        if isinstance(imgs, (str, int, unicode)):
            simg = []
            simg.append(imgs)
        else:
            simg = imgs

    for i in simg:
        python:
            i = ramu.arrayize(i, 3, (0.0, 0.0))

        add i[0] xalign i[1][0] yalign i[1][1] xoffset i[2][0] yoffset i[2][1]


screen scene_overlay_dis(img, align=(0, 0), offset=(0, 0)):
    add img xalign align[0] yalign align[1] xoffset offset[0] yoffset offset[0]

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
