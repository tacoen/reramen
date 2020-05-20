define character.sysd = Character('', window_background="#0000", what_xalign=0.5)

label ramen_newgame:

    $ _skipping = False

    stop music fadeout 1.0
    stop sound fadeout 1.0

    python:

        if ramen.dev and renpy.has_label('ramen_test'):
            renpy.jump('ramen_test')

    sysd """
    Made with Ren'Py [renpy.version_only]

    Using {icon=logo-ramen} Ramen framework.
    """

    $ _skipping = True

    jump start

label after_load:

    return
