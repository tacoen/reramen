init -100 python:

    pocket = inventory('pocket')

    hud = ramen_object('hud')
    hud.setdir()
    hud.pref = 0
    hud.enable = True
    hud.prop = hud.persistent('prop',
                              bgcolor=['#0000', '#123', "#621", '#222'],
                              fgcolor=['#fff', '#fff', '#fff', '#fff'],
                              wbcolor=['#111', '#123', '#621', '#222', ]
                              )

    ramu.prop2style(hud)

    hud.keyb = [
        #        ["K_F6", Function(ramen_hud_toggle, what='stats')],
        #        ["K_F8", Function(ramen_hud_toggle, what='hud')],
        #        ["ctrl_K_F1", Function(ramen_hud_toggle, what='legend')],
        ["K_F9", [ToggleScreen('inventory_ui', dissolve)]],
    ]

    hud.icons = {
        'pocket': {
            'icon': 'wallet',
            'action': [ToggleScreen('inventory_ui', dissolve)],
            'enable': True
        },
        'phone': {
            'icon': 'phone',
            'action': [ToggleScreen('phone_ui')],
            'enable': False
        }
    }


screen hud():

    for k in hud.keyb:
        key k[0] action k[1]

    key "K_F5" action ToggleVariable('hud.pref', ramu.cycle(hud.pref, hud.prop.bgcolor))
    key "K_F10" action ToggleVariable('hud.enable')
    key "shift_K_F10" action ToggleVariable('quick_menu')

    if hud.enable:

        use hud_navbar()

    use hud_togglebtn()


screen hud_togglebtn():

    python:
        if hud.enable:
            icon = 'chevrons-up'
        else:
            icon = 'chevrons-down'

    hbox xalign 1.0:
        if not hud.enable:
            hbox yoffset 8:
                use hud_component_score()

        textbutton ico(icon) style 'hud_icon' + str(hud.pref):
            padding(16, 16, 16, 16)
            action ToggleVariable('hud.enable')


screen hub_component_time():

    python:
        sunw = ['sun6', 'sun5', 'sun1', 'sun2', 'sun3', 'sun4', 'sun6', 'sun6']
        sunico = sunw[ramen.time.suntime(False)]

    hbox xoffset 16 yoffset 2:
        spacing 4

        text ico(sunico) style 'hud_icon' + str(hud.pref) + "_text" size 24 yoffset 6

        vbox:
            text "Day " + str(ramen.dayplay) style 'ramen_gui' size 20:
                color Color(hud.prop.fgcolor[hud.pref])
            text ramen.time.daytime() + " " + ramen.time.clock() size 14:
                color Color(hud.prop.fgcolor[hud.pref]).opacity(.7)

screen hud_component_score():
    text("{:03d}".format(mc.score)) style 'hud_score' size 40:
        color Color(hud.prop.fgcolor[hud.pref])

screen hud_navbar():

    #    frame background hud.prop.bgcolor[hud.pref]:
    frame style 'hud_nav' + str(hud.pref):
        hbox xfill True:
            spacing 8
            hbox xalign 0.0:
                use hud_component_score()
                use hub_component_time()
            hbox xalign 1.0 yoffset 4:
                spacing 8

                for i in hud.icons.keys():
                    if hud.icons[i]['enable']:
                        if i == 'pocket':
                            hbox:
                                text str(mc.money) + " $" style 'ramen_gui' size 22 yoffset 12:
                                    color Color(hud.prop.fgcolor[hud.pref]).opacity(.7)
                                textbutton ico(hud.icons[i]['icon']) style 'hud_icon' + str(hud.pref):
                                    text_size 32
                                    action hud.icons[i]['action']
                        else:
                            textbutton ico(hud.icons[i]['icon']) style 'hud_icon' + str(hud.pref):
                                text_size 32
                                action hud.icons[i]['action']

                    else:
                        textbutton ico(hud.icons[i]['icon']) style 'hud_icon' + str(hud.pref):
                            text_size 32
                            text_color Color(hud.prop.fgcolor[hud.pref]).opacity(.4)
                            action Null

                null width 40
