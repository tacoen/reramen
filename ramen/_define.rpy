init -304 python:

    multipersistent = MultiPersistent('tacoen.itch.io')

init -302 python:

    pe = ramen_persistent('env')
    pe.theme_path = 'theme/'
    pe.plugins_path = 'plugins/'
    pe.image_path = 'images/'
    pe.time_ico = [
        'moon2',
        'moon3',
        'sun1',
        'sun2',
        'sun2',
        'sun3',
        'moon1',
        'moon2']
    pe.time_cond = [
        'dark',
        'dark',
        'sun1',
        'sun2',
        'sun2',
        'sun3',
        'dark',
        'dark']
    pe.time_word = [
        'Midnight',
        'Morning',
        'Morning',
        'Noon',
        'Noon',
        'Evening',
        'Evening',
        'Night']
    pe.ext_img = ('.webp', '.png', '.jpg')
    pe.ext_txt = ('.json', '.txt')
    pe.ext_snd = ('.ogg', '.mp3', '.wav')

    pe.limit = (0, 20)

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


init -300 python:

    ramentime = ramen_time()
    ramu = ramen_util()
    ramen.uidnumber = 0
    ramen.objects = {}
    ramen.items = object()
    ramen.seed = datetime.timedelta(0, 0)

    ramen.smphone = False
    ramen.episode_menu = False

    if persistent.files is None or ramen.dev:
        persistent.files = sorted(renpy.list_files(False))

    config.label_callback = ramu.labelcallback
    config.layers = [
        'master',
        'transient',
        'screens',
        'overlay',
        'overlay2',
        'console',
        'dialog_layer']


init -100 python:

    mc_name = 'You'
    character.mc = Character('mc_name', dynamic=True, who_color='#ff0')

    narrator = Character(None, window_background="#0000",
                         what_xalign=0.5, what_color="#ddf", what_outlines=pt.bold_outlines
                         )

    chapter = Character(None,
                        window_xalign=0.9,
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
