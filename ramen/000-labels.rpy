define character.sysnote = Character('', window_background="#0000", what_xalign=0.5, what_size=18)

default ramen = ramen

label ramen_newgame:

    $ _skipping = False

    stop music fadeout 1.0
    stop sound fadeout 1.0

    python:

        if ramen.dev and renpy.has_label('ramen_test'):
            # mark the test
            character.sysnote("Made with Ren'Py [renpy.version_only]")
            character.sysnote("Using {icon=logo-ramen} Ramen framework.")
            # jump the test
            renpy.jump('ramen_test')

    $ _skipping = True

    jump start

label after_load:
    $ renpy.retain_after_load()
    return
