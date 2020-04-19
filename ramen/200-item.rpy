init -200 python:

    ramen.defvalue = {
        'name': None,
        'price': int(0),
        'count': int(1),
        'desc': str('No descriptions given.'),
        'eatable': False,
        'require': None,
        'effect': None,
        'persist': False,
    }

    class item(object):

        def __init__(self, id=None, **kwargs):

            if id is None:
                id = self.__class__.__name__ + "_" + str(ramen.uid())

            id = ramu.safestr(id)
            self.__dict__[str('id')] = str(id)

            ramen_item[str(id)] = ramu.kwdict(**kwargs)

            try:
                ramen_item[id]['name']
            except BaseException:
                ramen_item[str(id)]['name'] = id

            try:
                ramen_item[id]['dir']
            except BaseException:
                ramen_item[str(id)][str('dir')] = ramu.getdir()

        def __call__(self):
            res = ramen_item[self.id]
            for k in ramen.defvalue.keys():
                try:
                    res[k]
                except BaseException:
                    res[k] = ramen.defvalue[k]
            return res

        def set(self, key, value):
            if key in ramen.defvalue.keys():
                ramen_item[self.id][key] = value

        def __setattr__(self, key, value):
            self.set(key, value)

        def get(self, key):
            try:
                return ramen_item[self.id][key]
            except BaseException:
                return None

        def __getattr__(self, key):
            if self.get(key) is not None:
                return self.get(key)
            else:
                try:
                    return ramen.defvalue[key]
                except BaseException:
                    return None

        def copy(self):
            copies = object()
            copies.__dict__ = copy.copy(self.__call__())
            return copies

        def icon(self, size=(72, 72), color=None):

            icon = self.get('img')

            if icon is None:
                icon = ramu.ezfile(self.dir + self.id)

            if icon is None:
                it = self.name.lower().split('_')
                if len(it) > 1:
                    icon_text = (it[0][:1] + it[1][:1]).title()
                else:
                    icon_text = self.name[:2].title()

                if color is None:
                    color = Color(ramu.random_color(96, 192)).opacity(.8)

                icon = Composite(
                    size,
                    (0, 0), Solid(color),
                    (8, 8), Text(icon_text, font=font.ui_text,
                                 color='#fff', size=24, kerning=-1)
                )

            return icon
