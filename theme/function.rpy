init -299 python:

    class ramen_ui_tool():

        def button(self, color, border=Borders(3, 1, 1, 3), black=False):
            if black:
                res = ramu.ezfind('button-frame-black')
            else:
                res = ramu.ezfind('button-frame-white')

            size = renpy.image_size(res)
            img = Composite(size, (0, 0), Solid(color), (0, 0), res)
            return Frame(img, border, tile=False)

        def button_frame(self, color, border=Borders(3, 3, 3, 3), flip=False):

            res = ramu.ezfind('button-frame')
            size = renpy.image_size(res)
            if flip:
                res = im.Flip(res, True, True)

            img = Composite(size, (0, 0), Solid(color), (0, 0), res)
            return Frame(img, border, tile=False)

        def button_underline(self, color):
            fimg = Composite((24, 2), (0, 0), Solid(color))
            img = Composite((24, 24), (0, 0), Solid('#0000'), (0, 22), fimg)
            return Frame(img, Borders(1, 1, 1, 4), tile=False)

        def metro_button(self, color, shcolor):
            simg = Composite((53, 53), (0, 0), Solid(shcolor))
            fimg = Composite((48, 48), (0, 0), Solid(color))
            img = Composite((53, 53), (5, 5), simg, (0, 0), fimg)
            return Frame(img, Borders(6, 6, 6, 6), tile=False)

        def metro_pad(self, x):
            return (x * 2, x * 1, x * 3, x * 2)

    rui = ramen_ui_tool()

    def font_uitag(tag, argument, contents):

        return [
            (renpy.TEXT_TAG, "font="+pt.font_ui_text),
            ] + contents + [
                (renpy.TEXT_TAG, "/font"),
            ]

    config.custom_text_tags["ui"] = font_uitag

    def icon_tag(tag, icon='logo-ramen'):
        """
        put icons as renpy text_tag

        ``` python
        e " {icon=alert} Warning "
        ```
        """
        return [(renpy.TEXT_TAG, "font=" + pt.font_ui_ico),
                (renpy.TEXT_TEXT, ico(icon)), (renpy.TEXT_TAG, "/font")]

    config.self_closing_custom_text_tags["icon"] = icon_tag
