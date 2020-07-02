## Notify screen #########################################################
##
# The notify screen is used to show the player a message. (For example, when
# the game is quicksaved or a screenshot has been taken.)
##
# https://www.renpy.org/doc/html/screen_special.html#notify-screen
screen notify_ico(message, icon='alert', sec=5, style='notice'):

    zorder 100
    style_prefix style

    frame at notify_appear:
        button:
            if icon is not None:
                hbox:
                    text ico(icon) style 'notice_icon'
                    null width 8
                    text "[message!tq]"
            else:
                text "[message!tq]"

            action[ Hide('notify_ico') ]

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


style notice is default
style notice_frame is frame:
    xalign 0.02
    yalign 0.025
    xsize pt.dialogue_width * 3/4
    background "#fffd"
    padding(16, 16, 32, 16)

style notice_icon is ramen_icon_text:
    size 22
    line_leading 2
    outlines pt.idle_outlines
    color "#000"

style notice_text is ramen_gui:
    size 24
    color "#333"

style notify_frame is frame:
    xpos pt.dialogue_xpos
    yalign 0.7
    xsize pt.dialogue_width
    background rui.button(pt.notify_background, Borders(2, 2, 2, 2))
    padding(24, 12, 24, 12)

style notify_text is ramen_gui:
    size 20
