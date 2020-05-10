init -302 python in character:
    pass

init -302 python in ramen:
    pass

init -301 python:
    class time_class():
        """
        See: https://docs.python.org/2/library/datetime.html
        See: https://www.w3schools.com/python/python_datetime.asp
        """

        def __init__(self, y=2020, m=1, d=18, h=13, min=0):
            self.time = datetime.datetime(y, m, d, h, min)
            self.start = self.time

        def __call__(self):
            return self.time

        def __getattr__(self, key):
            res = getattr(self.time, key)
            if isinstance(res,(int,str,unicode)):
                return res
            else:
                try: return res()
                except: return res

        def adv(self, a=1, block=False):
            self.time = self.time + datetime.timedelta(hours=a)
            self.populate()
            if block:
                renpy.block_rollback()
            return self.time

        def nextday(self, a=8, block=False):
            b = 24 - self.time.hour
            self.time = self.time + datetime.timedelta(hours=b) + datetime.timedelta(hours=a)
            self.populate()
            if block:
                renpy.block_rollback()
            return self.time

        def populate(self):
            global seed
            seed = self.time - self.start

        def clock(self):
            return self.time.strftime('%H:%M')

        def ico(self,word=True):
            sun = int( float(self.time.hour)/24*len(ramen.time_ico) )
            if word:
                return ramen.time_ico[int(sun)]
            else:
                return sun

        def cond(self,word=True):
            sun = int( float(self.time.hour)/24*len(ramen.time_cond))
            if word:
                return ramen.time_cond[int(sun)]
            else:
                return sun

        def word(self,word=True):
            sun = int( float(self.time.hour)/24*len(ramen.time_word) )
            if word:
                return ramen.time_word[int(sun)]
            else:
                return sun

    class ramen_util():

        def mouse(self):
            """Get Mouse pos, return (x,y)"""
            return pygame.mouse.get_pos()
        
        def uid(self):
            """Return Next Unique id for object creations."""
            ramen.uidnumber += 1
            return "{:03d}".format(ramen.uidnumber)

        def makeobj(self, args, **kwargs):
            obj = object()
            obj.__dict__= kwargs
            if isinstance(args,type({})):
                for a in args:
                    obj.__dict__[str(a)]=args[a]
            return obj

        def labelcallback(self, name, abnormal):
            if not name.startswith('ramen_') or not name.startswith("_"):
                ramen.last_label = name

        def cycle(self, current, array):
            current = int(current) + 1
            if current >= len(array) or current < 0:
                current = 0
            return int(current)

        def safestr(self,name):
            return re.sub(r'\W+|\s+','',name).lower().strip()

        def random_int(self, min=0, max=100):
            return int(renpy.random.randint(min, max))

        def random_of(self, array):
            return array[int(renpy.random.randint(0, len(array) - 1))]

        def nice_cash(self,n):
            if n <1000:
                return ("{:03d}".format(n))
            elif n>1000:
                return ("{:0.1f}".format(n/1000))+"K"

        def nicenaming(self,name,prefix='',suffix=''):
            pre=[]
            suf=[]

            ori = name

            if not isinstance(prefix,tuple):
                pre.append(prefix)
            else:
                pre = prefix

            if not isinstance(suffix,tuple):
                pre.append(suffix)
            else:
                pre = suffix

            for p in pre:
                name = name.replace(p,'')
            for s in suf:
                name = name.replace(s,'')

            return name.replace('_', ' ').strip().title()

        def random_color(self, lo=0, hi=255):
            """Return random hex Color"""
            if lo < 96:
                lo = 96
            if hi > 255:
                hi = 255

            def r(): return self.random_int(lo, hi)
            return ('#%02X%02X%02X' % (r(), r(), r()))

        def invertColor(self,hexColor):
            def invertHex(hexNumber):
                inverse = hex(abs(int(hexNumber, 16) - 255))[2:]
                if len(inverse) == 1:
                    inverse = '0'+inverse
                return inverse

            inverse = ""
            hexCode = Color(hexColor).hexcode[1:]

            A=""

            if len(hexCode) == 3:
                R = hexCode[0]+hexCode[0]
                G = hexCode[1]+hexCode[1]
                B = hexCode[2]+hexCode[2]

            elif len(hexCode) == 4:
                R = hexCode[0]+hexCode[0]
                G = hexCode[1]+hexCode[1]
                B = hexCode[2]+hexCode[2]
                A = hexCode[3]+hexCode[3]

            elif len(hexCode) == 6:
                R = hexCode[:2]
                G = hexCode[2:4]
                B = hexCode[4:]

            elif len(hexCode) == 8:
                R = hexCode[:2]
                G = hexCode[2:4]
                B = hexCode[4:6]
                A = hexCode[6:]

            inverse = "#"+ invertHex(R) + invertHex(G) + invertHex(B)

            return inverse

        def hline(self,(size),color='#fff'):
            return Composite((size), (0,0),Solid(color))

        def img_hover(self, img, hover_color=None, size=(100,100)):

            if hover_color is None:
                hover_color = gui.hover_color;

            return Composite(
                size,
                (0, 0), Solid(Color(hover_color).opacity(.5)),
                (0, 0), img
                )

        # files

        def getdir(self):
            return re.sub(
                r'^game/', '', os.path.dirname(renpy.get_filename_line()[0])) + "/"

        def files(self, dir=False, key=False, ext=False):
            """
            Return file list from `persisten.files`

            ``` python
                file = ramu.files(['gui','img'],'bar','png')
            ```

            * return files inside 'gui/' and 'img/' which has 'bar' in filename(including his path), and end with 'png'
            * ramen's framework work best with namespaces in mind.

            """

            F = persistent.files
            dirs = []

            if dir:
                if isinstance(dir,(str,unicode)):
                    dirs.append(dir)
                else:
                    dirs = dir

                for dir in dirs:
                    F = filter(lambda w: dir in w, sorted(F))

            if key:
                F = filter(lambda w: key in w, F)

            if ext:
                F = filter(lambda w: w.endswith(ext), F)

            return  list(dict.fromkeys(F))

        def ezfile2(self, file, default=Color("#0019"), ext=RAMEN_IMG_EXT):

            for e in ext:
                if renpy.loadable(file + e):
                    return file + e
            else:
                return default

        def ezfile(self, file, ext=RAMEN_IMG_EXT):

            for e in ext:
                if renpy.loadable(file + e):
                    return file + e
            else:
                return None

        def file_info(self, file):
            """
            Get and extract the file information of the file as dict.

            ``` python:
                info = ramu.file_info("e:/yourproject/game/npc/girls_of_90/alpha/lucy smile.png")
            ```

            * info.file = lucy smile.png
            * info.name = lucy smile
            * info.ext = png
            * info.dir = npc/girl_of_90
            * info.path = alpha

            Note: `dir` and `path` doesn't had trailing slash.

            """

            r = object()
            r.__dict__[str('path')] = os.path.dirname(file)
            r.__dict__[str('file')] = os.path.basename(file)
            a = r.__dict__['file'].split('.')
            r.__dict__[str('name')] = str(a[0])
            r.__dict__[str('ext')] = str(a[1])
            r.__dict__[str('dir')] = str(r.__dict__['path'])
            r.__dict__[str('path')] = r.__dict__['path'].replace(
                os.path.dirname(r.__dict__['path']) + "/", '')

            return r

        def file_write(self, file, sts):
            file = open(file, "w")
            file.writelines(sts.strip())
            file.close()
            return file

        def character(self, id, name=None, **kwargs):
            """Define character"""

            if name is None:
                name = id.title()

            chaattr = {}
            p = []
            for k in kwargs:
                if k.startswith(('dynamic', 'window_', 'who_','what_', 'show_', 'cb_', 'ctc_')):
                    chaattr[k] = kwargs[k]
                    p.append(k)

            setattr(
                character,
                id,
                Character(
                    name,
                    image=id,
                    **chaattr
                )
            )

            return p
