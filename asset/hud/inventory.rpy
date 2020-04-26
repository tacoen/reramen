screen inventory_ui(inventory_obj=pocket):

    modal True

    add Solid(Color('#fff').opacity(.3))

    python:
        try: locals()['item']
        except: locals()['item']=None

    frame style 'hud_win'+str(hud.pref):
        padding (1,1+style['hud_tbar'+str(hud.pref)].yminimum,1,1)
        style_prefix 'hud_win'

        use hud_titlebar('Inventory','inventory_ui')

        if item is None:
            use inventory_vpgrid(inventory_obj)
        else:
            use inventory_detail(inventory_obj.item(item))

screen inventory_detail(item):

    transclude

    style_prefix 'hud_win'+str(hud.pref)

    vbox:
        python:
            i = ramu.dict2obj(item)
            descr = i.desc
            opt=[]
            act = 'Use'
            dact = 'Drop'

            if i.persist:
                opt.append('Persistent')
                dact = 'Drop'

            if i.eatable:
                opt.append('Eatable')
                act = 'Eat'

            if descr == '':
                descr = 'No description given.'

            option = ''

            for o in opt:
                option += "{size=16}[{b}"+o+"{/b}]{/size} "

            if not option == '': descr += "\n"+option
        hbox:

            vbox xoffset 8 yoffset 12:
                spacing 8
                xsize style['hud_win'+str(hud.pref)].xminimum-120-8-24

                text str(i.name) size 24 bold True
                text descr size 20
                null height 16

                use hbox_field('Contain',str(i.count),16)

                if i.tradable:
                    use hbox_field('Price',str(i.price)+ " $",16)

                if i.require is not None:
                    use hbox_field('Require',str(i.require),16)

                if i.effect is not None:
                    python:
                        for k in i.effect:
                            if i.effect[k] >0: pre="+"
                            else: pre="-"

                    use hbox_field(k.title(),"("+pre+str(i.effect[k])+")",16)

            vbox xoffset 24 yfill True:
                xsize 120

                vbox:
                    xsize 120
                    add i.icon xalign 0.5 yoffset 8
                    null height 32

                vbox yalign 1.0:
                    xsize 120
                    spacing 16

                    if i.tradable:
                        textbutton "Sell" action Null

                    $act = 'Use'

                    if i.require is not None:
                        $act = 'Make'

                    if i.eatable:
                        $act = 'Eat/Drink'

                    textbutton act action Null

                    textbutton 'Drop' action Null

                    textbutton 'Store' action Null

                    null height 16






screen hbox_field(field,value,fz=16):

    hbox xfill True:
        text field bold True size fz xalign 0.0
        text value size fz xalign 1.0

screen inventory_vpgrid(inventory_obj):

        vpgrid:
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_xalign 1.0
            cols math.floor(style['hud_win'+str(hud.pref)].xminimum / 100)

            for i in inventory_obj():

                imagebutton action SetScreenVariable('item',i):
                    idle inventory_obj.item(i).icon
                    hover ramu.img_hover(inventory_obj.item(i).icon)