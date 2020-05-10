# need for seperated sub-repo creations

init -300 python:
    config.version = "1.0"
    config.name = _("ramen")

init python:

    # starting stats
    
    mc.money = ramu.random_int(120,190)
    mc.bank = ramu.random_int(9000,9999)
    mc.score = 0
    mc.lastname = ramu.random_of(['East','West','North','South'])
    mc.name = 'Liam'
    
    mc.stat={
        'hygiene': ramu.random_int(5,11),
        'energy': ramu.random_int(5,11),
        'vital': ramu.random_int(5,11)
    }