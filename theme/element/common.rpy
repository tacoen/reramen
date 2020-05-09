init offset=-1

screen tooltip(msg,adjust=(0,0)):
    python:
        x,y=ramen.Mouse()

    frame background "#ffe5":
        xpos int(x+adjust[0])+40
        ypos int(y+adjust[1])
        padding (4,4,4,4)
        text msg size 12 color '#fff9'


## Additional screens
## https://www.renpy.org/doc/html/screen_special.html

## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

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
    padding (4,4,4,4)

style skip_text is ramen_gui:
    size 16

style skip_triangle is ramen_icon_text:
    size 20
    


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen ramen_notify(message,icon='alert'):
    
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        hbox:
            text ico(icon) style 'ramen_icon_text' size 20 line_leading 2
            null width 8
            text "[message!tq]"

    timer 3 action Hide('ramen_notify')

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
    xalign 1.0 
    xoffset -58
    ypos 58
    background rui.button("#000C",Borders(2,2,2,2))
    padding (16,8,16,8)

style notify_text is ramen_gui:
    size 20
