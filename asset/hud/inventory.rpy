screen inventory_ui(inventory_obj=pocket):
    modal True
    zorder 103

    add Solid('#0009') xpos 0 ypos 0
    python:
        try:
            locals()['item']
        except BaseException:
            locals()['item'] = None
    frame style 'hud_win' + str(hud.pref):
        padding(1, 1 + style['hud_tbar' + str(hud.pref)].yminimum, 1, 1)
        style_prefix 'hud_win'
        use hud_titlebar(inventory_obj.name, 'inventory_ui')
        
        if item is None:
            use inventory_vpgrid(inventory_obj)
        else:
            use inventory_detail(inventory_obj.item(item))


screen inventory_detail(item):
    style_prefix 'hud_win' + str(hud.pref)

    python:
        xs = math.floor(style['hud_win' + str(hud.pref)].xminimum / 2) - 8
        ys = style['hud_win' + str(hud.pref)].yminimum - 70
        
        i = ramu.dict2obj(item)
        opt = []
        act = 'Use'
        if i.persist:
            opt.append('Wearable')
            
        xsm = style['hud_win' + str(hud.pref)].xminimum - 120 - 70
            
    hbox xsize xs:
        textbutton ico('arrow-left') style 'hud_icon' text_size 24 text_line_leading 4:
            action SetScreenVariable('item', None)
            
        vbox xoffset 8 yoffset 12:
            xsize xsm
            spacing 8
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

            if i.effect is not None:
                use hud_subtitle('Effect', (xsm,2), style['hud_win' + str(hud.pref) + '_text'].color)
                python:
                    for k in i.effect:
                        if i.effect[k] > 0:
                            pre = "+"
                        else:
                            pre = "-"
                use hud_field(k.title(), "(" + pre + str(i.effect[k]) + ")", 16)
        vbox xoffset 24 yfill True:
            xsize 120
            vbox:
                xsize 120
                add i.icon xalign 0.5 yoffset 8
                null height 32
            vbox yalign 1.0:
                xsize 120
                spacing 16
                if ramen.last_label in ramen.trade['labels'] and i.tradable:
                    textbutton "Sell(" + str(i.price) + "$)" action Null
                if i.require is not None:
                    $act = 'Make'
                if i.eatable:
                    $act = 'Eat/Drink'

                textbutton act action Null
                textbutton 'Drop' action Null
                if ramen.last_label == ramen.storage:
                    textbutton 'Store' action Null

                null height 16

screen inventory_vpgrid(inventory_obj):
    python:
        xs = math.floor(style['hud_win' + str(hud.pref)].xminimum / 2) - 8
        ys = style['hud_win' + str(hud.pref)].yminimum - 70
    
    vpgrid:
        draggable True
        mousewheel True
        scrollbars "vertical"
        side_xalign 1.0
        cols math.floor(style['hud_win' + str(hud.pref)].xminimum / 100)
        for i in inventory_obj():
            imagebutton action SetScreenVariable('item', i):
                idle inventory_obj.item(i).icon
                hover ramu.img_hover(inventory_obj.item(i).icon)
