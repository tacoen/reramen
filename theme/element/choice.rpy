## Choice screen #########################################################
##
# This screen is used to display the in-game choices presented by the menu
# statement. The one parameter, items, is a list of objects, each with caption
# and action fields.
##
# https://www.renpy.org/doc/html/screen_special.html#choice

# When this is true, menu captions will be spoken by the narrator. When false,
# menu captions will be displayed as empty buttons.

screen choice(items):
    style_prefix "choice"

    vbox:
        if ramen.smphone:
            xalign 0.8
        else:
            xalign 0.5

        yalign 0.7
        yanchor 1.0
        spacing 24

        for i in items:
            textbutton i.caption action i.action


screen vchoice(items):

    hbox xalign 0.5 yalign 0.85:
        spacing 4
        style_prefix 'vchoice'
        for i in items:
            textbutton i.caption action i.action

style vchoice_button is ramen_button_medium:
    background "#222c"
    hover_background "#111c"

style vchoice_button_text is ramen_button_medium_text:
    outlines pt.hover_outlines
    size 20
