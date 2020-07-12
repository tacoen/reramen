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

    if hud.active:


        if hud.enable or shade:

            use hud_time()
            use hud_cash()
            use hud_score()

        # if hud.enable or shade:
            # add(ramu.ezfind('top-shade')) xalign 1.0 yalign 0.0 at FadeInterval(0.5)

        hbox xalign 1.0 yalign 0.0:

            spacing 8
            style_prefix 'hud'


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
        key "shift_K_F6" action ToggleScreen('show_image', img=ramu.ezfile(Plugin('hud').dir+'legend'))
        key "K_F7" action ToggleScreen('hud_stats', stats=['energy', 'hygiene', 'vital'])
        key "shift_K_F7" action ToggleVariable('quick_menu')

        if hud.enable:
            key "game_menu" action SetVariable('hud.enable', False)

        if hud.enable:
            timer 0.2 action Show('hud_bar')
        else:
            timer 0.2 action Hide('hud_bar')

screen hud_score(notif=False):
    
    python:
        if notif:
            transforma = delayed_blink
        else:
            transforma = basic_anim
    
    hbox xpos 1140 xsize 120 yoffset 14 at transforma:
        text ramu.maxscore(mc.score['point']) style 'hud_score' min_width 120

    if notif:
        timer (3.0) action [ Hide('hud_score') ]

screen hud_cash(notif=False):
    python:
        if notif:
            transforma = delayed_blink
        else:
            transforma = basic_anim

    hbox xpos 1040 ysize 72 yfill True at transforma:
        style_prefix 'hud'    
        text ico('ico-cash') style 'hud_icon_text' size 18 yalign 0.5 color "#fffc" 
        null width 4
        text ramu.str_nicecash(mc.money['cash']) size 24  yalign 0.5 

    if notif:
        timer (3.0) action [ Hide('hud_cash') ]

screen hud_time(notif=False):

    python:
        if notif:
            transforma = delayed_blink
        else:
            transforma = basic_anim

    hbox yoffset 10 xpos 910 at transforma:
        style_prefix 'hud'    
        spacing 8
        vbox:
            spacing 0
            yalign 0.5
            text ramentime.clock() xalign 1.0
            text ramen.time.strftime('%A') xalign 1.0
        text ico(ramentime.ico()) style 'hud_icon_text' size 40 yalign 0.5 color "#fff"
        null width 16

    if notif:
        timer (3.0) action [ Hide('hud_time') ]
        
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

screen hud_stats(stats=[]):

    vbox xsize 142 xalign 1.0 xoffset -80 yalign 0.1 yoffset 16:
        spacing 16
        for s in stats:
            vbox:
                style_prefix 'hud_stat'
                spacing 4
                hbox xfill True:
                    text s.title()
                    text str(mc.stat[s])+"/20" xalign 1.0
                bar value mc.stat[s] range 20 style 'hud_stat_bar_'+s.lower()

style hud_stat_text is ramen_gui:
    size 16
    outlines pt.hover_outlines

style hud_stat_bar is bar:
    ysize 8
    base_bar "#6666"

style hud_stat_bar_vital is hud_stat_bar:
    thumb "#e2d"
    left_bar "#e2dd"

style hud_stat_bar_energy is hud_stat_bar:
    thumb "#ff2"
    left_bar "#ff2d"

style hud_stat_bar_hygiene is hud_stat_bar:
    thumb "#2e2"
    left_bar "#2e2d"

init python:
    if renpy.has_screen('hud'):
        config.overlay_screens.append("hud")
