init -202 python:

    pt.about.append('Feather Icon (C) Cole Bemis. License MIT')

    if persistent.icon is None:

        persistent.icon = {
            'alert': u'\x71',
            'arrow-down': u'\x77',
            'arrow-down-left': u'\x65',
            'arrow-down-right': u'\x72',
            'arrow-left': u'\x74',
            'arrow-right': u'\x79',
            'arrow-up': u'\x75',
            'arrow-up-left': u'\x69',
            'arrow-up-right': u'\x6f',
            'chevron-left': u'\x26',
            'chevron-right': u'\x2a',
            'chevrons-down': u'\x70',
            'chevrons-left': u'\x61',
            'chevrons-right': u'\x73',
            'chevrons-up': u'\x64',
            'circle': u'\x66',
            'circle-check': u'\x67',
            'click-left': u'\x68',
            'click-right': u'\x6a',
            'close': u'\x6b',
            'folder': u'\x6c',
            'folder-qload': u'\x7a',
            'folder-qsave': u'\x78',
            'ico-archive': u'\x63',
            'ico-bag': u'\x76',
            'ico-box': u'\x62',
            'ico-box2': u'\x6e',
            'ico-briefcase': u'\x6d',
            'ico-bulb': u'\x51',
            'ico-cart': u'\x57',
            'ico-cash': u'\x21',
            'ico-coins': u'\x45',
            'ico-disk': u'\x52',
            'ico-map': u'\x25',
            'ico-phone': u'\x40',
            'ico-settings': u'\x54',
            'ico-tool': u'\x59',
            'ico-wallet': u'\x23',
            'inbox': u'\x55',
            'key-back': u'\x49',
            'key-fast': u'\x4f',
            'key-forward': u'\x50',
            'key-pause': u'\x41',
            'key-play': u'\x53',
            'log-down': u'\x44',
            'log-in': u'\x29',
            'log-in2': u'\x46',
            'log-out': u'\x28',
            'log-out2': u'\x47',
            'log-up': u'\x48',
            'logo-python': u'\x24',
            'logo-ramen': u'\x4a',
            'menu': u'\x4b',
            'menu-small': u'\x4c',
            'menu1': u'\x5a',
            'moon1': u'\x58',
            'moon2': u'\x43',
            'moon3': u'\x56',
            'more-horizontal': u'\x42',
            'more-vertical': u'\x4e',
            'phone': u'\x4d',
            'phone-call': u'\x2c',
            'phone-incoming': u'\x2e',
            'phone-outgoing': u'\x2f',
            'phone-x': u'\x27',
            'sliders': u'\x3b',
            'square': u'\x5b',
            'square-check': u'\x5d',
            'square-edit': u'\x5e',
            'square-minus': u'\x31',
            'square-plus': u'\x32',
            'square-x': u'\x33',
            'star': u'\x34',
            'sun1': u'\x35',
            'sun2': u'\x36',
            'sun3': u'\x37',
            'terminal': u'\xe901',
            'toggle-left': u'\x38',
            'toggle-right': u'\x39',
            'volume-off': u'\x30',
            'volume-on': u'\x60',
            'volume-x': u'\x7e'
        }



    
    def ico(what=None, say=False):
        """ Translate Ramen Icon Webfont, see demo.html in the 'fonts/icon' for the list"""

        if what is None:
            return sorted(persistent.icon)
        else:
            try:
                if say:
                    return "{font=" +  pt.font_ui_ico +"}"+persistent.icon[what]+"{/font}"
                else:
                    return persistent.icon[what]
            except BaseException:
                return " "