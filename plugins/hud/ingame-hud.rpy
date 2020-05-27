init -10 python:

    renpy.add_layer('hud', below='screens', menu_clear=True)

    style['hud'] = Style('empty')
    style['hud_text'].antialias = True
    style['hud_text'].font = pt.font_ui_text
    style['hud_text'].size = 16

    style['hud_score'] = Style('hud_text')
    style['hud_score'].color = Color(hud.fgcolor).opacity(1)
    style['hud_score'].outlines = pt.idle_outlines
    style['hud_score'].size = 32

    style['hud_icon'] = Style('button')
    style['hud_icon'].background = Color('#0000')
    style['hud_icon'].padding = (16, 24, 16, 24)

    style['hud_icon_text'] = Style('ramen_icon_text')
    style['hud_icon_text'].size = 32
    style['hud_icon_text'].idle_color = Color(hud.fgcolor).opacity(.9)
    style['hud_icon_text'].hover_color = Color(hud.fgcolor).opacity(1)
    style['hud_icon_text'].insensitive_color = Color(hud.fgcolor).opacity(.2)
    style['hud_icon_text'].insensitive_outlines = pt.insensitive_outlines
    style['hud_icon_text'].outlines = pt.idle_outlines
    style['hud_icon_text'].hover_outlines = pt.hover_outlines

    style['hud_text'].color = Color(hud.fgcolor).opacity(1)
    style['hud_text'].outlines = pt.idle_outlines

screen hud():

    default shade = False

    python:

        if hud.enable:
            icon = 'menu'
        else:
            icon = 'menu-small'

    zorder 99
    layer 'hud'

    if hud.enable or shade:
        add(pe.theme_path + 'gui/top-shade.png') xalign 1.0 yalign 0.0 at FadeInterval(0.5)

    hbox xalign 1.0 yalign 0.0:

        spacing 8
        style_prefix 'hud'

        if hud.enable or shade:

            use hud_time()
            use hud_cash()

        text "{:03d}".format(mc.score) style 'hud_score' yoffset 14 xalign 1.0

        textbutton ico(icon) style 'hud_icon' action ToggleVariable('hud.enable'):
            padding(16, 16, 16, 16)
            text_size 32
            hovered[SetScreenVariable('shade', True)]
            unhovered[SetScreenVariable('shade', False)]

    for m in hud.icons.keys():

        python:
            try:
                if hud.icons[m]['enable']:
                    k = hud.icons[m]['key']
                    a = hud.icons[m]['action']
            except BaseException:
                k = False

        if k:
            key k action a

    key "K_F10" action ToggleVariable('hud.enable')

    if hud.enable:
        key "game_menu" action SetVariable('hud.enable', False)

    if hud.enable:
        timer 0.2 action Show('hud_bar')
    else:
        timer 0.2 action Hide('hud_bar')

screen hud_cash():
    hbox xalign 1.0 ysize 72 yfill True:
        text ico('ico-cash') style 'hud_icon_text' size 18 yalign 0.5 color "#fffc"
        null width 4
        text ramu.nice_cash(mc.money) size 24  yalign 0.5
        null width 16

screen hud_time():

    hbox yoffset 10 xalign 1.0:
        spacing 8
        vbox:
            spacing 0
            yalign 0.5
            text ramentime.clock() xalign 1.0
            text ramentime.strftime('%A') xalign 1.0
        text ico(ramentime.ico()) style 'hud_icon_text' size 40 yalign 0.5 color "#fff"
        null width 16

screen hud_bar():

    vbox ypos 72 xalign 1.0 at dba:

        for e in hud.icons:
            $ i = object()
            $ i.__dict__ = hud.icons[e]
            if i.enable:
                textbutton ico(i.icon) style 'hud_icon':
                    action i.action
            else:
                textbutton ico(i.icon) style 'hud_icon':
                    action Null

init python:
    if renpy.has_screen('hud'):
        config.overlay_screens.append("hud")
