label ramen_init:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    $ renpy.free_memory

    hide screen _overlays

    python:

        if renpy.has_label('ramen_test'):
            renpy.jump('ramen_test')

    return
