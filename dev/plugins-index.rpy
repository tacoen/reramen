screen rdsa_tools_plugins():

    style_prefix 'rds'

    vbox:
        spacing 16
        for p in pp.plugins.keys():
            $ pl = plugin(p)

            vbox:
                spacing 2
                use hbox_line('Plugins', pl.title.title())
                use hbox_line('', p + "(" + pl.version + ")")
                use hbox_line("", pl.desc)
                use hbox_line('Author', pl.author)
                if pl.url is not None:
                    use hbox_line('Author', "{a=" + pl.author + "}" + pl.url + "{/a}")

screen hbox_line(field, value):
    hbox:
        if field is not None:
            text field bold True min_width 150
        if value is not None:
            text value
