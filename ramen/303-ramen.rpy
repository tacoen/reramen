init -303 python in character:
    pass

init -303 python in ramen:
    pass
    
init -303 python:

    class ramen_object(object):

        """ ramen_object is object() with function """

        def __init__(self,**kwargs):
            self.kdict(**kwargs)

        def get(self,key):
            try: return self.__dict__[key]
            except: return None

        def set(self,key,value):
            self.__dict__[str(key)]=value

        def kdict(self,key=None,**kwargs):
            if key is None:
                for k in kwargs:
                    self.set(str(k),kwargs[k])
            else:
                self.set(str(key),kwargs)

        def __getattr__(self,key):
            return self.get(key)

        def __setattr__(self,key,value):
            self.set(key,value)

        def __repr__(self):
            return '<'+self.__module__+":"+self.__class__.__name__+'>'

        def __call__(self):
            return self.__dict__

        def __delattr__(self,key):
            del self.__dict__[key]

        def makeid(self,id=None):
            if id is None:
                self.__dict__[str('id')]= self.__class__.__name__+ramu.uid()
            else:
                self.__dict__[str('id')]=str(id)

        def setdir(self,path=None):

            if path is None:
                path = ramu.getdir()

            try:
                self.__dict__['dir']
                if isinstance(self.__dict__['dir'],(str,unicode)):
                    dir_str = self.__dict__['dir']
                    self.__dict__[str('dir')]=[]
                    self.__dict__[str('dir')].append(dir_str)

            except: self.__dict__[str('dir')]=[]

            self.__dict__[str('dir')].append(path)


        def init(self,id=None,*args,**kwargs):
            pass

    class ramen_persistent(ramen_object):
        """
        Ramen_persistent is renpy persistent store for ramen's game enviroment.

        ``` python
        pe = ramen_persistent('env')
        pe.font = 'dejavu.ttf'
        ```
        * pe.font equal persistent.ramen['env']['font']

        """

        def __init__(self,id=None,**kwargs):

            self.makeid(id)

            if persistent.ramen is None:
                persistent.ramen = {}

            persistent.ramen[self.id] = {}

            self.kdict(**kwargs)

        def get(self,key):
            try: return persistent.ramen[self.id][key]
            except: return False

        def set(self,key,value):
            """Only Set if ramen.dev is True"""
            
            try: 
                persistent.ramen[self.id][key]
                
                if ramen.dev:
                    persistent.ramen[self.id][str(key)]=value
                else:
                    pass
                    
            except:
                pass
                persistent.ramen[self.id][str(key)]=value

        def __call__(self):
            return persistent.ramen[self.id]

        def __delattr__(self,key):
            del persistent.ramen[self.id][key]

    class ramen_multipersistent(ramen_object):
        """
        ramen_mutlipersistent is renpy multi persistent store for ramen's game progress.

        A chracter universe of the GAME_URI.

        ``` python
        multipersistent = MultiPersistent('tacoen.itch.io')

        mc.stat = ramen_multipersistent('stat')
        mc.stat.vital = 9
        ```

        * multipersistent equal MultiPersistent(GAME_URI)
        * mc.stat.vital equal multipersistent.__dict__['stat']['vital']

        """
        def __init__(self,id=None,**kwargs):

            if id is None:
                id = 'mp'+ramu.uid()

            try:
                multipersistent.__dict__[id]
            except:
                multipersistent.__dict__[str(id)]={}

            self.makeid(id)

            self.kdict(**kwargs)

        def set(self,key,value):
            multipersistent.__dict__[self.id][str(key)] = value

        def get(self,key):
            return multipersistent.__dict__[self.id][key]

        def __call__(self):
            return multipersistent.__dict__[self.id]

        def __delattr__(self,key):
            del multipersistent.__dict__[self.id][key]

    class ramen_extendable(ramen_object):

        def __init__(self, id=None, *args, **kwargs):
            self.makeid(id)
            self.register()
            self.kdict(**kwargs)
            self.setdir(ramu.getdir())
            self.init(id, *args, **kwargs)

        def register(self):
            try: ramen.objects[self.__class__.__name__]
            except: ramen.objects[self.__class__.__name__]=[]
            ramen.objects[self.__class__.__name__].append(self.id)

        def extend(self):
            self.setdir(ramu.getdir())

