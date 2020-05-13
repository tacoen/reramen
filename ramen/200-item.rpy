init -200 python:

    class itemobject(object):
        """itemobject handler class"""
        
        def __init__(self,id,**kwargs):
        
            for k in kwargs: 
                self.__dict__[str(k)] = kwargs[k]
            
            self.__dict__['id'] = id
            
            try: self.__dict__['dir']
            except: self.__dict__['dir'] = ramu.getdir()

            try: self.__dict__['name']
            except: self.__dict__['name'] = id.title()
            
            try: ramen.objects[self.__class__.__name__]
            
            except: ramen.objects[self.__class__.__name__]=[]
            ramen.objects[self.__class__.__name__].append(self.id)

        def __call__(self):
            res = self.__dict__.copy()
            for k in pe.itemd.keys():
                try:
                    res[k]
                except BaseException:
                    res[k] = pe.itemd[k]
            return res
            
        def set(self, key, value):
            if key in pe.itemd.keys():
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
                    return pe.itemd[key]
                except BaseException:
                    return None

        def copy(self):
            copies = object()
            copies.__dict__ = copy.copy(self.__call__())
            return copies

        def icon(self, size=(100, 100), color=None):
            """
            Return or generate the icon of your item.
            Put your icon_img.png within the directory where the item being define or set the `dir`.
            """
            
            
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
                    (8, 8), Text(icon_text, font=pt.font_ui_text,
                                 color='#fff', size=24, kerning=-1)
                )
                
            return icon

    def item(id):
        """Return item from `ramen.items` by their id."""
        return ramen.items.__dict__[id]
    
    class define_item(object):
        """ 
        Define new item 

        ``` python
        define_item('coke',name='fake cola',price=10,count=1)    
        item('coke')
        ```

        * The default arguments where set in `pe.itemd`
        * Item will store in `ramen.items`

        """
        def __new__(cls, id=None, *args, **kwargs):
            
            if id is None:
                id = item+ "_" + str(ramen.uid())        

            id = ramu.safestr(id)
            
            ramen.items.__dict__[id] = itemobject(id,**kwargs)
