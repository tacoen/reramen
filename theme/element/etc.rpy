# ramen multipurpose screen

init offset= -20

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

screen story_skipbutton(label, text='Skip'):
    zorder 199
    layer 'dialog_layer'
    textbutton text style 'ramen_button_medium' xalign 0.975 yalign 0.95:
        background "#456"
        text_size 20
        hover_background "#567"
        action[ Hide('story_skipbutton'), Jump(label) ]

screen show_image(img):

    add img xpos 0 ypos 0

screen scene_overlay(imgs):

    layer 'master'

    python:
        if isinstance(imgs, (str, int, unicode, type(Composite((0, 0))) )):
            simg = []
            simg.append(imgs)
        else:
            simg = imgs

    for i in simg:
        python:
            i = ramu.arrayize(i, 3, (0.0, 0.0))

        add i[0] xalign i[1][0] yalign i[1][1] xoffset i[2][0] yoffset i[2][1]
