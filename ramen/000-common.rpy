init offset = -299

image white = Solid('#eee')
image black = Solid('#111')
image bg room = Solid('#338')
image mimic = Solid("#0000")
image blank = Solid("#0000")

define qpixellate = Pixellate(0.5, 2)

transform FadeInterval(ms=1.0):
    on show:
        alpha 0
        linear ms alpha 1
    on hide:
        alpha 1
        linear ms alpha 0

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause(cycle - .4)
        repeat

transform ramen_lb:
    xalign 0.0
    yalign 1.0
    yoffset 24

transform ramen_center:
    xalign 0.5
    yalign 1.0

transform dba:
    on show:
        xalign 1.3
        linear 0.5 xalign 1.0
    on hide:
        xalign 1.0
        linear 0.5 xalign 1.3
