style hud is default
style hud_frame is empty
style hud_text is ramen_gui
style hud_icon is button:
    background None
    padding (8,8,8,8)
    
#style hud_icon_text is ramen_icon:
#    size 32
    
style hud_icon_disable is hud_icon
style hud_icon_disable_text is hud_icon_text:
    color "#fff9"
    
style hud_navbar_frame:
    xpos 0
    ypos 0
    xsize config.screen_width
    ysize 56
    padding (8,4,8,8)

style hud_score is ramen_gui:
    size 32
    text_align 1.0
    xalign 1.0
    
style hud_titlebar is empty:
    ysize 38


   
screen hud_titlebar(title,screen_name):

    frame style 'hud_tbar'+str(hud.pref) yoffset -style['hud_tbar'+str(hud.pref)].yminimum:
        hbox xfill True:
            text title.title() size 18 bold True
            textbutton ico('x-square') style 'hud_icon'+str(hud.pref) text_size 18 xalign 1.0:
                action Hide(screen_name)
    