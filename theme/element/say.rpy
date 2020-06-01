## Say screen ############################################################

screen say(who, what):
    style_prefix "say"

    window:

        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    # If there's a side image, display it above the text. Do not display on the
    # phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0 yoffset 20

# Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize pt.textbox_height
    background pt.dialoque_background

style namebox:
    xpos pt.name_xpos
    yoffset pt.name_ypos
    ysize pt.namebox_height
    xsize pt.namebox_width
    padding pt.namebox_borders

style say_label:
    color pt.accent_color
    size pt.name_size
    xalign pt.name_xalign
    yalign 0.5
    outlines pt.who_outlines

style say_dialogue:
    ypos pt.dialogue_ypos
    xpos pt.dialogue_xpos
    xsize pt.dialogue_width
    line_leading 4
    size 24

style say_thought is say_dialogue:
    xalign 0.5
