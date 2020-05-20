init -300 python:

    # Set True to enable developer options
    ramen.dev = False
    
    # Game Title
    config.name = _("ramen")
    config.version = "1.0"
    gui.about = _p("a game made using ramen renpy framework.")
    gui.show_name = True    

init python:

    build.name = ramu.safestr(config.name)

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

    # lastname

    pe.native_name = [
        'Hilla',
        'Bona',
        'Ilary',
        'Rumvurt',
        'Onaria',
        'Kani',
        'Delani',
        'Yonee',
        'Muhbil',
        'Picsa',
        'Shinga',
        'Pizda',
        'Cikano',
        'Olio',
        'Siknius',
        'Kisa',
        'Pidhi',
        'Kef']
