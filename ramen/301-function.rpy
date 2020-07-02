init -301 python:

    class ramen_util():

        def create_items(self, key, **kwargs):
            """
            Return list of mass create items

            ``` python
                    items = ramu.create_items(
                        'zd_',
                        price=ramu.random_int(20, 29),
                        eatable=True,
                        effect={'energy': 3 }
                        )
            ```
            """

            res=[]
            for f in sorted( self.files(self.getdir(), key, pe.ext_img) ):

                fn = self.file_info(f)
                count = 1
                r = fn.name.strip().lower()

                for m in pe.itemd:
                    try:
                        kwargs[m]
                    except BaseException:
                        kwargs[m] = pe.itemd[m]

                define_item(
                    r,
                    name=self.str_nicenaming(r, (key, 'item-')),
                    price=kwargs['price'],
                    count=kwargs['count'],
                    require=kwargs['require'],
                    effect=kwargs['effect'],
                    eatable=kwargs['eatable']
                )

                res.append(r)

            return res

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

        def globalcheck(self, what):
            """
            Check where if [what] is in globals. Sometimes [what] retrieve from multipersistent, this to check whenever [what] came from this game or not.
            """

            try:
                globals()[what]
                return True
            except BaseException:
                return False

        def uid(self):
            """Return Next Unique ID for creations. 3 Decimal format."""

            ramen.uidnumber += 1
            return "{:03d}".format(ramen.uidnumber)

        def shuffle(self, array):
            """Short of renpy.random.shuffle"""

            renpy.random.shuffle(array)
            return array

        def select(self, key, list):
            """Return selected [key] from list"""

            return filter(lambda w: key in w, list)

        def kdict(self, **kwargs):
            """Return dict from keywords arguments."""

            dict={}
            for k in kwargs:
                dict[k] = kwargs[k]
            return dict

        def makeobj(self, args, **kwargs):
            """
            Return object from {} or keywords arguments.

            from a hash/list

            ``` python:
                obj = ramu.makeobj( {'id':1, 'name':'someting'})
            ```

            from keyword arguments:

            ``` python:
                obj = ramu.makeobj( id=1, name=someting )
            ```
            """

            obj = object()
            obj.__dict__ = kwargs
            if isinstance(args, (type(self.__dict__), type({}))):
                for a in args:
                    obj.__dict__[str(a)] = args[a]
            return obj

        def cycle(self, current, array):
            """Return n+1 or 0 if n>len(array)"""

            current = int(current) + 1
            if current >= len(array) or current < 0:
                current = 0
            return int(current)

        def str_proper(self, text, title=True):
            """Return IBM(less or 4 character), Ii Bb Mm if title=True"""

            if len(text)<=4:
                return text.upper()
            else:
                if title:
                    return text.title()
                else:
                    return text

        def str_safe(self, text):
            """Return 'safenamebonanza' from 'Safe Name Bonanza'"""
            return re.sub(r'\W+|\s+', '', text).lower().strip()

        def str_firstcap(self, text):
            """Return 'Snb' from 'Safe Name Bonanza', used most in thumbnail/icon creation."""

            res = ''
            tt = text.split(' ')
            for t in tt:
                res += t[0]
            return res.title()

        def str_nicecash(self, n):
            """Return 009 from 9 and 8.2 K from 8200"""

            if n < 1000:
                return ("{:03d}".format(n))
            elif n > 1000:
                return ("{:0.1f}".format(n / 1000)) + "K"

        def str_nicenaming(self, text, prefix='', suffix=''):
            """Return 'Coca Cola' from '[prefix]coca_cola[suffix]. Used in item creations. Prefix and suffix can be tuple."""

            pre = []
            suf = []

            if not isinstance(prefix, tuple):
                pre.append(prefix)
            else:
                pre = prefix

            if not isinstance(suffix, tuple):
                suf.append(suffix)
            else:
                suf = suffix

            for p in pre:
                text = text.replace(p, '')
            for s in suf:
                text = text.replace(s, '')

            return text.replace('_', ' ').strip().title()

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

        def file_info(self, file):
            """
            Get and extract the file information of the file as dict.

            ``` python:
                info = ramu.file_info("e:/yourproject/game/npc/girls_of_90/alpha/lucy smile.webp")
            ```

            * info.file = lucy smile.webp
            * info.name = lucy smile
            * info.ext = webp
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
                #find.insert(0, path)
                find.append(path)

            res = None

            for f in find:
                res = self.ezfile(f+file, None, ext)
                if res is not None:
                    break

            return res

        def file_write(self, file, text, mod="w"):
            """Write a [text] to [file]. mod='a' for appending, mod='w' for (re)write."""

            file = open(file, mod)
            file.writelines(text.strip())
            file.close()
            return file

        def json_file(self, file):
            """Return data from json file"""

            try:
                with open(renpy.loader.transfn(file), 'r') as json_file:
                    return json.load(json_file)
            except BaseException:
                return {'0': ['Hi, please tell the developer, that his JSON file was not valid.']}

        def json_write(self, file, data):
            """Dump data to json file"""

            with open(renpy.loader.transfn(file), 'w') as outfile:
                json.dump(data, outfile)

        def random_int(self, min=0, max=100):
            """Return random from [min] till [max]"""

            return int(renpy.random.randint(min, max))

        def random_of(self, data):
            """Return randomize value from list """

            return data[int(renpy.random.randint(0, len(data) - 1))]

        def random_color(self, lo=0, hi=255):
            """Return random hex Color"""

            if lo < 96:
                lo = 96
            if hi > 255:
                hi = 255

            def r(): return self.random_int(lo, hi)
            return ('#%02X%02X%02X' % (r(), r(), r()))

        def random_files(self, dir=False, key=False, ext=pe.ext_img):
            """Return random files for [dir] with [key] as keyword"""

            files = self.files(dir, key, ext)
            return self.random_of(files)

        def uniquedict(self, data):
            """Return unique and sorted data from a dict"""

            if isinstance(data, list):
                res = []
                for x in range(0, len(data)):
                    res.append(self.uniquedict(data[x]))

            elif isinstance(data, tuple):
                return data

            elif isinstance(data, dict):
                res = {}
                for k in sorted(data.keys()):
                    res[k] = self.uniquedict(data[k])

                return res

            elif isinstance(data, (str, int, float, unicode) ):
                if isinstance(data, (unicode, str)):
                    return data.lower().strip()
                if isinstance(data, (float, int)):
                    return data
                else:
                    return str(data)

            return sorted(list(res))

        def persistent_sort(self, what):
            """Sort and remove duplicate in `persistent.ramen`"""

            L = persistent.ramen[what]
            N = {}
            for k in L:
                N[k]=ramu.uniquedict(L[k])
            persistent.ramen[what] = N

        def arrayize(self, array, length, default=None):
            """

            Return/convert list from inputed list to be same length, when it not satified use default value

            ``` python:
                i = 20
                i = ramu.arrayize(i, 3, (0.0, 0.0))
                > print i
                [20,4,4]
            ```

            """

            if isinstance(array, (unicode, str, int, type(Composite((0, 0))))):
                sarray=[]
                sarray.append(array)
            else:
                sarray = array

            if len(sarray) == length:
                return sarray
            else:
                for n in range(0, length):
                    try:
                        sarray[n]
                    except BaseException:
                        sarray.insert(n, default)

            return sarray

        def npc(self, npc_id, what):

            try:
                if type(globals()[npc_id]) is not ramen_npc:
                    return False
            except BaseException:
                pass

            try:
                return globals()[npc_id]._get(what)
            except BaseException:
                return None

    # ----------------------------------------------------- #

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

        def trait(self, which, value):

            # radio,it,managing,writing

            mc.job[which] = self.limits(mc.job[which]+value)
            return mc.job[which]

        def gain(self, m, src, ret=False):
            src += m
            res = True

            if ret:
                return res

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
            return float(value)

        def mouse(self):
            """Get Mouse pos, return (x,y)"""
            return pygame.mouse.get_pos()

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

                print 'callback '+ ramentime.word()+ " "+ramen.label_last

                events = filter(lambda w: ramen.label_last.lower() == ramen.events.__dict__[w].__dict__['label'], ramen.events.__dict__ )

                print events

                for event in events:
                    e = Event(event)
                    print event + " read"
                    if e.occur():
                        print event + " -- occur!"
                        renpy.jump(e.jump)
                        break

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

        def sfx(self, file, path=None, channel='sound', **kwargs):

            res = self.ezfind(file, 'sound', path)

            if res is not None:
                renpy.sound.play(res, channel=channel, **kwargs)
            else:
                return False

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
            $ ramu.talk(npc_id='rita',what='chat',type='label')
            ```

            Make a phone talk using label (fallback):

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
            $ ramu.talk(npc_id='rita',what='conversation1',type='json')
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

            you can validate the JSON on : https://jsonlint.com/

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

                    label = kwargs['npc_id'] + '.' + kwargs['what']
                    if renpy.has_label(label):
                        renpy.call_in_new_context(label)
                        return True

                    label = kwargs['what']
                    if renpy.has_label(label):
                        renpy.call_in_new_context(label)
                        return True

                else:
                    sysnote('missing '+label)
                    return None
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
