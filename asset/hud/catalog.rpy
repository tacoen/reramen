style catalog_detail is default
style catalog_detail_text:
    size 18

screen catalog_ui(inventory_obj=vending):
    modal True
    zorder 102
    add Solid('#0009') xpos 0 ypos 0
    python:
        try:
            locals()['item']
        except BaseException:
            locals()['item'] = None

        mcart = str(len(inventory_obj.cart(None, False)))

    frame style 'hud_win' + str(hud.pref):
        xpos 8
        padding(1, 1 + style['hud_tbar' + str(hud.pref)].yminimum, 1, 1)
        style_prefix 'hud_win'
        use hud_titlebar(inventory_obj.name, 'catalog_ui')

        if item is None:
            use catalog_vpgrid(inventory_obj)
        else:
            use catalog_detail(item,inventory_obj)
                
        frame style style['hud_tbar'+str(hud.pref)]:
            yalign 1.0
            ysize 40
         
            hbox:
                spacing 2
                textbutton "Cart("+mcart+")" style 'hud_win' + str(hud.pref)+'_button':
                    action Null
                textbutton "Check-out" style 'hud_win' + str(hud.pref)+'_button':
                    action Null


screen catalog_vpgrid(inventory_obj):

    python:
        xs = math.floor(style['hud_win' + str(hud.pref)].xminimum / 2) - 8
        ys = style['hud_win' + str(hud.pref)].yminimum - 90
    
    vpgrid:
        xsize xs 
        ysize ys
        draggable True
        mousewheel True
        scrollbars "vertical"
        side_xalign 1.0
        cols 2

        for im in inventory_obj():
            $ i = ramu.dict2obj(inventory_obj.item(im))

            hbox:
                imagebutton action SetScreenVariable('item', im):
                    idle i.icon
                    hover ramu.img_hover(i.icon)
                null width 8

                vbox xsize xs - 116 yalign 1.0:
                    style_prefix 'catalog_detail'
                    text str(i.name) size 16
                    text str(i.price) + " $" color gui.accent_color
                    null height 16
                    hbox:
                        spacing 2
                        textbutton 'detail' style 'hud_win' + str(hud.pref) + '_button':
                            xsize 60 action SetScreenVariable('item', im)
                        textbutton 'buy' style 'hud_win' + str(hud.pref) + '_button':
                            xsize 60 action Function(inventory_obj.cart, item=i)

                    null height 32

screen catalog_detail(item,inventory_obj):

    style_prefix 'hud_win' + str(hud.pref)

    python:
        xs = math.floor(style['hud_win' + str(hud.pref)].xminimum / 2)
        ys = style['hud_win' + str(hud.pref)].yminimum - 70

    viewport xsize xs:
        python:
            i = ramu.dict2obj(inventory_obj.item(item))
            opt = []
            act = 'Use'
            if i.persist:
                opt.append('Wearable')
                
            vxs = style['hud_win' + str(hud.pref)].xminimum - 120 - 8 - 24 - 80

        hbox ysize None:
    
            textbutton ico('arrow-left') style 'hud_icon' text_size 24 text_line_leading 4:
                action SetScreenVariable('item', None)
            
            vbox xoffset 8 yoffset 12:
                spacing 8
                xsize vxs
                text str(i.name) size 24 bold True
                if not i.desc == '':
                    text str(i.desc) size 20
                if len(opt) > 0:
                    hbox:
                        for o in opt:
                            text o style 'ramen_label' size 16
                null height 16
                if i.count > 1:
                    use hud_field('Contain', str(i.count), 16)
                if i.require is not None:
                    use hud_field('Require', str(i.require), 16)
                use hud_subtitle('Effect', (vxs, 1), style['hud_win' + str(hud.pref) + '_text'].color)
                if i.effect is not None:
                    python:
                        for k in i.effect:
                            if i.effect[k] > 0:
                                pre = "+"
                            else:
                                pre = "-"
                    use hud_field(k.title(), "(" + pre + str(i.effect[k]) + ")", 16)
            
            vbox xoffset 24:
                xsize 120

                add i.icon xalign 0.5 yoffset 8
                null height 32

                textbutton 'buy' style 'hud_win' + str(hud.pref) + '_button':
                    xsize 60 action Function(inventory_obj.cart, item=i)

