init -200 python:

    class npc(ramen_object):

        def load(self, *args, **kwargs):
            self.setdir()
            self.dict(**kwargs)
            
            try: self.name
            except: self.name = self.id.title()

            try: del kwargs['name']
            except: pass
            
            ramu.character(self.id,self.name, **kwargs)

            self.define_byfile()
 
        def define_byfile(self):

            files = ramu.files(self.id,False,RAMEN_IMG_EXT+RAMEN_TXT_EXT)
            pose = {}
            
            for f in files:
                fn = ramu.file_info(f)
                
                if fn.ext == 'json':
                    try: self.__dict__['___'][str('json')]
                    except: self.__dict__['___'][str('json')]={}
                    
                    self.__dict__['___'][str('json')][fn.name]=f                   

                if "."+fn.ext in RAMEN_IMG_EXT:
                
                    if fn.name.lower() == 'profile':
                        self.__dict__['___'][str('profile_pic')] = f
                        
                    elif fn.path == self.id or fn.path == 'pose':
                        pose[fn.name]=f

                    else:
                        try: self.__dict__['___'][fn.path] 
                        except: self.__dict__['___'][fn.path]={}
                        self.__dict__['___'][fn.path][fn.name]=f
                        
            main=False
            
            if len(pose.keys()) >0:

                l = sorted(pose.keys())
            
                for k in pose.keys():
                    if k == 'main':
                        renpy.image(self.id, pose[k])
                        main=True
                    else:
                        renpy.image(self.id + " " + k, pose[k])

                if not main:
                    renpy.image(self.id, pose[l[0]])
                
                self.__dict__['___'][str('pose')] = l

    class player(npc):

        def load(self, *args, **kwargs):
            self.id = 'mc'
            self.setdir('mc')
            self.dict(**kwargs)
            self.newname()

            kwargs['dynamic']=True
            try: del kwargs['name']
            except: pass
            
            ramu.character(self.id, 'mc_name', **kwargs)

            self.define_byfile()
            
        def newname(self, name=None, lastname=None):
            if name is not None:
                self.name = name.title()
            if lastname is not None:
                self.lastname = lastname.title()
            globals()['mc_name'] = self.name
            return self.name

        def bod(self):
            return ramen.time().year - self.age

        def fullname(self):
            return self.name.title() + " " + self.lastname.title()
