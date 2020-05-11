label ramen_newgame:

    python:

        if RAMEN_DEV and renpy.has_label('ramen_test'):
            renpy.jump('ramen_test')

    "Made with Ren'Py [renpy.version_only]."
    "Using {icon=logo-ramen} Ramen framework."

    jump start

label after_load:
    stop music fadeout 1.0
    stop sound fadeout 1.0
    return
