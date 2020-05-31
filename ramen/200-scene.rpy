init -200 python:

    class ramen_scene(ramen_extendable):

        def init(self, id=None, *args, **kwargs):
            self.define_byfile()
            self.map = {}

        def define_map(self, map, **kwargs):
            self.kdict('pos', **kwargs)
            for a in map:
                self.map[a] = ramen_map(self.id, self.pos, self.dir, a)

        def reinit(self):
            self.define_byfile()

        def define_byfile(self):

            tdir = []
            prop = [ 'scene', 'overlay' ]

            for d in self.dir:
                for p in prop:
                    tdir.append(d + p)

            condition = sorted(
                list(
                    dict.fromkeys(
                        pe.time_cond +
                        pe.time_word +
                        pe.time_ico)))
            cond = ()

            files = ramu.files(tdir, False, pe.ext_img + pe.ext_txt)

            res = {}
            res['scene']={}

            def est(where, what=None):
                try:
                    res[where]
                except BaseException:
                    res[where] = {}
                if what is not None:
                    try:
                        res[where][what]
                    except BaseException:
                        res[where][what] = {}

            for f in files:

                fn = ramu.file_info(f)
                est(fn.path)

                if fn.path == 'scene':

                    if ' ' in fn.name:
                        fnn = fn.name.split(' ')
                        if self.exist('scene', fnn[0]):
                            continue
                    else:
                        if self.exist('scene', fn.name):
                            continue

                    if ' ' in fn.name:

                        withcondition=False

                        for c in condition:

                            if ' ' + c.lower() in fn.name:

                                fnn = fn.name.split(' ')
                                est(fn.path, fnn[0])

                                try:
                                    res[fn.path][fnn[0]]['cond']
                                except BaseException:
                                    res[fn.path][fnn[0]]['cond'] = ()

                                if c in pe.time_ico:
                                    res[fn.path][fnn[0]
                                                 ]['cond'] += ("ramentime.ico()=='" + c + "'", f)
                                elif c in pe.time_word:
                                    res[fn.path][fnn[0]
                                                 ]['cond'] += ("ramentime.word()=='" + c + "'", f)
                                elif c in pe.time_cond:
                                    res[fn.path][fnn[0]
                                                 ]['cond'] += ("ramentime.cond()=='" + c + "'", f)
                                withcondition=True

                        if withcondition:
                            try:
                                res[fn.path][fnn[0]]['main']
                                continue
                            except BaseException:
                                fnn = fn.name.split(' ')
                                est(fn.path, fnn[0])
                                res[fn.path][fnn[0]]['main'] = f
                        else:
                            est(fn.path, fn.name)
                            res[fn.path][fn.name]['main'] = f

                    #---
                    else:

                        est(fn.path, fn.name)
                        res[fn.path][fn.name]['main'] = f

                elif fn.path=='overlay':
                    res[fn.path][fn.name] = f

                else:
                    print "----"
                    print fn.path
                    #res[fn.path][fn.name] = f

            #111
            for k in res['scene']:

                if self.exist('scene', k):
                    continue

                try:
                    res['scene'][k]['cond']
                    res['scene'][k]['cond'] += (True, res['scene'][k]['main'])
                    renpy.image(
                        self.id + " " + k,
                        ConditionSwitch(
                            *res['scene'][k]['cond']))
                    del res['scene'][k]['main']
                    res['scene'][k] = res['scene'][k]['cond']

                except BaseException:
                    try:
                        renpy.image(self.id + " " + k, res['scene'][k]['main'])
                        res['scene'][k] = res['scene'][k]['main']
                    except BaseException:
                        pass

            print res

            for k in res:

                try:
                    self.__dict__[k]
                except BaseException:
                    self.__dict__[k] = {}

                self.__dict__[k].update(res[k])

    class ramen_map(object):

        def __init__(self, obj_id, pos, dir, scene):

            try:
                persistent.ramen['map']
            except BaseException:
                persistent.ramen['map'] = {}
            try:
                persistent.ramen['map'][obj_id]
            except BaseException:
                persistent.ramen['map'][str(obj_id)] = {}
            try:
                persistent.ramen['map'][obj_id][scene]
            except BaseException:
                persistent.ramen['map'][str(obj_id)][str(scene)] = {}

            self.map = persistent.ramen['map'][str(obj_id)][scene]
            self.base_pos = pos
            self.dir = dir
            self.obj_id = obj_id
            self.scene = scene

            try:
                globals()[obj_id].last_scene
            except BaseException:
                globals()[obj_id].last_scene=''

            try:
                globals()[obj_id].last_key
            except BaseException:
                globals()[obj_id].last_key=''

        def __call__(self):
            return self.map

        def set(self, what, key, value):

            try:
                self.map[what]
            except BaseException:
                self.map[str(what)]={}

            self.map[what][str(key)] = value

        def get(self, what, key):

            try:
                return self.map[what][key]
            except BaseException:
                return None

        def kdict(self, what, **kwargs):
            for k in kwargs:
                self.set(what, k, kwargs[k])

        def point(self, key, **kwargs):
            for k in kwargs:
                self.set(k, key, kwargs[k])

        def branch(self):
            try:
                branch = self.map['pos'].keys()
            except BaseException:
                branch =[]

            branch +=self.base_pos.keys()

            return sorted(list(dict.fromkeys(branch)))

        def trans(self, key, value=None):
            if value is not None:
                self.set('trans', key, value)
            else:
                return self.get('trans', key)

        def pos(self, key, value=None):
            if value is not None:
                self.set('pos', key, value)
            else:

                if self.get('pos', key) is None:

                    try:
                        return self.base_pos[key]
                    except BaseException:
                        return None
                else:
                    return self.get('pos', key)

        def way(self, key, value=None):
            if value is not None:
                self.set('way', key, value)
            else:
                way = self.get('way', key)
                if way is None:
                    hasfunc = self.get('func', key)
                    if hasfunc is not None:
                        return True
                else:
                    return way

        def img(self, key, value=None):

            def guess_img(dir, key):

                img = None

                img = ramu.ezfile(dir + 'hs/' + key)

                if img is None:
                    img = ramu.ezfile(dir + 'hs/' + key + '-hover')

                if img is None:
                    img = ramu.ezfile(dir + 'scene/hs/' + key)

                if img is None:
                    img = ramu.ezfile(dir + 'scene/hs/' + key + '-hover')

                return img

            if value is not None:
                self.set('img', key, value)

            else:

                img = self.get('img', key)

                if img is None:
                    img = key

                if img is not None:
                    for d in self.dir:
                        img = guess_img(d, img)
                        if img is not None:
                            break

                if img is None:
                    img = Composite(
                        (200, 200), (0, 0), Color('#f003'), (20, 20), Text('N/A'))

                return img

        def function_proxy(self, func):
            res = globals()[func]()
            if res:
                return res

        def func(self, key, value=None):

            if value is not None:
                self.set('func', key, value)
            else:

                setvars = [
                    SetVariable(self.obj_id+'.last_scene', self.scene),
                    SetVariable(self.obj_id+'.last_key', key),
                    Hide('scene_map')
                ]

                if self.get('trans', key) is None:
                    trans = dissolve

                if self.get('func', key) is None:

                    func = False

                    if not func:
                        way = self.get('way', key)
                        obj_str = self.obj_id + '.'

                        if way is not None:
                            ways = [
                                obj_str + self.scene + '.' + way,
                                obj_str + way,
                                self.scene + "_" + way,
                                way,
                            ]

                            for label in ways:

                                if renpy.has_label(label):
                                    func=[]
                                    func.insert(0, setvars)
                                    func.append(Jump(label))
                                    break

                    if not func:

                        try:
                            if not persistent.ramen['map'][self.obj_id][way]['way'] == {}:
                                func=[]
                                func.append(SetVariable('ramen.map_obj', self.obj_id))
                                func.append(SetVariable(self.obj_id+'.last_key', key))
                                func.append(SetVariable(self.obj_id+'.last_scene', way))
                                func.append(Show('scene_map', transition=trans))
                            else:
                                func = None
                        except BaseException:
                            func = None

                    if func is not None:
                        return func
                    else:
                        return None

                else:

                    func=[]
                    func.insert(0, setvars)
                    func.append(SetVariable('ramen.map_obj', self.obj_id))
                    func.append(Function(self.function_proxy, func=self.get('func', key)))
                    return func
