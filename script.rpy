# The script of the game goes in this file.
# The game starts here.

init python:

    def coba(h=None):
        import datetime
        if h is None:
            return ramentime.time()
        else:
            return ramentime.adv(h)

default cari=22


label start:

    "[wotime]"

    "Hello world"
    #$ co.add(2)

    "Hello world [wotime]"

    "Hello world [wotime]"

    "fine?"

    jump testmenu
