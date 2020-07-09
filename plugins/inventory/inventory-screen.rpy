init -12 python:

    pocket = ramen_inventory('pocket', max=16)

    storage = ramen_inventory('storage', max=96)

    ramen.res = [None, False, False, False]

    ramen.labeloc = {}
    ramen.labeloc['storage'] = ['home.kitchen']
    ramen.labeloc['microwave'] = ['home.kitchen']
    ramen.labeloc['pawn'] = ['pawn_shop']

    def inv_resnotify(sec=3.0, sfx=None):

        ### ---

        msg = []
        res = ramen.res

        if res[0] is not None:
            msg.append(str(res[0]))

        if res[1]:
            icon = 'square-minus'

        if res[2]:
            icon = 'square-x'

        if res[3]:
            msg.append(res[3][0] + " = " + str(res[3][1]))

        if sfx is None:
            sfx = 'beep'

        rascr.notify("\n".join(msg), icon, sfx, sec)

    def labeloc(what):
        try:
            if ramen.label_last in ramen.labeloc[what]:
                return True
            else:
                return False
        except BaseException:
            return False

screen inventory_ui(inv, size=(880, 480), align=(0.5, 0.5), name='inventory_ui'):

    default item = None
    $ cnt = "(" + str(len(inv.inventory.keys())) + "/" + str(inv.max) + ")"

    use modal(name,
              Showtitle=True, title=inv.id + cnt, closebutton=True, size=(size[0] + 24, size[1]), align=align):
        style_prefix "modal"

        if item is None:
            use inventory_grid(inv, size, align)
        else:
            use inventory_detail(inv, item, size, align)

screen inventory_hbox(what, value):

    hbox xfill True:
        style_prefix 'inventory_detail'
        text str(what) color "#666" min_width 120
        text str(value) xalign 1.0

screen inventory_detail(inv, item, size, align):

    python:
        i = inv.item(item)

        try:
            i.persistent
        except BaseException:
            i.persistent = False

    hbox:
        vbox xsize size[0] - 118:

            hbox:
                textbutton ico('arrow-left') style 'ramen_icon':
                    text_size 20 text_color "#333" text_hover_color "#111"
                    action SetScreenVariable('item', None)

                vbox:
                    spacing 8
                    if i.name is not None:
                        text i.name

                    if not i.desc == "":
                        text i.desc size 20 color '#999'

                    if i.count > 1:
                        use inventory_hbox('Count', i.count)

                    if i.require is not None:
                        use inventory_hbox('Require', i.require)

                    if i.tradable and labeloc('pawn'):
                        use inventory_hbox('Sell Price', i.price)

                    if i.effect:
                        null height 6
                        add ramu.hline(((size[0] - 148 - 24), 1), "#ccc")
                        text 'Effect' bold True size 18 color "#ccc"

                        for e in i.effect:
                            use inventory_hbox(e.title(), i.effect[e])

        vbox xsize 120 yfill True ysize size[1] - 64:
            style_prefix "inventory_action"

            add i.icon xalign 0.5

            vbox yalign 1.0 xalign 0.5:
                spacing 10

                python:
                    action_text = i.require

                    the_action = [
                        Function(inv.use, item_id=i.id, use_ramen=True),
                        Function(inv_resnotify),
                        SetScreenVariable('item', None)
                    ]

                if i.tradable and labeloc('pawn'):

                    textbutton "Sell" action[
                        Function(inv.sell, item_id=i.id, use_ramen=True),
                        Function(inv_resnotify),
                        SetScreenVariable('item', None)
                    ]

                if not i.persistent:

                    if i.eatable:
                        $ action_text = "Consume"
                    else:
                        $ action_text = "Use"

                    if i.require is not None:
                        if labeloc(i.require):
                            $ action_text = i.require.title()
                            $ the_action = [
                                Function(inv.use, item_id=i.id, use_ramen=True),
                                SetScreenVariable('item', None),
                                Jump('solo_'+i.require)
                            ]

                        else:
                            $ action_text = False

                    if action_text:

                        textbutton action_text action the_action

                if labeloc('storage') and inv.id == "storage":

                    null height 8

                    textbutton "Take" action[
                        Function(inv.transfer, item_id=i.id, dst_id='pocket'),
                        SetScreenVariable('item', None)
                    ]

                if labeloc('storage') and inv.id == "pocket":

                    null height 8

                    textbutton "Store" action[
                        Function(inv.transfer, item_id=i.id, dst_id='storage'),
                        SetScreenVariable('item', None)
                    ]

                null height 8

                textbutton "Drop" action[
                    Confirm("Drop " + i.name + " ?",
                            [Function(inv.drop, item_id=i.id)], None, True),
                    SetScreenVariable('item', None)
                ]

screen inventory_grid(inv, size, align):

    python:
        vp_height = size[1] - 40
        vp_width = size[0]
        cols = int(math.floor(vp_width / 100))
        rows = int(inv.max / cols)
        vp_width_withspacing = vp_width + 16

    if len(inv.inventory.keys()) < 1:

        vbox:
            ysize vp_height
            xsize vp_width_withspacing

            text "Empty" color "#333" xalign 0.5 yalign 0.5

    else:

        vpgrid id "inventory_vp":
            cols cols
            rows rows
            spacing 5
            draggable True
            mousewheel True
            ysize vp_height
            xsize vp_width_withspacing

            $ r_inv = inv()
            $ itemok = False
            for item in sorted(r_inv):

                python:
                    try:
                        i = inv.item(item)
                        if i.count > 1:
                            icon_count = Composite((100, 100), (0, 0), i.icon,
                                                   (75, 75), Text(str(i.count), size=14, color='#111', min_width=25, xalign=0.5, yalign=0.5))
                        else:
                            icon_count = i.icon

                        itemok = True
                    except BaseException:
                        itemok = False

                if itemok:
                    imagebutton action SetScreenVariable('item', item):
                        idle icon_count
                        hover Composite((100, 100), (0, 0), Solid(pt.accent_color), (0, 0), icon_count)

        vbar value YScrollValue("inventory_vp"):
            xoffset 8
            ysize vp_height

style inventory_detail_text:
    size 20
    color "#999"

style inventory_detail_label_text:
    color "#666"

style inventory_action_button is button:
    background rui.button_frame("#369", Borders(1, 1, 1, 1), False)
    hover_background rui.button_frame("#58B", Borders(1, 1, 1, 1), False)
    selected_background rui.button_frame("#58B", Borders(1, 1, 1, 1), True)
    xsize 100
    xalign 0.5

style inventory_action_button_text is ramen_gui:
    color "#eee"
    hover_color "#fff"
    xalign 0.5
    size 18
