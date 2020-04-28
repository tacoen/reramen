style catalog_detail is default
style catalog_detail_text:
    size 18




screen catalog_ui(inventory_obj=vending):
    python:
        try:
            locals()['item']
        except BaseException:
            locals()['item'] = None
        try:
            locals()['submenu']
        except BaseException:
            locals()['submenu'] = None
            
        mcart = str(len(inventory_obj.cart(None, False)))

    zorder 102
    add Solid('#0009') xpos 0 ypos 0
    modal True

    frame style 'hud_win' + str(hud.pref):
        xalign 0.5
        padding(1, 1 + style['hud_tbar' + str(hud.pref)].yminimum, 1, 1)
        style_prefix 'hud_win'
        use hud_titlebar(inventory_obj.name, 'catalog_ui')

        if submenu == 'cart':
            use catalog_cart(inventory_obj)
        else:
            if item is None:
                use catalog_vpgrid(inventory_obj)
            else:
                use catalog_detail(item,inventory_obj)
        
        frame style style['hud_tbar'+str(hud.pref)]:
            yalign 1.0
            ysize 40
         
            hbox xfill True:
                spacing 2
                textbutton "Cart("+mcart+")" style 'hud_win' + str(hud.pref)+'_button':
                    xalign 0.0
                    action SetScreenVariable('sub','cart')
                textbutton "Check-out" style 'hud_win' + str(hud.pref)+'_button':
                    xalign 1.0
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
                        textbutton 'Detail' style 'hud_win' + str(hud.pref) + '_button':
                            xsize 60 action SetScreenVariable('item', im)
                        textbutton 'Buy' style 'hud_win' + str(hud.pref) + '_button':
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
                
            xsm = style['hud_win' + str(hud.pref)].xminimum - 120 - 70

        hbox ysize None:
    
            textbutton ico('arrow-left') style 'hud_icon' text_size 24 text_line_leading 4:
                action SetScreenVariable('item', None)
            
            vbox xoffset 8 yoffset 12:
                spacing 8
                style 'hud_content'+str(hud.pref)
                style_prefix 'hud_content'+str(hud.pref)

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
                
                use hud_subtitle('Effect', (xsm, 2), style['hud_win' + str(hud.pref) + '_text'].color)
                
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

                textbutton 'Buy' style 'hud_win' + str(hud.pref) + '_button':
                    xsize 60 action Function(inventory_obj.cart, item=i)

screen catalog_cart(inventory_obj):

    style_prefix 'hud_win' + str(hud.pref)

    python:
        cart = inventory_obj.cart(None, False)
        
        xs = math.floor(style['hud_win' + str(hud.pref)].xminimum / 2)
        ys = style['hud_win' + str(hud.pref)].yminimum - 70
        xsm = style['hud_win' + str(hud.pref)].xminimum - 120 - 70

    viewport xsize xs:

        hbox:
    
            textbutton ico('arrow-left') style 'hud_icon' text_size 24 text_line_leading 4:
                action SetScreenVariable('sub', None)
            
            vbox xoffset 8 yoffset 12:
                spacing 8
                style 'hud_content'+str(hud.pref)
                style_prefix 'hud_content'+str(hud.pref)

                text "cart"
                