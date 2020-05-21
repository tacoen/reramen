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

        def set_phonenum(self, fordig=None):

            if fordig is None:
                fordig = "{:04d}".format(ramu.random_int(650, 9998))

            self.phonenum = "5555-" + fordig

            return self.phonenum

        def relation(self, what=None, point=None):
            """
            Set/get npc relation stat to main character

            ``` python
            mia.relation('love',10)
            mia.relation('obedience',3)

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

                for i in ['phone-incall', 'phone-outcall', 'phone-oncall']:
                    temp_img = ramu.ezfile(pe.image_path + 'side/' + i)
                    if temp_img is not None:
                        self.create_sideimage(f, temp_img, i, cut='phone-')

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
                    if k == 'main':
                        renpy.image(self.id, pose[k])
                        main = True
                    else:
                        renpy.image(self.id + " " + k, pose[k])

                if not main:
                    renpy.image(self.id, pose[l[0]])

                self.__dict__[str('pose')] = l

        def create_sideimage(self, img, temp_img, tag, cut='phone-'):

            if temp_img:
                compo = Composite(
                    (340, 340),
                    (0, 0), temp_img,
                    (105, 112), At(im.Scale(img, 96, 96, bilinear=True))
                )

                what = tag.replace(cut, '')
                renpy.image("side " + self.id + " " + what, compo)

