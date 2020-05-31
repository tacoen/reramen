screen rdsa_tools_plugins():

    style_prefix 'rds'

    vbox:
        spacing 16
        for p in pp.plugins.keys():
            $ pl = Plugin(p)

            vbox:
                spacing 2
                use hbox_line('Plugins', pl.title.title(), 200, 0.0, 0.1)
                use hbox_line('', p + "(" + pl.version + ")", 200, 0.0, 0.1)
                use hbox_line("", pl.desc, 200, 0.0, 0.1)
                if pl.author_url is not None:
                    use hbox_line('Author', "{a=" + pl.author_url + "}" + pl.author + "{/a}", 200, 0.0, 0.1)
