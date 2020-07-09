init -9 python:

    register_plugins(
        title="ATM, Banking screen",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/reramen',
        desc="Provide script for Auto Teller Machine",
        build=True
    )

screen atm_screen(dir):

    default saving = mc.money['bank']
    default withdrawn = 0
    default payment = 0
    default menu = None

    style_prefix "atm"

    use atm_face(dir):

        if menu == 'withdrawn':
            use atm_withdrawn

        elif menu == 'take':
            use atm_takeout

        elif menu == 'payment':
            use atm_payment

        elif menu == 'balance':
            use atm_balance

        elif menu == 'close':

            vbox xalign 0.5 yalign 0.5:
                spacing 24
                text 'Thank you for using us.' xalign 0.5

            timer(2.0) action[ SetScreenVariable('menu', 'main'), Hide('atm_screen'), Return(True) ]

        elif menu == 'main':
            use atm_mainmenu

        elif menu == 'pin_entered':

            vbox xalign 0.5 yalign 0.5:
                text 'Enter Your PIN Number' xalign 0.5
                text '* * * *' bold True  xalign 0.5
                null height 80

                # add bannerads xalign 0.5

            timer(2.0) action[
                SetScreenVariable('menu', 'main')
                ]

        else:
            vbox xalign 0.5 yalign 0.5:

                text 'Enter Your PIN Number'  xalign 0.5
                null height 120
                add bannerads xalign 0.5

            timer(0.5) action[
                Function( ramu.sfx, file='atm-start', path=Plugin('atm').dir ),
            ]

            timer(3.5) action[
                SetScreenVariable('menu', 'pin_entered')
                ]

screen atm_payment:

    vbox xsize style['atm_frame'].xminimum:

        text '-- Under Maintenance --'

    timer(2.0) action[ SetScreenVariable('menu', 'main') ]

screen atm_withdrawn:

    hbox xsize style['atm_frame'].xminimum:

        vbox:
            textbutton "{icon=chevron-left} 2000" action[
                SetScreenVariable('withdrawn', 2000),
                SetScreenVariable('menu', 'take')
                ]
            textbutton "{icon=chevron-left} 1000" action[
                SetScreenVariable('withdrawn', 1000),
                SetScreenVariable('menu', 'take')
                ]
            textbutton "{icon=chevron-left} 500" action[
                SetScreenVariable('withdrawn', 500),
                SetScreenVariable('menu', 'take')
                ]

        vbox xalign 1.0 yfill True:
            textbutton "300 {icon=chevron-right}" style 'atm_onright' action[
                SetScreenVariable('withdrawn', 300),
                SetScreenVariable('menu', 'take')
                ]
            textbutton "100 {icon=chevron-right}" style 'atm_onright' action[
                SetScreenVariable('withdrawn', 100),
                SetScreenVariable('menu', 'take')
                ]
            textbutton "50 {icon=chevron-right}" style 'atm_onright' action[
                SetScreenVariable('withdrawn', 50),
                SetScreenVariable('menu', 'take')
                ]
            textbutton "EXIT {icon=chevron-right}" style 'atm_onright' action[
                SetScreenVariable('withdrawn', 0),
                SetScreenVariable('menu', 'close')
                ]

screen atm_balance(back=True):

    hbox xsize style['atm_frame'].xminimum :
        vbox yalign 0.5 xalign 0.5:
            spacing 20
            text "Your Balance is:" xalign 0.5
            text str(float(mc.money['bank']))+ " $"  xalign 0.5
            text "Thank you for using SHBANK"  xalign 0.5

    if back:
        timer(3.0) action[ SetScreenVariable('menu', 'main') ]


screen atm_takeout:

    python:
        mcf.withdrawn(withdrawn)

    use atm_balance(False)

    timer(1.0) action[
        Function( ramu.sfx, file='atm-over', path=Plugin('atm').dir ),
        SetScreenVariable('menu', 'close'),
        ]

screen atm_mainmenu:

    hbox xsize style['atm_frame'].xminimum:
        vbox:
            textbutton "{icon=chevron-left} Payment":
                action SetScreenVariable('menu', 'payment')
            textbutton "{icon=chevron-left} Balance":
                action SetScreenVariable('menu', 'balance')
        vbox xalign 1.0 yfill True:
            textbutton "Withdrawn {icon=chevron-right}" style 'atm_onright':
                action SetScreenVariable('menu', 'withdrawn')
            textbutton "Exit {icon=chevron-right}" style 'atm_onright':
                action Return(False)

screen atm_face(dir):

    python:
        face = ramu.ezfind('atm-face', 'image', Plugin('atm').dir)

    add face

    frame:
        has vbox
        hbox xsize style['atm_frame'].xminimum:
            text "SHBANK ATM" xalign 0.5 text_align 0.5 size 40

        transclude


style atm is default

style atm_frame:
    background "#0000"
    xpos 272
    ypos 138
    xminimum 740
    ymaximum 500


style atm_hbox:
    xfill True

style atm_vbox:
    spacing 24

style atm_text is ramen_gui:
    color "#ff0"
    size 32

style atm_button is gui_button:
    hover_background "#cdf"

style atm_button_text is atm_text:
    hover_color "#000"

style atm_onright is atm_button:
    xalign 1.0

style atm_onright_text is atm_button_text:
    xalign 1.0
