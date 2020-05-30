init -303 python in character:
    pass

init -303 python in ramen:
    pass

init -303 python:

    class ramen_object(object):

        """ ramen_object is object() with function """

        def __init__(self, **kwargs):
            self.kdict(**kwargs)

        def _get(self, key):
            try:
                return self.__dict__[key]
            except BaseException:
                return None

        def _set(self, key, value):
            self.__dict__[str(key)] = value

        def kdict(self, key=None, **kwargs):
            if key is None:
                for k in kwargs:
                    self._set(str(k), kwargs[k])
            else:
                self._set(str(key), kwargs)

        def __getattr__(self, key):
            return self._get(key)

        def __setattr__(self, key, value):
            self._set(key, value)

        def __repr__(self):
            return '<' + self.__module__ + ":" + self.__class__.__name__ + '>'

        def __call__(self):
            return self.__dict__

        def __delattr__(self, key):
            del self.__dict__[key]

        def makeid(self, id=None):
            if id is None:
                self.__dict__[str('id')] = self.__class__.__name__ + ramu.uid()
            else:
                self.__dict__[str('id')] = str(id)

        def setdir(self, path=None):

            if path is None:
                path = ramu.getdir()

            try:
                self.__dict__['dir']
                if isinstance(self.__dict__['dir'], (str, unicode)):
                    dir_str = self.__dict__['dir']
                    self.__dict__[str('dir')] = []
                    self.__dict__[str('dir')].append(dir_str)

            except BaseException:
                self.__dict__[str('dir')] = []

            self.__dict__[str('dir')].append(path)

        def find(self, file, ext=('.webp', '.png', '.jpg')):

            for d in range(0,len(self.dir)):
                f = ramu.ezfile(self.dir[d]+file,None,ext)
                if f is not None:
                    return f
                    break

            if f is None:
                return False

        def init(self, id=None, *args, **kwargs):
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

        def __init__(self, id=None, **kwargs):

            self.makeid(id)

            if persistent.ramen is None:
                persistent.ramen = {}

            persistent.ramen[self.id] = {}

            self.kdict(**kwargs)

        def _get(self, key):
            try:
                return persistent.ramen[self.id][key]
            except BaseException:
                return False

        def _set(self, key, value):
            """Only Set if ramen.dev is True"""

            try:
                persistent.ramen[self.id][key]

                if ramen.dev:
                    persistent.ramen[self.id][str(key)] = value
                else:
                    pass

            except BaseException:
                pass
                persistent.ramen[self.id][str(key)] = value

        def __call__(self):
            return persistent.ramen[self.id]

        def __delattr__(self, key):
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

        def __init__(self, id=None, **kwargs):

            if id is None:
                id = 'mp' + ramu.uid()

            try:
                multipersistent.__dict__[id]
            except BaseException:
                multipersistent.__dict__[str(id)] = {}

            self.makeid(id)

            self.kdict(**kwargs)

        def _set(self, key, value):
            multipersistent.__dict__[self.id][str(key)] = value

        def _get(self, key):
            return multipersistent.__dict__[self.id][key]

        def __call__(self):
            return multipersistent.__dict__[self.id]

        def __delattr__(self, key):
            del multipersistent.__dict__[self.id][key]

    class ramen_extendable(ramen_object):

        def __init__(self, id=None, *args, **kwargs):
            """ramen_object extended with `id` and `dir`, and can be chained with `init`"""
            self.makeid(id)
            self.ro_register()
            self.setdir(ramu.getdir())

            self.kdict(**kwargs)
            self.init(id, *args, **kwargs)

        def exist(self,what,key):
            try:
                self.__dict__[what][k]
                res=True
            except:
                res=False

            return res

        def ro_register(self):
            """ all ramen_extendable object are registered on `ramen.object`"""
            try:
                ramen.objects[self.__class__.__name__]
            except BaseException:
                ramen.objects[self.__class__.__name__] = []
            ramen.objects[self.__class__.__name__].append(self.id)

        def reinit(self):
            pass

        def extend(self):
            """extend the ramen_object to the directory"""
            self.setdir(ramu.getdir())
            self.reinit()
