init -304 python:

    multipersistent = MultiPersistent('tacoen.itch.io')
    config.save_directory = "ramendir"

init -300 python:

    # Set True to enable developer options

    # Game Title
    config.name = _("ramen")
    config.version = str(1)+"."+datetime.datetime.now().strftime('%m%d')

    gui.about = _p("a game made using ramen renpy framework.")
    gui.show_name = True

    config.autoreload = False
    config.has_autosave = False

    # uncomment to release
    # config.developer = False

    # Set False to disable developer options.
    ramen.dev = True

init -2 python:

    build.name = ramu.safestr(config.name)
    config.window_icon = "window_icon.png"

    # False will force disable ramen episodes menu
    # ramen.episodes_menu = False

    # starting stats

    mc.money = ramu.random_int(120, 190)
    mc.bank = ramu.random_int(9000, 9999)
    mc.score = 0

    mc.name = 'Liam'
    mc.lastname = ramu.random_of(['East', 'West', 'North', 'South'])

    mc.stat = {
        'hygiene': ramu.random_int(5, 11),
        'energy': ramu.random_int(5, 11),
        'vital': ramu.random_int(5, 11)
    }

    mc_name = mc.name

    # for npc creation

    pe.native_name = ['Easton', 'Westly', 'Northgate', 'Southvile' ]

    chapter = Character(None,
                        window_xalign=0.8,
                        window_yalign=0.9,
                        window_xsize=0.9,
                        window_ysize=None,
                        window_padding=(0, 0, 0, 0),
                        window_background="#0000",
                        what_xalign=1.0,
                        what_yalign=1.0,
                        what_color="#fff",
                        what_size=48,
                        what_font=pt.font_ui_title,
                        what_prefix="{cps=80}",
                        what_suffix="{/cps}",
                        )

    caption = Character(None,
                        window_xalign=0.05,
                        window_yalign=0.85,
                        window_xsize=config.screen_width / 2,
                        window_ysize=None,
                        window_padding=(0, 0, 0, 0),
                        window_background="#FFCC33DD",
                        what_xalign=0.0,
                        what_yalign=1.0,
                        what_xpos=24,
                        what_xsize=(config.screen_width / 2) - 48,
                        what_color="#000",
                        what_prefix="{vspace=24}{size=-1}{cps=80}",
                        what_suffix="{/cps}{/size}{vspace=0}",
                        )
