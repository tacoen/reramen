init -290 python:

    register_plugins (
        title="App Container",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/reramen',
        desc="small apps in screen",
        build=True
    )

    ramen.active_apps = {}
    
    class ramen_apps(ramen_extendable):
    
        def init(self,id=None,*args,**kwargs):
            self.__dict__['apps'] = ramen_persistent(self.id)
            try: ramen.active_apps[self.id]
            except: ramen.active_apps[self.id]=[]

        def register(self, what=None,**kwargs):
            
            if what is None:
                what = os.path.basename(renpy.get_filename_line()[0]).replace('.rpy','')
                
            what = what.lower().strip()

            try: kwargs['dir']
            except: kwargs['dir'] = ramu.getdir()
            
            try: kwargs['icon']
            except: 
                icon = ramu.ezfile(ramu.getdir()+what)
                if icon is not None:
                    kwargs['icon']=icon
                else:
                    kwargs['icon'] = ramu.ezfile2(ramu.getdir()+"icon")

            try: kwargs['order']="{:03d}".format(kwargs['order'])
            except: kwargs['order']=ramu.uid()
            
            try: 
                if kwargs['active']:
                    ramen.active_apps[self.id].append(kwargs['order']+":"+what)
                    ramen.active_apps[self.id] = list(ramen.active_apps[self.id])
            except:
                kwargs['active'] = False

            try: kwargs['title']
            except:
                kwargs['title'] = what.title()
                
            try: kwargs['start']
            except:
                kwargs['start'] = self.id+"_apps_"+what
        
            self.apps._set(what,kwargs)
            
        def activated(self,what,state=True):
            if state:
                ramen.active_apps[self.id].append(kwargs['order']+":"+what)
                ramen.active_apps[self.id] = list(ramen.active_apps[self.id])
            else:
                try: ramen.active_apps[self.id].pop(what)
                except: pass
                
        def get(self, what, attr=None):
            if attr is None:
                return self.apps()[what]
            else:
                try: self.apps()[what][attr]
                except: return None
