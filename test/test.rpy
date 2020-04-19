init python:

    print "*** New Testramen ***"

    print 'ramen_object'

    a = ramen_object('apa')
    a.x=1
    a.persistent('prop')
    a.prop.x=2
    a.multipersistent('var')
    a.var.x=3

    b = ramen_object('beh')
    b.x=4
    b.persistent('prop')
    b.prop.x=5
    b.multipersistent('var')
    b.var.x=6

    mc = player('mc',
        name = 'Liam',
        lastname = 'North',
        age=40,
        score = 0,
        money = 100,
    )



    res = "a="
    res += repr( a())
    res += repr( a.prop())
    res += repr( a.var())
    res = res.replace("{","(").replace("}",")")

    print res

    res = "b="
    res += repr( b())
    res += repr( b.prop())
    res += repr( b.var())
    res = res.replace("{","(").replace("}",")")

    print res

    coke = item('coke')
    cake = item('cake')

    pocket = inventory('pocket')

    pocket.add(cake)
    pocket.add(coke)
    pocket.add(coke)

    pocket.use('cake')
    pocket.use('coke')

    print pocket()

    print ramen.time()

    ramen.time.adv(36)

    print ramen.time()
    
    joan = npc('joan',who_color='#C00')

label ramen_test:
    
    mc "I'am [mc.name]!"
    
    show joan 
    joan "Boo!"
    
    $ ramu.test_image(coke.icon())
    "now the other"
    $ ramu.test_image(cake.icon())
    "hide it"
    hide screen test_image
