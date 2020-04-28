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

    ramen.storage = 'rt2'
    ramen.trade = {
        'res':None,
        'labels':['rt3']
    }
    
    define_item('coke')
    define_item('cake',
        effect={'energy':1,'vital':1},
        require='microwave',
    )

    pocket.add(item('coke'))
    pocket.add(item('coke'))
    pocket.add(item('cake'))

    pocket.use('coke')

    print ramen.time()

    ramen.time.adv(36)

    print ramen.time()
    
    joan = npc('joan',who_color='#C00')

label aaaramen_test:
    
    scene white
    
    mc "I'am [mc.name]!"

label rt2:
    mc "We are on label: [ramen.last_label]"

label rt1:
    #show screen catalog_ui(vending) with dissolve
    
    
label rt3:    
    show joan 
    joan "Boo!"
    
