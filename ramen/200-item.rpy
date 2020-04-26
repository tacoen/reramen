init -200 python:

    ramen.defvalue = {
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

    ramen.items=object()

    class itemobject(object):
    
        def __init__(self,id,**kwargs):
        
            for k in kwargs: 
                self.__dict__[str(k)] = kwargs[k]
            
            self.__dict__['id'] = id
            
            try: self.__dict__['dir']
            except: self.__dict__['dir'] = ramu.getdir()

            try: self.__dict__['name']
            except: self.__dict__['name'] = id.title()

        def __call__(self):
            res = self.__dict__
            for k in ramen.defvalue.keys():
                try:
                    res[k]
                except BaseException:
                    res[k] = ramen.defvalue[k]
            return res
            
        def set(self, key, value):
            if key in ramen.defvalue.keys():
                self.__dict__[key] = value

        def __setattr__(self, key, value):
            self.set(key, value)

        def get(self, key):
            try:
                return self.__dict__[key]
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

        def icon(self, size=(100, 100), color=None):

            icon = self.get('img')

            if icon is None:
                icon = ramu.ezfile(self.dir + self.id)

            if icon is not None:
                icon = im.Scale(icon,size[0],size[1])

            else:
            
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

    def item(id):
        return ramen.items.__dict__[id]
    
    class define_item(object):
        def __new__(cls, id=None, *args, **kwargs):
            
            if id is None:
                id = self.__class__.__name__ + "_" + str(ramen.uid())        

            id = ramu.safestr(id)
            
            ramen.items.__dict__[id] = itemobject(id,**kwargs)
            
    class item_old(object):

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

        def icon(self, size=(100, 100), color=None):

            icon = self.get('img')

            if icon is None:
                icon = ramu.ezfile(self.dir + self.id)

            if icon is not None:
                icon = im.Scale(icon,size[0],size[1])

            else:
            
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
