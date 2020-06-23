screen shop_ui(inv, size=(300, 480), align=(0.5, 0.5), counting=True, background='#fff', name='shop_ui'):

    # the icon size 100, 300 means 3 cols

    default item = None
    default cart_count = 0
    default cart_price = 0

    use shop_face(name, inv=inv, size=size, align=align, background=background, counting=counting):

        style_prefix "modal"

        if item is None:
            use inventory_grid(inv, size, align)
        else:
            use shop_detail(inv, item, size, align, counting)


screen shop_face(name, inv, size, align, background, counting):

    python:

        if counting:
            width = size[0]+340+32
        else:
            width = size[0]+32

    frame xsize width ysize size[1] xalign align[0] yalign align[1]:
        padding(10, 10, 10, 10)
        background background

        if not counting:

            hbox xsize width-24 xfill True:
                transclude

        if counting:

            hbox xsize width-24 xfill True:

                transclude

                vbox xsize 300 xalign 1.0:

                    use shop_cartview(inv, name, size)

screen shop_cartview(inv, name, size):

    vbox xsize 300 yfill True ysize size[1]:

        vbox xsize 280 xoffset 10:
            spacing 2
            yfill False
            style_prefix 'shop'

            hbox xsize 280:
                text 'Item(s) :'  size 18 color "#ccc"
                text str(inv.cart.count())  size 18 xalign 1.0

            add ramu.hline((280, 1), "#ccc")

            for i in inv.cart.cart:
                null height 4
                hbox xsize 280:
                    style_prefix "shop_detail"
                    text str(inv.cart.cart[i][0]) min_width 20 text_align 0.5
                    text inv.item(i).name min_width 200
                    text str(inv.cart.cart[i][1]) min_width 60 text_align 1.0 xalign 1.0

            null height 12

            add ramu.hline((280, 1), "#ccc")

            hbox xsize 280:
                text 'Total :'  size 18 color "#ccc"
                text str(inv.cart.total())  size 18 xalign 1.0

        hbox yalign 1.0 ysize 52 xfill True:

            if inv.cart.count() > 0:

                if mc.money >= inv.cart.total():

                    textbutton "Pay" style "inventory_action_button":
                        action[
                            Function(inv.cart.purchase),
                            SetScreenVariable('item', None),
                            Hide(name),
                            Return(True)
                        ]

                else:

                    textbutton "Pay" style "inventory_action_button":
                        background "#999"
                        action[
                            Function(inv.cart.reset),
                            SetScreenVariable('item', None),
                            Hide(name),
                            Return(True)
                        ]

            textbutton "Exit" style "inventory_action_button" xalign 1.0:
                action[
                    Function(inv.cart.reset),
                    SetScreenVariable('item', None),
                    Hide(name),
                    Return(False)

                ]


transform item_detail:
    zoom 1.5

screen shop_detail(inv, item, size, align, counting):

    python:
        i = inv.item(item)

    vbox xsize size[0]-24 ysize size[1] yfill True:

        hbox:
            textbutton ico('arrow-left') style 'ramen_icon':
                text_size 20 text_color "#333" text_hover_color "#111"
                action SetScreenVariable('item', None)

            vbox ysize size[1]-52:

                vbox:

                    if i.name is not None:
                        text i.name

                    add i.icon xalign 0.5 at item_detail

                    if not i.desc == "":
                        text i.desc

                    null height 8
                    add ramu.hline(((size[0] - 24), 1), "#ccc")
                    null height 8

                    use inventory_hbox('Price', i.price)

                    if i.count > 1:
                        use inventory_hbox('Count', i.count)

                    if i.require is not None:
                        use inventory_hbox('Require', i.require)

                    if i.effect:
                        null height 16
                        add ramu.hline(((size[0] - 24), 1), "#ccc")
                        text 'Effect' bold True size 18 color "#ccc"

                        for e in i.effect:
                            use inventory_hbox(e.title(), i.effect[e])

        hbox xoffset 32 ysize 52 xalign 1.0:

            style_prefix "inventory_action"

            if counting:
                textbutton "Add" action[
                    Function(inv.cart.add, item_id=i.id, item_price=i.price),
                    SetScreenVariable('item', None)
                ]

            else:

                textbutton "Buy" action[
                    Function(inv.cart.add, item_id=i.id, item_price=i.price),
                    Function(inv.cart.purchase),
                    SetScreenVariable('item', None)
                ]

            null width 32

style shop_text:
    color "#000"

style shop_detail_text:
    color "#555"
    size 16

style inventory_detail_text:
    size 20
    color "#999"

style inventory_detail_label_text:
    color "#666"

style shop_action_button is inventory_action_button
style shop_action_button_text is inventory_action_button_text
