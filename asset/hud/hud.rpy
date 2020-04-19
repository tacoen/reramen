init -100 python:

    hud = ramen_object('hud')
    hud.setdir()
    hud.pref=1
    hud.enable=True
    hud.prop = hud.persistent('prop',
        bgcolor = [ '#0000', '#123C', '#000C', '#fffc' ],
        fgcolor = [ '#fff', '#eee', '#ccc', '#333' ],
    )
    hud.keyb=[
#        ["K_F6", Function(ramen_hud_toggle, what='stats')],
#        ["K_F8", Function(ramen_hud_toggle, what='hud')],
#        ["shift_K_F8", Function(ramu.toggle, what='quick_menu')],
#        ["ctrl_K_F1", Function(ramen_hud_toggle, what='legend')],
#        ["K_F9", Function(ramen_hud_toggle, what='pocket')],
    ]
    
    print hud.color
    
style hud is default
style hud_frame is empty
style hud_text is ramen_gui
style hud_icon is button:
    background None
    padding (8,8,8,8)
style hud_icon_text is ramen_icon:
    size 24
    
style hud_navbar_frame:
    xpos 0
    ypos 0
    xsize config.screen_width
    ysize 56
    padding (8,8,8,8)

style hud_score is ramen_gui:
    size 32
    text_align 1.0
    xalign 1.0
    
screen hud():

    style_prefix "hud"

    for k in hud.keyb:
        key k[0] action k[1]

    key "K_F10" action ToggleVariable('hud.enable')

    if hud.enable:

        use hud_navbar()

        key "K_F5" action ToggleVariable('hud.pref',ramu.cycle(hud.pref,hud.prop.bgcolor))


    use hud_togglebtn()


             
screen hud_togglebtn():

    python:
        if hud.enable:
            icon = 'chevrons-up'
        else:
            icon = 'chevrons-down'

    hbox xalign 1.0:
        if not hud.enable:
            text ("{:03d}".format(mc.score)) style 'hud_score' yoffset 10
        textbutton ico(icon) style 'hud_icon':
            action ToggleVariable('hud.enable') padding (16,16,16,16)
    
screen hud_navbar():
    style_prefix 'hud_navbar'
    
    frame background hud.prop.bgcolor[hud.pref]:
        text 'navbar'





    
