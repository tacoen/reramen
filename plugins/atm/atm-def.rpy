init -9 python:

    register_plugins(
        title="ATM, Banking screen",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/reramen',
        desc="Provide script for Auto Teller Machine",
        build=True
    )

    def atm_drawn(ammount):
        value_transfer(ammount, mc.bank, mc.money)
        ramu.sfx("atm-over", Plugin('atm').dir)
        return True

style atm is default

style atm_frame:
    background "#0000"
    xpos 272
    ypos 138
    xsize 740
    ysize 430

style atm_text is ramen_gui:
    color "#ff0"
    size 32

style atm_button is gui_button:
    hover_background "#cdf"

style atm_button_text is atm_text:
    hover_color "#000"

# screen atm(dscr=None):

    # python:
    # try:
    # scr
    # except BaseException:
    # scr = dscr

    # style_prefix "atm"

    # python:

    # face = ezfind('atm-face', 'image', Plugin('atm').dir)

    # add face

    # frame:
    # vbox yfill True:
    # vbox:
    # null height 32
    # hbox xfill True:
    # text "SHBANK ATM" xalign 0.5
    # null height 32

    # if scr is None:
    # use atm_mainmenu
    # elif scr == 'balance':
    # use atm_balance
    # elif scr == 'withdrawn':
    # use atm_withdrawn
    # elif scr == 'payment':
    # use atm_payment
    # else:
    # vbox yfill True xsize 740:
    # text "Thank you for banking with us." xalign 0.5

# screen atm_pin(text):

    # python:
    # face = ramu.fn_search("atm-face", ATMPATH)
    # if not face:
    # face = Solid('#009')

    # add face

    # style_prefix "atm"
    # frame:
    # vbox xalign 0.5 yalign 0.5:
    # text "[text]"

# screen atm_balance():
    # vbox yfill True xsize 740:
    # text str(mc.bank) + " $" size 48 xalign 0.5
    # textbutton "< Back" action SetScreenVariable('scr', None)

# screen atm_payment():
    # python:
    # if rbc.cycle:
    # homebill = 350
    # else:
    # homebill = 0

    # hbox xfill True:
    # vbox yalign 1.0:
    # textbutton "< Back" action SetScreenVariable('scr', None)
    # vbox xalign 1.0:
    # spacing 24
    # textbutton "(" + str(homebill) + ") Home Bill >" action[
    # SetVariable('rbc.cycle', False),
    # Function(mc.pay, where='bank', ammount=homebill),
    # Return('balance')
    # ]

# screen atm_withdrawn():
    # hbox xfill True:
    # vbox:
    # spacing 24
    # textbutton "< 1000" action[Function(atm_drawn, ammount=1000), Return('balance')]
    # textbutton "< 700" action[Function(atm_drawn, ammount=700), Return('balance')]
    # textbutton "< 500" action[Function(atm_drawn, ammount=500), Return('balance')]
    # null height 32
    # textbutton "< Back" action SetScreenVariable('scr', None)
    # vbox xalign 1.0:
    # spacing 24
    # textbutton "300 >" action[Function(atm_drawn, ammount=300), Return('balance')]
    # textbutton "100 >" action[Function(atm_drawn, ammount=100), Return('balance')]
    # textbutton "50 >" action[Function(atm_drawn, ammount=50), Return('balance')]

# screen atm_mainmenu():

    # hbox xfill True:
    # vbox:
    # spacing 24
    # textbutton "< Payment" action SetScreenVariable('scr', 'payment')
    # textbutton "< Balance" action SetScreenVariable('scr', 'balance')
    # textbutton "< Exit" action Return(False)
    # vbox yalign 1.0 xalign 1.0:
    # spacing 24
    # textbutton "Withdrawn >" action SetScreenVariable('scr', 'withdrawn')


# label atm:
    # show screen atm_pin('pin:')
    # $ ramu.sfx('atm-start', ATMPATH, True)
    # pause 1
    # hide screen atm_pin
    # show screen atm_pin('pin: ******')
    # pause 3
    # hide screen atm_pin
    # call screen atm()
    # if _return == 'balance':
    # call screen atm('balance')
    # else:
    # $ ramu.sfx('atm-cancel', ATMPATH)
    # show screen atm('thanks')
    # pause 2
    # hide screen atm
    # return
