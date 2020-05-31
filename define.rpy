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
    mc.lastname = ramu.random_of(['East', 'West', 'North', 'South'])
    mc.name = 'Liam'

    mc.stat = {
        'hygiene': ramu.random_int(5, 11),
        'energy': ramu.random_int(5, 11),
        'vital': ramu.random_int(5, 11)
    }

    mc_name = mc.name

    pe.native_name = ['Easton','Westly','Northgate','Southvile' ]

