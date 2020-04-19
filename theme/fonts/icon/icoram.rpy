##
#  @file ramen_icon.rpy
#  @brief Provide Webfont icons like CSS3. ramen_icon is generated using Icomoon apps, https://icomoon.io/app/. Designer: Cole Bemis, License: MIT
#
#

init -297 python:

    def ico(what=None,say=False):
        """ Translate Ramen Icon Webfont, see demo.html in the 'fonts/icon' for the list"""
        i={
            'alert': u'\x2b',
            'arrow-down': u'\x32',
            'arrow-down-left': u'\x31',
            'arrow-down-right': u'\x33',
            'arrow-left': u'\x34',
            'arrow-right': u'\x35',
            'arrow-up': u'\x38',
            'arrow-up-left': u'\x36',
            'arrow-up-right': u'\x37',
            'briefcase': u'\x42',
            'building': u'\x3d',
            'check': u'\x43',
            'check-square': u'\x76',
            'chevron-down': u'\x21',
            'chevron-left': u'\x39',
            'chevron-right': u'\x30',
            'chevron-up': u'\x40',
            'chevrons-down': u'\x24',
            'chevrons-left': u'\x25',
            'chevrons-right': u'\x5e',
            'chevrons-up': u'\x26',
            'close': u'\x58',
            'exit': u'\x29',
            'github': u'\x47',
            'globe': u'\x4f',
            'heart': u'\x3a',
            'heart-outline': u'\x3b',
            'help': u'\x2a',
            'home': u'\x2d',
            'home-o': u'\x5f',
            'info': u'\x28',
            'lightbulb': u'\x77',
            'list': u'\x3e',
            'log-down': u'\x60',
            'log-in': u'\x5d',
            'log-out': u'\x5b',
            'log-up': u'\x7e',
            'map-o': u'\x4d',
            'menu': u'\x3c',
            'messages': u'\x75',
            'minus-square': u'\x79',
            'more-horizontal': u'\x69',
            'more-vertical': u'\x49',
            'mouse-lc': u'\x6f',
            'mouse-rc': u'\x73',
            'phone': u'\x50',
            'phone-call': u'\x56',
            'pin': u'\x4c',
            'plus-square': u'\x7a',
            'python': u'\x70',
            'radio_off': u'\x2c',
            'radio_on': u'\x2e',
            'road': u'\x5a',
            'save': u'\x2f',
            'settings': u'\x7c',
            'shield': u'\x6a',
            'shopping-bag': u'\x53',
            'shopping-cart': u'\x72',
            'square': u'\x71',
            'stack': u'\x44',
            'sun1': u'\x64',
            'sun2': u'\x61',
            'sun3': u'\x63',
            'sun4': u'\x6d',
            'sun5': u'\x67',
            'sun6': u'\x65',
            'thumbs-down': u'\x6b',
            'thumbs-up': u'\x6c',
            'toggle-left': u'\x54',
            'toggle-right': u'\x74',
            'user': u'\x55',
            'wallet': u'\x57',
            'weather1': u'\x62',
            'weather2': u'\x66',
            'weather3': u'\x68',
            'x': u'\x58',
            'x-square': u'\x78',
        }
        
        if what is None:
            return sorted(i)
        else:
            try:
                if say:
                    return "{font="+ font.ui_ico+"}"+i[what]+"{/font}"
                else:
                    return i[what]
            except:
                return " "