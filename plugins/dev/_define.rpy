init -290 python:

    register_plugins (
        title="ramen develope",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/reramen',
        desc="Developer Screens",
        build=True
    )

    rds = ramen_object()

    rds.kdict('pos',
        panel = [0,0,config.screen_width,config.screen_height,None,'#012' ],
        topbar = [0,0,config.screen_width,40,(8,8,8,8),'#345' ],
        side = [0,41,300,config.screen_height-41, (8,8,8,8),'#234' ],
        win = [301,41,config.screen_width-301,config.screen_height-32,(8,8,8,8)]
    )
    
    rds.menu = ramen.objects
    rds.menu['tools']=['md']
    rds.menu['tools'].append('plugins')

    rds.md_path = "E:/pp-renpy/ramen/wiki/"
    rds.game_path = "E:/pp-renpy/ramen/game/"