init -202 python:

    pt.about.append('Feather Icon (C) Cole Bemis. License MIT')

    # Delete persistent if you made a change!
    # keyword, hex
    # it's Standard character set (32 - 127)
    # Expiremnting: Extended character set (128 - 255):
    # Also See : https://www.renpy.org/doc/html/text.html

    if persistent.icon is None:

        persistent.icon = {

            'alert': u'\x21',
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
            'click-left': u'\x68',
            'click-right': u'\x6a',
            'close': u'\x6b',
            'eye': u'\xa1',
            'folder': u'\x6c',
            'folder-qload': u'\x7a',
            'folder-qsave': u'\x78',
            'ico-archive': u'\x63',
            'ico-bag': u'\x76',
            'ico-box': u'\x62',
            'ico-box2': u'\x6e',
            'ico-briefcase': u'\x6d',
            'ico-building0': u'\xae',
            'ico-building1': u'\xa9',
            'ico-building2': u'\x22',
            'ico-building3': u'\x3e',
            'ico-building4': u'\xab',
            'ico-building5': u'\x20',
            'ico-bulb': u'\x51',
            'ico-cart': u'\x57',
            'ico-cash': u'\x24',
            'ico-coins': u'\x45',
            'ico-disk': u'\x52',
            'ico-gift': u'\xaa',
            'ico-home': u'\x3c',
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
            'key-stop': u'\x34',
            'list': u'\x7c',
            'log-down': u'\x44',
            'log-in': u'\x29',
            'log-in2': u'\x46',
            'log-out': u'\x28',
            'log-out2': u'\x47',
            'log-up': u'\x48',
            'logo-python': u'\x3f',
            'logo-ramen': u'\x4a',
            'logo-renpy': u'\x71',
            'map-pin1': u'\x7d',
            'map-pin2': u'\x3a',
            'menu': u'\x4b',
            'menu-small': u'\x4c',
            'menu1': u'\x5a',
            'monitor': u'\xa3',
            'moon1': u'\x58',
            'moon2': u'\x43',
            'moon3': u'\x56',
            'more-horizontal': u'\x42',
            'more-vertical': u'\x4e',
            'msg-forward': u'\x3d',
            'msg-mail': u'\x27',
            'msg-reply': u'\x2b',
            'phone': u'\x4d',
            'phone-call': u'\x2c',
            'phone-incoming': u'\x2e',
            'phone-outgoing': u'\x2f',
            'phone-x': u'\x2d',
            'radio-off': u'\x66',
            'radio-on': u'\x67',
            'sliders': u'\x3b',
            'square': u'\x5b',
            'square-check': u'\x5d',
            'square-edit': u'\x5e',
            'square-minus': u'\x31',
            'square-plus': u'\x32',
            'square-x': u'\x33',
            'sun1': u'\x35',
            'sun2': u'\x36',
            'sun3': u'\x37',
            'terminal': u'\x5c',
            'toggle-left': u'\x38',
            'toggle-right': u'\x39',
            'trash-0': u'\x5f',
            'trash-1': u'\x30',
            'user': u'\xfb',
            'user-min': u'\xff',
            'user-plus': u'\xd6',
            'user-rel': u'\xa2',
            'volume-off': u'\x60',
            'volume-on': u'\x7e',
            'volume-x': u'\x7f',
            'map-pin3': "{{"
        }

    def ico(what=None):
        r""" Translate Ramen Icon Webfont, see demo.html in the 'theme\icons' for the list"""

        if what is None:
            return sorted(persistent.icon)
        else:
            try:
                return persistent.icon[what]
            except BaseException:
                return " "
