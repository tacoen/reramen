## Notify screen #########################################################
##
# The notify screen is used to show the player a message. (For example, when
# the game is quicksaved or a screenshot has been taken.)
##
# https://www.renpy.org/doc/html/screen_special.html#notify-screen

init -10 python:

    def notify_ico(message, icon='alert', sec=5):
        """
        Notify with icon

        ``` python:
            $ notify_icon('You see notification with icon','logo-ramen')
            $ renpy.notify("You see renpy default notification.")
        ```

        """

        renpy.show_screen('notify_ico', message=message, icon=icon, sec=5)

screen notify_ico(message, icon='alert', sec=5):

    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        hbox:
            text ico(icon) style 'ramen_icon_text' size 20 line_leading 2
            null width 8
            text "[message!tq]"

    timer(float(sec)) action Hide('notify_ico')

screen notify(message):

    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"

    timer 3 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is frame:
    xpos pt.dialogue_xpos
    yalign 0.7
    xsize pt.dialogue_width
    background rui.button(pt.notify_background, Borders(2, 2, 2, 2))
    padding(24, 12, 24, 12)

style notify_text is ramen_gui:
    size 20
