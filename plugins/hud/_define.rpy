init -11 python:

    register_plugins (
        title="outlines hud",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/reramen',
        desc="Provide some HUD",
        build=True
    )
    
    
    hud =  ramen_object(
        pref = 0,
        enable = False,
        bgcolor = "#000",
        fgcolor = "#fff",
    )
    
    hud.maxpref = len(hud.bgcolor)
    
    hud.kdict('icons',
    
        pocket = { 
            'icon': 'ico-wallet', 
            'key': "K_F8", 
            'action': ToggleScreen('inventory_ui',inv=pocket,size=(440,480),align=(0.9,0.4)),
            'enable': True
        },
        
        phone = { 
            'icon': 'ico-phone', 
            'key': "K_F9", 
            'action': ToggleScreen('smphone_ui'),
            'enable': True
        },
        
        map = { 
            'icon': 'ico-map', 
            'key': "shift_K_F9", 
            'action': Null,
            'enable': False
        }
    )