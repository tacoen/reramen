init -200 python:

    class ramen_npc(ramen_extendable):

        def init(self, id=None, *args, **kwargs):

            if self.name is None:
                self.name = self.id.title()

            if self.lastname is None:
                self.lastname = ramu.random_of(pe.native_name).title()

            try:
                del kwargs['name']
            except BaseException:
                pass

            delme = ramu.character(self.id, self.name, **kwargs)

            for d in delme:
                del self.__dict__[d]

            self.define_byfile()

        def reinit(self):
            self.define_byfile()

        def relation(self, point=None, what='relation'):
            """
            Set/get npc relation stat to main character

            ``` python
            mia.relation(5)
            mia.relation(10,'love')
            mia.relation(3,'obedience')

            >mia.relation()
            {'love':10,'obedience':3}

            ```

            """
            try:
                mc.rel
            except BaseException:
                mc.rel = {}
            try:
                mc.rel[self.id]
            except BaseException:
                mc.rel[self.id] = {}

            if what is None:
                return mc.rel[self.id]
            else:

                try:
                    mc.rel[self.id][what]
                except BaseException:
                    mc.rel[self.id][what] = 0

                if point is None:
                    return mc.rel[self.id][what]
                else:
                    mc.rel[self.id][what] = ramu.limits(
                        mc.rel[self.id][what] + point)
                    return mc.rel[self.id][what]

        def relation_dict(self, **kwargs):
            """
            Set npc relation to main character using keyword arguments

            ```python
            mia.relation_dict(like=8,hate=3)

            >mia.relation()
            {'love':10,'obedience':3,'like':8,'hate':3}

            ```
            """

            for k in kwargs:
                self.relation(k, kwargs[k])

        def define_byfile(self):

            files = ramu.files(self.dir, self.id, pe.ext_img + pe.ext_txt)
            pose = {}

            def file_json(fn, f):
                try:
                    self.__dict__[str('json')]
                except BaseException:
                    self.__dict__[str('json')] = {}
                self.__dict__[str('json')][fn.name] = f

            def file_profile(fn, f):

                self.__dict__[str('profile_pic')] = f
                renpy.image(self.id + ' profile_pic', f)

            for f in files:
                fn = ramu.file_info(f)

                if fn.ext == 'json':
                    file_json(fn, f)
                    continue

                if "." + fn.ext in pe.ext_img:

                    if fn.name.lower() == 'profile':
                        file_profile(fn, f)
                        continue

                    if fn.path == self.id or fn.path == 'pose':
                        pose[fn.name] = f
                    else:
                        try:
                            self.__dict__[fn.path]
                        except BaseException:
                            self.__dict__[fn.path] = {}
                        self.__dict__[fn.path][fn.name] = f

            main = False

            if len(pose.keys()) > 0:

                l = sorted(pose.keys())

                for k in pose.keys():

                    if self.exist('pose', k):
                        continue

                    if k == 'main':
                        renpy.image(self.id, pose[k])
                        main = True
                    else:
                        renpy.image(self.id + " " + k, pose[k])

                    #self.__dict__[str('pose')].append(k)

                if not main:
                    renpy.image(self.id, pose[l[0]])

                self.__dict__[str('pose')] = l

            try:
                if len(self.__dict__['sprite']) > 0:
                    for s in self.sprite.keys():
                       renpy.image(self.id+" sprite "+s, self.sprite[s])
            except:
                pass

        def create_sideimage(self, img, temp_img, tag, cut=None):

            compo = Composite(
                (340, 340),
                (0, 0), temp_img,
                (105, 112), At(im.Scale(img, 96, 96, bilinear=True))
            )

            if cut is not None:
                what = tag.replace(cut, '')
            else:
                what = tag

            renpy.image("side " + self.id + " " + what, compo)

        def setup_phone(self, fordig=None, sideimg_dir=None):

            if fordig is None:
                fordig = "{:04d}".format(ramu.random_int(650, 9998))

            self.phonenum = "5555-" + fordig

            if sideimg_dir is not None:

                for i in ['phone-incall', 'phone-outcall', 'phone-oncall']:
                    temp_img = ramu.ezfind(i, 'image', sideimg_dir )
                    if temp_img is not None:
                        self.create_sideimage(self.profile_pic, temp_img, i)

            return self.phonenum


        def spriteanim(self, name, seq, tick=1.0, transform=basic_anim):
            anim =()

            if isinstance(seq,(str,unicode)):
                seq = filter(lambda w: seq in w, self.sprite.keys())

            for s in seq:
                print seq
                print "+++"
                if isinstance(s,tuple):
                    print 'tuple'
                    print s
                    if s[0] in self.sprite:
                        tick = float(s[1])
                        anim = anim + ( At(self.sprite[s[0]],transform), tick )
                else:
                    if s in self.sprite:
                        print "auto"
                        print s
                        anim = anim + ( At(self.sprite[s],transform), tick )

            renpy.image((self.id, name), Animation(*anim))


transform Expression(who, npc_expression, pos=(0, 0)):
    xpos int(ramu.imgexpo(who, 'bound')[0])+ int(ramu.npc(who, 'expression_pos')[0])
    ypos int(ramu.imgexpo(who, 'bound')[1])+ int(ramu.npc(who, 'expression_pos')[1])
    ramu.npc(who, 'expression')[npc_expression]
