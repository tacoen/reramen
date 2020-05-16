init -304 python:

    multipersistent = MultiPersistent('tacoen.itch.io')

init -302 python:

    pe = ramen_persistent('env')
    pe.theme_path = 'theme/'
    pe.plugins_path = 'plugins/'
    pe.image_path = 'image/'
    pe.time_ico = ['moon2','moon3','sun1','sun2','sun2','sun3','moon1','moon2']
    pe.time_cond = ['dark','dark','sun1','sun2','sun2','sun3','dark','dark']
    pe.time_word = ['Midnight','Morning','Morning','Noon','Noon','Evening','Evening','Night']
    pe.ext_img = ('.webp', '.png', '.jpg')
    pe.ext_txt= ('.json', '.txt')
    pe.ext_snd = ('.ogg', '.mp3', '.wav')

    pe.limit=(0,20)

    pe.itemd = {
        'name': None,
        'price': int(0),
        'count': int(1),
        'desc': str(''),
        'eatable': False,
        'require': None,
        'effect': None,
        'persist': False,
        'tradable': False,
    }
    
    pl = ramen_persistent('plugins')

    mc = ramen_multipersistent('mc')
    mc_name = 'You'
    character.mc = Character('mc_name',dynamic=True,who_color='#ff0')

init -300 python:

    ramentime = ramen_time()
    ramu = ramen_util()
    ramen.uidnumber=0
    ramen.dev = True
    ramen.objects = {}    
    ramen.items=object()
    ramen.seed = datetime.timedelta(0, 0)

    if persistent.files is None or ramen.dev:
        persistent.files = sorted(renpy.list_files(False))    
    
    config.label_callback = ramu.labelcallback
    config.layers = ['master', 'transient', 'ambient', 'hud', 'screens', 'above_screens','overlay','overlay2', 'console', 'dialog_layer']

    
    