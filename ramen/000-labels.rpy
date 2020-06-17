default ramen = ramen

label ramen_newgame:

    stop music fadeout 1.0
    stop sound fadeout 1.0

    python:

        if ramen.dev:

            _skipping = True

            try:
                ramen_test()
                print "--- Function: ramen_test ---"
            except BaseException:
                pass

            if renpy.has_label('ramen_test'):
                # mark the test
                sysnote("Made with Ren'Py [renpy.version_only]")
                sysnote("Using {icon=logo-ramen} Ramen framework.")
                # jump the test
                _skipping = False
                renpy.jump('ramen_test')

        _skipping = False

    jump start

label after_load:
    $ renpy.retain_after_load()
    return

label theend:
    $ renpy.block_rollback()
    return
