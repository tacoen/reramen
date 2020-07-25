init offset = -299

image white = Solid('#eee')
image black = Solid('#111')
image mimic = Solid("#0000")
image blank = Solid("#0000")
image dim = Solid('#000c')
image dim2 = Solid('#000d')
image dim3 = Solid('#000e')

image overlays = ramu.ezfile(pt.overlays, Color("#0019"))

define qpixellate = Pixellate(0.5, 2)

transform basic_anim:
    pass

transform rotate(deg):
    # ged = 0-360
    rotate deg

transform xflip:
    xzoom -1

transform xa(a):
    yalign 1.0
    xalign float(a)/float(10)

transform zoom(z=1.2):
    zoom z

transform scale(size=(100, 100)):
    maxsize size

transform xp(x=0.5, y=1.0):
    yalign 1.0
    xpos x
    yanchor y

transform hit_anim:
    alpha 0.95
    easeout .1 zoom 1.005, alpha 1.0, yoffset 1
    pause 0.8
    easein .1 zoom 1.0, alpha 0.95, yoffset 0
    repeat

transform FadeInterval(ms=1.0):
    on show:
        alpha 0
        linear ms alpha 1
    on hide:
        alpha 1
        linear ms alpha 0

transform delayed_blink(delay=0.2, sec=1):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause(float(sec) - .4)
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
