init -302 python:

    RAMEN_IMG_EXT = ('.webp', '.png', '.jpg')
    RAMEN_TXT_EXT = ('.json', '.txt')
    RAMEN_IMG_SND = ['.ogg', '.mp3', '.wav']
    RAMEN_INTMIN = 0
    RAMEN_INTMAX = 100

    multipersistent = MultiPersistent('tacoen.itch.io')
    
    if persistent.files is None or RAMEN_DEV:
        persistent.files = sorted(renpy.list_files(False))    

init -299 python:

    config.label_callback = ramu.labelcallback

    pe = ramen_persistent('env')

    pe.theme_path = 'theme/'
    pe.plugins_path = 'plugins/'
    
    pe.itemd = {
        'name': None,
        'price': int(0),
        'count': int(1),
        'desc': str(''),
        'eatable': False,
        'require': None,
        'effect': None,
        'persist': False,
        'tradable': True,
    }

    ramen.objects = {}    
    ramen.items=object()
    
    ramen.time_ico = ['moon2','moon3','sun1','sun2','sun2','sun3','moon1','moon2']
    ramen.time_cond = ['dark','dark','sun1','sun2','sun2','sun3','dark','dark']
    ramen.time_word = ['Midnight','Morning','Morning','Noon','Noon','Evening','Evening','Night']

    mc = ramen_multipersistent('mc',a=1)
    
    config.layers = ['master', 'transient', 'ambient', 'screens', 'overlay', 'overlay2','console', 'dialog_layer']


