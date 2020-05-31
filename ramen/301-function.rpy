init -301 python:

    class ramen_util():

        def menuof(self, label, screen='choice', exitword='Done', void=None, **condition):

            choices=[]
            last =''
            n = 1

            if void is None:
                void = ramen.label_last

            labels = filter(lambda w: w.startswith(label+'.'), list(renpy.get_all_labels()))

            for l in sorted(labels):
                caption = l.replace(label+'.', '')

                if caption in void or l in void:
                    continue

                if caption == last:
                    caption += str(n)
                    n += 1
                else:
                    last = caption

                if caption in condition.keys():
                    cond = condition[caption]
                else:
                    cond = True

                if cond:
                    caption = caption.replace('_', ' ')
                    choices.append((caption.title(), l))

            if exitword is not None:
                choices.append((exitword, False))

            res = renpy.display_menu(choices, interact=True, screen=screen)

            return res

        def pay(self, m, src, ret=False):
            if src > m:
                src -= m
                res = True
            else:
                res = False

            if ret:
                return res

        def gain(self, m, src, ret=False):
            src += m
            res = True

            if ret:
                return res

        def npc(self, npc_id, what):
            if type(globals()[npc_id]) is not ramen_npc:
                return False

            try:
                return globals()[npc_id]._get(what)
            except BaseException:
                return None

        def imgexpo(self, tag=None, what='size'):

            tags = list(renpy.get_showing_tags())

            if tag is None:
                tag = tags[-1]
            else:
                tag = tags[tags.index(tag)]

            try:
                attr = renpy.get_attributes(tag)[0]
                im = renpy.get_registered_image(tag+' '+attr).filename
            except BaseException:
                im = renpy.get_registered_image(tag).filename

            if what=='size':
                return renpy.image_size(im)
            if what=='bound':
                return renpy.get_image_bounds(tag)

            else:
                return im

        def limits(self, value):
            if value < pe.limit[0]:
                value = pe.limit[0]
            if value > pe.limit[1]:
                value = pe.limit[1]
            return value

        def mouse(self):
            """Get Mouse pos, return (x,y)"""
            return pygame.mouse.get_pos()

        def uid(self):
            """Return Next Unique id for object creations."""

            ramen.uidnumber += 1
            return "{:03d}".format(ramen.uidnumber)

        def makeobj(self, args, **kwargs):
            obj = object()
            obj.__dict__ = kwargs
            if isinstance(args, (type(self.__dict__), type({}))):
                for a in args:
                    obj.__dict__[str(a)] = args[a]
            return obj

        def label_callback(self, name, abnormal):

            if not name.startswith('ramen_') and \
                    not name.startswith("_") and \
                    not name.endswith('_screen') and \
                    not name=='after_load':

                if not name == ramen.label_trace[-1]:
                    ramen.label_trace.append(name)

                if len(ramen.label_trace)>10:
                    ramen.label_trace=ramen.label_trace[-9:]

                ramen.label_last = name

                if ramu.safestr(name) in ramen.events.__dict__.keys():
                    e = Event(ramu.safestr(name))
                    print e.occur()
                    if e.occur():
                        renpy.call(e.label)

        def cycle(self, current, array):
            current = int(current) + 1
            if current >= len(array) or current < 0:
                current = 0
            return int(current)

        def safestr(self, name):
            return re.sub(r'\W+|\s+', '', name).lower().strip()

        def capcap(self, title):
            res = ''
            tt = title.split(' ')
            for t in tt:
                res += t[0]
            return res.title()

        def random_int(self, min=0, max=100):
            return int(renpy.random.randint(min, max))

        def random_of(self, array):
            return array[int(renpy.random.randint(0, len(array) - 1))]

        def nice_cash(self, n):
            if n < 1000:
                return ("{:03d}".format(n))
            elif n > 1000:
                return ("{:0.1f}".format(n / 1000)) + "K"

        def nicenaming(self, name, prefix='', suffix=''):
            pre = []
            suf = []

            ori = name

            if not isinstance(prefix, tuple):
                pre.append(prefix)
            else:
                pre = prefix

            if not isinstance(suffix, tuple):
                suf.append(suffix)
            else:
                suf = suffix

            for p in pre:
                name = name.replace(p, '')
            for s in suf:
                name = name.replace(s, '')

            return name.replace('_', ' ').strip().title()

        def random_color(self, lo=0, hi=255):
            """Return random hex Color"""
            if lo < 96:
                lo = 96
            if hi > 255:
                hi = 255

            def r(): return self.random_int(lo, hi)
            return ('#%02X%02X%02X' % (r(), r(), r()))

        def invertColor(self, hexColor):
            def invertHex(hexNumber):
                inverse = hex(abs(int(hexNumber, 16) - 255))[2:]
                if len(inverse) == 1:
                    inverse = '0' + inverse
                return inverse

            inverse = ""
            hexCode = Color(hexColor).hexcode[1:]

            A = ""

            if len(hexCode) == 3:
                R = hexCode[0] + hexCode[0]
                G = hexCode[1] + hexCode[1]
                B = hexCode[2] + hexCode[2]

            elif len(hexCode) == 4:
                R = hexCode[0] + hexCode[0]
                G = hexCode[1] + hexCode[1]
                B = hexCode[2] + hexCode[2]
                A = hexCode[3] + hexCode[3]

            elif len(hexCode) == 6:
                R = hexCode[:2]
                G = hexCode[2:4]
                B = hexCode[4:]

            elif len(hexCode) == 8:
                R = hexCode[:2]
                G = hexCode[2:4]
                B = hexCode[4:6]
                A = hexCode[6:]

            inverse = "#" + invertHex(R) + invertHex(G) + invertHex(B)

            return inverse

        def hline(self, (size), color='#fff'):
            return Composite((size), (0, 0), Solid(color))

        def img_hover(self, img, hover_color=None, size=(100, 100)):

            if hover_color is None:
                hover_color = gui.hover_color

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

            FL = persistent.files
            dirs = []

            if dir:
                if isinstance(dir, (str, unicode)):
                    dirs.append(dir)
                else:
                    dirs = dir

                F=[]

                for dir in dirs:
                    fl = filter(lambda w: dir in w, sorted(FL))
                    F += fl
            else:
                F = persistent.files

            if key:
                F = filter(lambda w: key in w, F)

            if ext:
                F = filter(lambda w: w.endswith(ext), F)

            return list(dict.fromkeys(F))

        def random_files(self, dir=False, key=False, ext=pe.ext_img):
            files = self.files(dir, key, ext)
            return self.random_of(files)

        def ezfile(self, file, nonevalue=None, ext=pe.ext_img):
            """
            Get [file] within [ext] selection or return nonevalue

            ``` python
            obj.ezfile( "some/body", Color("#999"))
            ```

            * Search for `some/body` ('.webp', '.png', '.jpg')
            * if `some/body` not loadable, return Color("#999")
            * by default extension to search is `pe.ext_img`

            #### File Extension:

            * pe.ext_img = ('.webp', '.png', '.jpg')
            * pe.ext_txt = ('.json', '.txt')
            * pe.ext_snd = ('.ogg', '.mp3', '.wav')

            """
            for e in ext:
                if renpy.loadable(file + e):
                    return file + e
                    break
            else:
                return nonevalue

        def ezfind(self, file, ext='image', path=None):
            """

            ``` python
            ramu.ezfind('theme_song','sound')
            ```

            Search for 'theme_song' ('.ogg', '.mp3', '.wav') in sortorder:
            * path
            * pe.title_path
            * pe.theme_path+'audio/'
            * pe.audio_path

            ``` python
            ramu.ezfind('game','image')
            ```

            Search for 'game' ('.webp', '.png', '.jpg') in sortorder:
            * path
            * pe.title_path
            * pe.theme_path+'gui/'
            * pe.image_path

            """

            if ext == 'sound':
                find = [ pe.title_path, pe.theme_path+'audio/', pe.audio_path ]
                ext = pe.ext_snd
            else:
                ext = pe.ext_img
                find = [ pe.title_path, pe.theme_path+'gui/', pe.image_path ]

            if path is not None:
                find.insert(0, path)

            res = None

            for f in find:
                res = self.ezfile(f+file, None, ext)
                if res is not None:
                    break

            return res

        def sfx(self, file, path=None, channel='sound', **kwargs):

            res = self.ezfind(file, 'sound', path)

            if res is not None:
                renpy.sound.play(res, channel=channel, **kwargs)
            else:
                return False

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
                if k.startswith(('dynamic', 'window_', 'who_',
                                 'what_', 'show_', 'cb_', 'ctc_')):
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

        def talk(self, **kwargs):
            """
            Let npc and mc do a chat.

            ### Keyword arguments:

            | # | Key | Description |
            | --- | --- | --- |
            | 0 | npc_id | npc.id to talk with |
            | 1 | what | json topic / label |
            | 2 | type | json or label |
            | 3 | prefix | topic id / label prefix |

            #### Using Label

            ``` python
            $ ramu.talk('rita','chat','label','phone')
            ```

            Make a phone talk using label (fallback):

            * `if exist` rita.phone_chat
            * `if exist` rita_chat
            * `if exist` chat

            ``` python

            label rita:
                ...
                label .onphone_chat:
                    rita "Let's chat!"
                    mc "Ok!"
                    return

            ```

            #### Using Json file

            ``` python
            $ ramu.talk('rita','chat','json')
            ```

            * file chat.json must on rita npc's path,
            * `rita.json` must return that file
            * if no prefix suplied, the line will be randomize
            * In pairing. First Sayer is NPC, followed by MC. '' are muted.

            ``` chat.json

            {
                "1": ["[mc_name]? Hello", "Yes, [rita.name].",	"See ya!", "Ok." ],
                "2": ["What?", "Uh Nothing!" ],
                "3": ["Hello","", "Say something...","","No?" ],
            }

            ```

            """

            try:
                kwargs['npc_id']
            except BaseException:
                kwargs['npc_id'] = False

            try:
                kwargs['what']
            except BaseException:
                kwargs['what'] = None

            try:
                kwargs['type']
            except BaseException:
                kwargs['type'] = 'label'

            try:
                kwargs['prefix']
            except BaseException:
                kwargs['prefix'] = False

            if kwargs['type'] == 'label':

                if kwargs['npc_id']:

                    if kwargs['prefix']:
                        label = kwargs['npc_id'] + '.' + \
                            kwargs['prefix'] + '_' + kwargs['what']
                        if renpy.has_label(label):
                            renpy.call_in_new_context(label)
                            return True

                    label = kwargs['npc_id'] + '_' + kwargs['what']
                    if renpy.has_label(label):
                        renpy.call_in_new_context(label)
                        return True

                    label = kwargs['what']
                    if renpy.has_label(label):
                        renpy.call_in_new_context(label)
                        return True

                else:

                    label = kwargs['what']
                    if renpy.has_label(label):
                        renpy.call_in_new_context(label)
                        return True
            else:

                try:
                    jfile = ramu.npc(kwargs['npc_id'], 'json')[kwargs['what']]
                except BaseException:
                    jfile = None

                if jfile:
                    dialogue = ramu.json_file(jfile)

                    if not kwargs['prefix']:
                        d = ramu.random_of(dialogue.keys())
                    else:
                        d = kwargs['prefix']

                    npc = True
                    who = character.__dict__[kwargs['npc_id']]

                    for line in dialogue[d]:
                        if not npc:
                            if not line == "":
                                character.mc(line)
                            npc = True
                        else:
                            if not line == "":
                                who(line)
                            npc = False

                    return True

                else:
                    return False

            return False

        # json

        def json_file(self, file):
            try:
                with open(renpy.loader.transfn(file), 'r') as json_file:
                    return json.load(json_file)
            except BaseException:
                return {'0': ['Hi, please tell the developer, that his JSON file was invalid.']}

        def json_write(self, file, data):
            with open(renpy.loader.transfn(file), 'w') as outfile:
                json.dump(data, outfile)
