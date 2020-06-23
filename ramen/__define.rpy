init -302 python:

    ramen_version_name = 'RE-01'

    pe = ramen_persistent('env')
    pe.theme_path = 'theme/'
    pe.title_path = 'title/'
    pe.plugins_path = 'plugins/'
    pe.image_path = 'images/'

    pe.audio_path = 'audio/'

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
        'night',
        'dark']
    pe.time_word = [
        'Midnight',
        'Dusk',
        'Morning',
        'Noon',
        'Noon',
        'Evening',
        'Night',
        'Night']
    pe.ext_img = ('.webp', '.png', '.jpg')
    pe.ext_txt = ('.json', '.txt')
    pe.ext_snd = ('.ogg', '.mp3', '.wav')
    pe.ext_vid = ('.webm', '.ogv', '.mp4')

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

    ramu = ramen_util()
    ramen.uidnumber = 0
    ramen.objects = {}
    ramen.items = object()

    ramentime = ramen_time(2018, 1, 18, 12, 0)
    pe.time_block_rollback = False

    ramen.label_trace = ['start']

    ramen.smphone = False
    ramen.episode_menu = False

    if persistent.files is None or ramen.dev:
        persistent.files = sorted(renpy.list_files(False))

    config.label_callback = ramu.label_callback

    config.layers = [
        'master',
        'transient',
        'scenes',
        'ambients',
        'screens',
        'overlay',
        'console',
        'dialog_layer']

    config.transient_layers = [ 'transient' ]

init -100 python:

    mc_name = 'You'

    character.mc = Character('mc_name', dynamic=True, who_color='#ff0')

    anon = Character('anon_name', dynamic=True, who_color=ramu.random_color(100, 200))

    narrator = Character(None, window_background="#0000",
                         what_xalign=0.5, what_color="#ddf", what_outlines=pt.bold_outlines
                         )

    sysnote = Character(None,
                        window_background="#0000",
                        window_xalign=0.5,
                        window_yalign=0.5,
                        window_xsize=config.screen_width,
                        window_ysize=None,
                        window_padding=(0, 0, 0, 0),
                        what_yalign=0.5,
                        what_xalign=0.5,
                        what_text_align=0.5,
                        what_size=18)
