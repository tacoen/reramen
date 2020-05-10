init offset = -1

screen tooltip(msg, adjust=(0, 0)):
    python:
        x, y = ramu.mouse()

    frame background "#ffe5":
        xpos int(x + adjust[0]) + 40
        ypos int(y + adjust[1])
        padding(4, 4, 4, 4)
        text msg size 12 color '#fff9'


# Additional screens
# https://www.renpy.org/doc/html/screen_special.html

# https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text ico('chevron-right') at delayed_blink(0.0, 1.0) style "skip_triangle"
            text ico('chevrons-right') at delayed_blink(0.2, 1.0) style "skip_triangle"
            text ico('chevrons-right') at delayed_blink(0.4, 1.0) style "skip_triangle"


style skip_frame is empty:
    ypos 0
    background "#0006"
    padding(4, 4, 4, 4)

style skip_text is ramen_gui:
    size 16

style skip_triangle is ramen_icon_text:
    size 20

