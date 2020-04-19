init -310:

    # all screen/style and tranform needed before the ramen function

    screen test_image(img):
        add img xalign 0.5 yalign 0.5

init -301 python:

    class ramen_util():

        def test_image(self, img):
            renpy.show_screen('test_image', img=img)

        def kwdict(self, **kwargs):
            d = {}
            for k in kwargs:
                d[str(k)] = kwargs[k]
            return d

        def styleref(self, what=None):
            styleprop = []
            for s in dir(style.default):
                if not s.startswith('_'):
                    if what is not None:
                        if what in s:
                            styleprop.append(s)
                    else:
                        styleprop.append(s)
            return sorted(styleprop)

        def style(self, id, key=None, val=None, **kwargs):

            if val is None:
                val = self.kwdict(**kwargs)

            try:
                style[id]
            except BaseException:
                style[id] = Style(style.default)

            if key is not None:
                holder = style[id][key]
            else:
                holder = style[id]

            try:
                holder.xpos = val['x']
                del val['x']
            except BaseException:
                pass
            try:
                holder.ypos = val['y']
                del val['y']
            except BaseException:
                pass

            try:
                holder.xsize = val['w']
                del val['w']
            except BaseException:
                pass

            try:
                holder.ysize = val['h']
                del val['h']
            except BaseException:
                pass

            try:
                holder.padding = val['p']
                del val['p']
            except BaseException:
                pass

            for s in self.styleref():
                try:
                    setattr(holder, s, val[s])
                    del val[s]
                except BaseException:
                    pass

            for v in val:

                if not isinstance(val[v], (str, int, unicode, tuple)):
                    self.style(id, v, val[v])

        def getdir(self):
            return re.sub(
                r'^game/', '', os.path.dirname(renpy.get_filename_line()[0])) + "/"

        def files(self, where=False, key=False, ext=False):
            """
            Return file list from `persisten.files`

            ``` python
                file = ramu.files('gui','bar','png')
            ```

            * return files inside 'gui/' which has 'bar' in filename(including his path), and end with 'png'
            * ramen's framework work best with namespaces in mind.

            """

            F = persistent.files
            if where:
                F = filter(lambda w: where + "/" in w, sorted(F))
            if key:
                F = filter(lambda w: key in w, F)
            if ext:
                F = filter(lambda w: w.endswith(ext), F)

            return F

        def ezfile(self, file, ext=RAMEN_IMG_EXT):

            for e in ext:
                if renpy.loadable(file + e):
                    return file + e
            else:
                return None

        def old_file_info(self, file):
            r = {}
            r[str('path')] = os.path.dirname(file)
            r[str('file')] = os.path.basename(file)
            a = r['file'].split('.')
            r[str('name')] = str(a[0])
            r[str('ext')] = str(a[1])
            r[str('dir')] = str(r['path'])
            r[str('path')] = r['path'].replace(
                os.path.dirname(r['path']) + "/", '')
            return r

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

        def limits(self, value, min=RAMEN_INTMIN, max=RAMEN_INTMAX):
            if int(value) < min:
                return min
            elif int(value) > max:
                return max
            else:
                return int(value)

        def toggle(self, what):

            if what is None:
                what = False

            if what:
                return False
            else:
                return True

        def cycle(self, current, array):
            current = int(current) + 1
            if current >= len(array) or current < 0:
                current = 0
            return int(current)

        def random_int(self, min=0, max=100):
            return int(renpy.random.randint(min, max))

        def random_of(self, array):
            return array[int(renpy.random.randint(0, len(array) - 1))]

        def random_color(self, lo=0, hi=255):
            """Return random hex Color"""
            if lo < 96:
                lo = 96
            if hi > 255:
                hi = 255

            def r(): return self.random_int(lo, hi)
            return ('#%02X%02X%02X' % (r(), r(), r()))

        def safestr(self, str=''):
            return re.sub(r'\W+', '', str.lower())

        def character(self, id, name=None, **kwargs):
            """Define character"""
            
            if name is None:
                name = id.title()
                
            chaattr = {}
            
            for k in kwargs:
                for c in ['dynamic', 'window_', 'who_',
                          'what_', 'show_', 'cb_', 'ctc_']:
                    if k.startswith(c):
                        chaattr[k] = kwargs[k]

            setattr(
                character,
                id,
                Character(
                    name,
                    image=id,
                    **chaattr
                )
            )

        def labelcallback(self, name, abnormal):

            if not name.startswith('ramen_'):
                ramen.last_label = name

    ramu = ramen_util()

    config.label_callback = ramu.labelcallback
