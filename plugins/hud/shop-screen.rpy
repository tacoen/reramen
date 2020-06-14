screen shop_ui(inv, size=(380, 480), align=(0.5, 0.5), name='shop_ui', counting=True):

    default item = None
    default cart_count = 0
    default cart_price = 0

    use shop_face(name, inv=inv, size=(size[0] + 324, size[1]), align=align, counting=counting):

        style_prefix "modal"

        if item is None:
            use inventory_grid(inv, size, align)
        else:
            use shop_detail(inv, item, size, align)


screen shop_face(name, inv, size, align, counting):

    frame xsize size[0] ysize size[1] xalign align[0] yalign align[1]:
        padding(10, 10, 10, 10)
        background "#fff"

        hbox:

            transclude

            vbox xoffset 20 xsize 200:
                spacing 16
                style_prefix 'shop'

                if counting:

                    text 'Item(s) :' + str(vending.cart.count())

                    for i in vending.cart.cart:
                        hbox xsize 240:
                            style_prefix "shop_detail"
                            text str(vending.cart.cart[i][0]) min_width 30
                            text i min_width 150
                            text str(vending.cart.cart[i][1])+ " $" min_width 60

                    text 'Price : ' + str(vending.cart.total())

                else:

                    text 'Item(s) :' + str(vending.cart.count())
                    text 'Price : ' + str(vending.cart.total())

                if vending.cart.count() > 0:

                    textbutton "Pay" style "inventory_action_button" action[
                        Function(vending.cart.purchase),
                        SetScreenVariable('item', None),
                        Hide(name)
                    ]

                textbutton "Exit" style "inventory_action_button" action[
                    Function(vending.cart.reset),
                    SetScreenVariable('item', None),
                    Hide(name)
                ]

screen shop_detail(inv, item, size, align):

    python:
        i = inv.item(item)

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
                        text i.desc

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

                        for e in effect:
                            use inventory_hbox(e.title(), i.effect[e])

        vbox xsize 120 yfill True ysize size[1] - 64:
            style_prefix "inventory_action"

            add i.icon xalign 0.5

            vbox yalign 1.0 xalign 0.5:
                spacing 10

                textbutton "Add" action[
                    Function(vending.cart.add, item_id=i.id, item_price=i.price),
                    SetScreenVariable('item', None)
                ]

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
