init -200 python:

    ramen.last_map = None
    
    class ramen_map(object):
    
        def __init__(self, obj_id, scene, branch=[], *args, **kwargs):
        
            try: persistent.ramen['map']
            except: persistent.ramen['map'] = {}
            try: persistent.ramen['map'][obj_id]
            except: persistent.ramen['map'][str(obj_id)] = {}
            try: persistent.ramen['map'][obj_id][scene]
            except: persistent.ramen['map'][obj_id][str(scene)] = {}

            self.obj_id = obj_id
            self.scene = scene

            map = persistent.ramen['map'][obj_id][scene]
            
            branch =[str(i) for i in branch]
            
            try: map['branch']
            except: map[str('branch')] = sorted(branch)
            
            for a in ['way','func','spot','img']:
                try: map[a]
                except: map[str(a)]={}
            
            self.map = map
            
        def __call__(self):
            return self.map
            
        def add_branch(self,what):
            self.map['branch'].append(str(what))
            self.map['branch'] = sorted( list(dict.fromkeys(self.map['branch'])))
        
        def set(self,what,key,value):
            try: self.map[what]
            except: self.map[str(what)]={}
            
            if key in self.map['branch']:
                self.map[what][str(key)]=str(value)
            
        def get(self,what,key=None):
            if key is None:
                return self.map[what]
            else:
                return self.map[what][key]
        
        def way(self,key,value=None):
            if value is not None:
                self.set('way',key,value)
            try: return self.get('way',key)
            except: return None
            
        def spot(self,key,value=None):
            if value is not None:
                self.set('spot',key,value)
            try: return self.get('spot',key)
            except: return None

        def func(self,key,value=None):

            if value is not None:
                self.set('func',key,value)
            else:

                try: func = self.get('func',key)
                except: func = False
                
                if not func:
                    way = self.get('way',key)
                    obj_str = self.obj_id+'_'
                    ways = [
                        obj_str+self.scene+'_'+way,
                        obj_str+way,
                        self.scene+"_"+way,
                        way,
                    ]
                    
                    for label in ways:
                        if renpy.has_label(label):
                            func = Jump(label)
                            break
                            
                    if not func:
                        try: 
                            persistent.ramen['map'][self.obj_id][way]
                            map2map = True
                        except:
                            map2map = False
                            
                        if map2map:
                            func = Function(scene_map,id=value)
                        else:
                            func = Null
                            
            return [
                SetVariable('ramen.last_map',self.scene), func
            ]
        
        def img(self,key,value=None):

            if value is not None:
                self.set('img',key,value)
                
            else:
                try: 
                    img = self.get('img',key)
                except:
                    img = False

                if img:
                    rimg = ramu.ezfile2(self.dir+'hs/'+img)
            
                if not img or rimg is None:
                    rimg = Composite((200,200),(0,0),Color('#f003'),(20,20),Text('N/A'))

                return rimg

    class ramen_scene(ramen_extendable):

        def init(self, id=None, *args, **kwargs):
            self.define_byfile()
            self.map={}
            
        def define_map(self,scene,branch=[]):
            self.map[scene]=ramen_map(self.id,scene,branch)
            
        def define_byfile(self):

            tdir = []
            for d in self.dir:
                tdir.append(d + 'scene')

            condition = sorted(
                list(
                    dict.fromkeys(
                        pe.time_cond +
                        pe.time_word +
                        pe.time_ico)))
            cond = ()
            files = ramu.files(tdir, False, pe.ext_img + pe.ext_txt)

            res = {}

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
                    else:

                        est(fn.path, fn.name)
                        res[fn.path][fn.name]['main'] = f

                else:
                    res[fn.path][fn.name] = f

            for k in res['scene']:
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
                    renpy.image(self.id + " " + k, res['scene'][k]['main'])
                    res['scene'][k] = res['scene'][k]['main']

            for k in res:
                self.__dict__[k] = res[k]
