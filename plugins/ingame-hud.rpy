init -199 python:
    hud =  ramen_object(
        pref = 0,
        enable = False,
        bgcolor = [ "#000", "#fff" ],
        fgcolor = [ "#fff", "#000" ]
    )
    
    hud.maxpref = len(hud.bgcolor)
    
    hud.kdict('icons',
        pocket = { 
            'icon': 'ico-wallet', 
            'key': "K_F8", 
            'action': Null,
            'enable': True
        },
        phone = { 
            'icon': 'ico-phone', 
            'key': "K_F9", 
            'action': Null,
            'enable': True
        },
        map = { 
            'icon': 'ico-map', 
            'key': "K_F9", 
            'action': Null,
            'enable': False
        }
    )

    style['hud']=Style('empty')
    style['hud_text'].antialias=True
    style['hud_text'].font=pe.font_ui_text
    style['hud_text'].size=16
    
    style['hud_score']=Style('hud_text')
    
    style['hud_score'].size=32
    style['hud_icon']=Style('button')
    style['hud_icon'].background=Color('#0000')
    style['hud_icon_text']=Style('ramen_icon')
    style['hud_icon_text'].size=32
    
    style['quickmenu']=Style('default')
    style['quickmenu_button']=Style('button')
    style['quickmenu_button'].padding=(8,8,8,8)
    style['quickmenu_button_text']=Style('ramen_icon')
    style['quickmenu_button_text'].size=24    
    
    outlines_null = [(absolute(2), Color("#000").opacity(0), absolute(0), absolute(0)) ]
    outlines_fade = [(absolute(2), Color("#000").opacity(.3), absolute(0), absolute(0)) ]
    outlines = [(absolute(2), Color("#000").opacity(.5), absolute(0), absolute(0)) ]
    
    for pref in range(0,len(hud.bgcolor)):
    
        style['hud'+str(pref)+'_text']=Style('hud_text')
        style['hud'+str(pref)+'_text'].color=Color(hud.fgcolor[pref]).opacity(1)
        style['hud'+str(pref)+'_text'].outlines = outlines_fade

        style['hud_score'+str(pref)]=Style('hud_score')
        style['hud_score'+str(pref)].color=Color(hud.fgcolor[pref]).opacity(1)
        style['hud_score'+str(pref)].outlines = outlines_fade
        
        style['hud_icon'+str(pref)]=Style('hud_icon')
        style['hud_icon'+str(pref)].padding=(16,16,16,16)
        style['hud_icon'+str(pref)].color=Color(hud.fgcolor[pref]).opacity(1)
        
        style['hud_icon'+str(pref)+'_text']=Style('hud_icon_text')
        style['hud_icon'+str(pref)+'_text'].idle_color=Color(hud.fgcolor[pref]).opacity(.9)
        style['hud_icon'+str(pref)+'_text'].hover_color=Color(hud.fgcolor[pref]).opacity(1)
        style['hud_icon'+str(pref)+'_text'].insensitive_color=Color(hud.fgcolor[pref]).opacity(.2)
        style['hud_icon'+str(pref)+'_text'].insensitive_outlines=outlines_null
        style['hud_icon'+str(pref)+'_text'].outlines = outlines_fade
        style['hud_icon'+str(pref)+'_text'].hover_outlines =outlines

        style['hud_icontext'+str(pref)]=Style('hud_icon_text')
        style['hud_icontext'+str(pref)].color=Color(hud.fgcolor[pref]).opacity(1)
        style['hud_icontext'+str(pref)].outlines = outlines_fade
        
        style['quickmenu'+str(pref)]=Style('quickmenu')
        style['quickmenu'+str(pref)+'_button']=Style('quickmenu_button')
        style['quickmenu'+str(pref)+'_button_text']=Style('quickmenu_button_text')
        style['quickmenu'+str(pref)+'_button_text'].idle_color=Color(hud.fgcolor[pref]).opacity(.8)
        style['quickmenu'+str(pref)+'_button_text'].hover_color=Color(hud.fgcolor[pref]).opacity(1)
        style['quickmenu'+str(pref)+'_button_text'].insensitive_color=Color(hud.fgcolor[pref]).opacity(.2)
        style['quickmenu'+str(pref)+'_button_text'].outlines = outlines_fade
        style['quickmenu'+str(pref)+'_button_text'].insensitive_outlines=outlines_null
        style['quickmenu'+str(pref)+'_button_text'].hover_outlines =outlines
        
    
            
  
screen hud():

    default shade = False
    
    python:
        
        if hud.enable:
            icon = 'menu'
        else:
            icon = 'menu-small'

    zorder 100

    hbox xalign 1.0 yalign 0.0:
        
        spacing 8
        style_prefix 'hud'+str(hud.pref)
        
        if hud.enable:    
            $ shade = True

        if shade:
            use hud_time()
            use hud_cash()
 
        text '099' style 'hud_score'+str(hud.pref) yoffset 12 xalign 1.0
  
        textbutton ico(icon) style 'hud_icon'+str(hud.pref) action ToggleVariable('hud.enable'):
            padding (16,16,16,16)
            text_size 32
            hovered [ SetScreenVariable('shade',True) ]
            unhovered [ SetScreenVariable('shade',False) ]
        
    if shade:
        timer 0.2 action Show('hud_shade')
    else:
        timer 0.2 action Hide('hud_shade')
    
    if hud.enable:
        timer 0.4 action Show('hud_bar')
    else:
        timer 0.4 action Hide('hud_bar')
        
screen hud_shade():
    
    zorder 90
    add ('theme/gui/htopshade.png') xalign 1.0 yalign 0.0 at FadeInterval(0.5)

screen hud_cash():
    hbox xalign 1.0 ysize 72 yfill True:
        text ico('ico-cash') style 'hud_icontext'+str(hud.pref) size 18 yalign 0.5
        null width 4
        text ramu.nice_cash(10000) size 24  yalign 0.5
        null width 16

screen hud_time():

    hbox yoffset 10 xalign 1.0:
        spacing 8
        vbox:
            spacing 0
            yalign 0.5
            text ramen.time.clock() xalign 1.0
            text ramen.time.strftime('%A') xalign 1.0
        text ico(ramen.time.sun()) style 'hud_icontext'+str(hud.pref) size 40 yalign 0.5
        null width 16
        
screen hud_bar():

    vbox ypos 64 xalign 1.0:

        for e in hud.icons:
            $ i = ramu.makeobj(hud.icons[e])
            if i.enable:
                textbutton ico(i.icon) style 'hud_icon'+str(hud.pref):
                    action i.action
                    padding (12,12,12,12)
            else:
                textbutton ico(i.icon) style 'hud_icon'+str(hud.pref):
                    text_color Color(hud.fgcolor[hud.pref]).opacity(.2)
                    text_outlines outlines_null
                    padding (12,16,12,16)
                    action Null
