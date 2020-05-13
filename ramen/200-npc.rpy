init -200 python:

    class npc(ramen_extendable):

        def init(self,id=None,*args,**kwargs):
        
            try: self.name
            except: self.name = self.id.title()

            try: del kwargs['name']
            except: pass
            
            delme = ramu.character(self.id,self.name, **kwargs)

            for d in delme:
                del self.__dict__[d]
 
            self.define_byfile()
            
 
        def define_byfile(self):

            files = ramu.files(self.dir,self.id,pe.ext_img+pe.ext_txt)
            pose = {}
            
            for f in files:
                fn = ramu.file_info(f)
                
                if fn.ext == 'json':
                    try: self.__dict__[str('json')]
                    except: self.__dict__[str('json')]={}
                    
                    self.__dict__[str('json')][fn.name]=f                   

                if "."+fn.ext in pe.ext_img:
                
                    if fn.name.lower() == 'profile':
                        self.__dict__[str('profile_pic')] = f
                        
                    elif fn.path == self.id or fn.path == 'pose':
                        pose[fn.name]=f

                    else:
                        try: self.__dict__[fn.path] 
                        except: self.__dict__[fn.path]={}
                        self.__dict__[fn.path][fn.name]=f
                        
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
                
                self.__dict__[str('pose')] = l